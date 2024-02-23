import pandas as pd
import json
from glob import glob
import os
from time import sleep
from imap_tools import MailBox, AND

user = 'escritorios.qai.bot@gmail.com'
password = 'sxux ztfv fsiw'

def fetch_emails():
    email = MailBox('imap.gmail.com').login(user, password)

    listagem_email = email.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True) 

    listagem_email = list(listagem_email)
    tamanho = len(listagem_email)

    if tamanho != 0:
        counter = 0
        for msg in listagem_email:
            sleep(0.3)
            if len(msg.text) < 5:
                print(f'Empty mail found. {msg}\n')
            elif keyword != '' and keyword not in msg.subject:
                print(f'Mail without keyword returned. {msg}\n')
                pass
            else:
                counter += 1
                answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
                name = answer_mail.replace('.', '').split('@')[0]
                print(f'Processing mail from {answer_mail},\tnumber {counter}\n')
                corpo = msg.text.replace("\n", '').replace('None', '"sem comentários"').replace('-', '').replace("'", '"').lower()
                corpo = json.loads(corpo, strict=False)
                try:
                    df = pd.DataFrame()
                    df['id_pergunta'] = corpo['id_pergunta']
                    df['resposta'] = corpo['resposta']
                    df['email'] = answer_mail
                    df.to_csv(f'MAIL_{counter}_{name}.csv', encoding='latin-1', sep=';')
                except:
                    print(f'\nERROR. Not possible to create DataFrame from {answer_mail}: {msg.text}\n')

def join_dataframes():
    globed = glob('MAIL_*.csv')
    size_globed = len(globed)
    if size_globed < 1:
        print('No DataFrames to join...\n')
    else:
        principal = pd.read_csv(globed[0], encoding='latin-1', sep=';')
        os.remove(globed[0])
        globed.pop(0)
        for i in globed:
            sleep(0.3)
            print(f'Joining DataFrame {i} to the main\n')
            new = pd.read_csv(i, encoding='latin-1',sep=';')
            try:
                principal = pd.concat([principal, new], ignore_index=True)
                principal.drop(columns='Unnamed: 0', axis=1, inplace=True)
                os.remove(i)
            except:
                print(f'Could not concatenate DataFrame {i}\n')
        main_already = glob('MAIN_DATAFRAME.csv')
        if len(main_already) >= 1:
            principal.to_csv(f'MAIN_DATAFRAME({len(main_already)}).csv', encoding='latin-1',sep=';')
        else:
            principal.to_csv('MAIN_DATAFRAME.csv', encoding='latin-1',sep=';')
    sleep(0.3)
    print('Joining complete\n')