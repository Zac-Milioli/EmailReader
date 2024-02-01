import customtkinter as ctk
import pandas as pd
import json
from glob import glob
import os
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

            listagem_email = email.fetch(criteria=AND(seen=True), mark_seen=True, bulk=True)

            tamanho = 0
            listagem_email = list(listagem_email)
            for x in listagem_email:
                if keyword != '':
                    if keyword not in x.subject:
                        listagem_email.remove(x)
                    else:
                        tamanho += 1
                else:
                    tamanho += 1

            terminal_box.insert('0.0', f'Returned {tamanho} emails\n')
            
            if tamanho != 0:
                counter = 0
                for msg in listagem_email:
                    counter += 1
                    answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
                    terminal_box.insert('0.0', f'Processing mail from {answer_mail},\tnumber {counter} out of {tamanho}\n')
                    corpo = msg.text.replace("\'", "\"").replace('None', 'null').replace("\r", '').replace('\n', ' ').replace('\t', ' ')
                    corpo = json.loads(corpo)
                    try:
                        df = pd.DataFrame(corpo)
                        df.to_csv(f'MAIL_{counter}.csv', sep=';')
                    except:
                        terminal_box.insert('0.0', f'ERROR AT EMAIL FROM {answer_mail}. skipping...\n')

                terminal_box.insert('0.0', 'Processing done\n')

        fetch_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Fetch', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50, command=fetch_emails)
        fetch_button.pack(pady=common_pady)
        terminal_box.pack(pady=common_pady, expand=True, fill="x")

        def join_dataframes():
            globed = glob('MAIL_*.csv')
            print(globed)
            terminal_box.insert('0.0', 'globed a few dataframes (or not)')

        joindf_button = ctk.CTkButton(fm, fg_color='#A9D18E', text='Juntar DataFrames', font=fonte, hover_color='#000000', text_color='white', corner_radius=45, width=240, height=50, command=join_dataframes)
        joindf_button.pack(pady=common_pady)

        wn.mainloop()

if __name__ == '__main__':
    EmailReader(ctk.CTk())
    