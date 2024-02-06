import customtkinter as ctk
import pandas as pd
import json
from glob import glob
import os
from time import sleep
from imap_tools import MailBox, AND

fonte_t = ("Inter", 36, 'bold')
fonte = ("Inter", 20, 'bold')
fonte_terminal = ("Inter", 12)
common_pady = 20


class EmailReader:
    def __init__(self, root):
        wn = root
        wn.geometry('600x800')
        wn.config(background='white')
        wn.title('EmailReader')

        titulo = ctk.CTkLabel(wn, text='EmailReader', font=fonte_t, fg_color='white', text_color='black', bg_color='white')
        titulo.pack(pady=common_pady, expand=True, fill='both')

        fm = ctk.CTkFrame(wn, fg_color='#F2F2F2', corner_radius=0, height=650)
        fm.pack_propagate(False)
        fm.pack(expand=True, fill='x')

        email_entry = ctk.CTkEntry(fm, placeholder_text='Email', justify='center', width=400, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
        email_entry.pack(pady=common_pady)

        password_entry = ctk.CTkEntry(fm, placeholder_text='Senha', justify='center', width=400, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
        password_entry.pack(pady=common_pady)

        chave_entry = ctk.CTkEntry(fm, placeholder_text='Título-chave', justify='center', width=400, height=60, font=fonte, text_color='black', fg_color='white', corner_radius=45, border_color='white', placeholder_text_color='black')
        chave_entry.pack(pady=common_pady)

        terminal_box = ctk.CTkTextbox(fm, fg_color='white', font=fonte_terminal, text_color='black', bg_color='white', border_color='white', height=120)

        def fetch_emails():
            terminal_box.insert('0.0', 'Fetching emails...\n')

            keyword = chave_entry.get()

            user = email_entry.get()
            password = password_entry.get()

            email = MailBox('imap.gmail.com').login(user, password)

            listagem_email = email.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True) 

            listagem_email = list(listagem_email)
            tamanho = len(listagem_email)

            terminal_box.insert('0.0', f'Returned {tamanho} objects\n')
            
            if tamanho != 0:
                counter = 0
                for msg in listagem_email:
                    sleep(0.3)
                    if len(msg.text) < 5:
                        terminal_box.insert('0.0', f'Empty mail found. {msg}\n')
                    elif keyword != '' and keyword not in msg.subject:
                        terminal_box.insert('0.0', f'Mail without keyword returned. {msg}\n')
                        pass
                    else:
                        counter += 1
                        answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
                        name = answer_mail.replace('.', '').split('@')[0]
                        terminal_box.insert('0.0', f'Processing mail from {answer_mail},\tnumber {counter}\n')
                        corpo = msg.text.replace("\n", '').replace('None', '"sem comentários"').replace('-', '').replace("'", '"').lower()
                        corpo = json.loads(corpo, strict=False)
                        try:
                            df = pd.DataFrame()
                            df['id_pergunta'] = corpo['id_pergunta']
                            df['resposta'] = corpo['resposta']
                            df['email'] = answer_mail
                            df.to_csv(f'MAIL_{counter}_{name}.csv', encoding='latin-1', sep=';')
                        except:
                            terminal_box.insert('0.0', f'\nERROR. Not possible to create DataFrame from {answer_mail}: {msg.text}\n')
                sleep(0.3)
                terminal_box.insert('0.0', 'Processing done\n')

        fetch_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Fetch', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50, command=fetch_emails)
        fetch_button.pack(pady=common_pady)
        terminal_box.pack(pady=common_pady, expand=True, fill="x")

        def join_dataframes():
            globed = glob('MAIL_*.csv')
            size_globed = len(globed)
            if size_globed < 1:
                terminal_box.insert('0.0', 'No DataFrames to join...\n')
            else:
                principal = pd.read_csv(globed[0], encoding='latin-1', sep=';')
                os.remove(globed[0])
                globed.pop(0)
                for i in globed:
                    sleep(0.3)
                    terminal_box.insert('0.0', f'Joining DataFrame {i} to the main\n')
                    new = pd.read_csv(i, encoding='latin-1',sep=';')
                    try:
                        principal = pd.concat([principal, new], ignore_index=True)
                        principal.drop(columns='Unnamed: 0', axis=1, inplace=True)
                        os.remove(i)
                    except:
                        terminal_box.insert('0.0', f'Could not concatenate DataFrame {i}\n')
                main_already = glob('MAIN_DATAFRAME.csv')
                if len(main_already) >= 1:
                    principal.to_csv(f'MAIN_DATAFRAME({len(main_already)}).csv', encoding='latin-1',sep=';')
                else:
                    principal.to_csv('MAIN_DATAFRAME.csv', encoding='latin-1',sep=';')
            sleep(0.3)
            terminal_box.insert('0.0', 'Joining complete\n')

        joindf_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Juntar DataFrames', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50, command=join_dataframes)
        joindf_button.pack(pady=common_pady)

        wn.mainloop()

if __name__ == '__main__':
    EmailReader(ctk.CTk())
    