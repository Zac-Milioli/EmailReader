from imap_tools import MailBox, AND
import pandas as pd
import json

user = ''
password = ''

email = MailBox('imap.gmail.com').login(user, password)

listagem_email = email.fetch(criteria=AND(seen=False), mark_seen=False)

keyword = 'RESPOSTAS DE '

for msg in listagem_email:
    answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
    texto = msg.text.replace("\'", "\"").replace('None', 'null').replace("\r", '').replace('\n', ' ').replace('\t', ' ')
    texto = json.loads(texto)
    df = pd.DataFrame(texto)
    print(df)
