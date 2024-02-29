import pandas as pd
import json
from glob import glob
from imap_tools import MailBox, AND
from datetime import datetime 
from time import sleep
import warnings
warnings.filterwarnings("ignore")

user = 'escritorios.qai.bot@gmail.com'
password = 'sxux ztfv fsiw aqfp'
keyword = 'RESPOSTAS-'
megalista = []

def fetch_emails():
    mails_list = []
    email = MailBox('imap.gmail.com').login(user, password)

    listagem_email = email.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True) 

    listagem_email = list(listagem_email)
    tamanho = len(listagem_email)

    if tamanho != 0:
        for msg in listagem_email:
            print(f'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
            if len(msg.text) < 10:
                print(f'Empty mail found. {msg}\n')
            elif keyword not in msg.subject:
                print(f'Mail without keyword returned. {msg}\n')
            else:
                answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
                name = answer_mail.replace('.', '').split('@')[0]
                corpo = msg.text.replace("\n", '').replace('None', '"sem comentários"').replace('-', '').replace("'", '"').lower()
                corpo = json.loads(corpo, strict=False)
                corpo['email'] = answer_mail
                df = pd.DataFrame([corpo])
                print(df)
                mails_list.append(df)
                sleep(0.2)
        print(f'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        
        big_df = mails_list[0]
        mails_list.pop(0)
        for mail in mails_list:
            big_df = pd.concat([big_df, mail], ignore_index=True)

        big_df.to_csv(f'respostas_retornadas({datetime.now():%d.%m.%y-%I %p}).csv', sep=';', encoding='latin-1')


fetch_emails()
