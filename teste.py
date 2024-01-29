from imap_tools import MailBox, AND

user = 'escritorios.qai.bot@gmail.com'
password = ''

email = MailBox('imap.gmail.com').login(user, password)

listagem_email = email.fetch()

for msg in listagem_email:
    print(msg.subject)
    print(msg.text)