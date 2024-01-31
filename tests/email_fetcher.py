from imap_tools import MailBox, AND
import pandas as pd
import json

user = ''
password = ''

email = MailBox('imap.gmail.com').login(user, password)

listagem_email = email.fetch()

for msg in listagem_email:
    texto = msg.text.replace("\'", "\"").replace('None', '\"null\"')
    texto = json.loads(texto)
    df = pd.DataFrame(texto)

print(df)
