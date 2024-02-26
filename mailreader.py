import pandas as pd
import json
from glob import glob
import os
from time import sleep
from imap_tools import MailBox, AND

user = 'escritorios.qai.bot@gmail.com'
password = 'sxux ztfv fsiw'
megalista = ['q0', 'q1a', 'c0 - conforto térmico', 'c0 - qualidade do ar', 'c0 - conforto visual', 'c0 - conforto acústico', 'c0 - privacidade visual', 'c0 - privacidade acústica', 'c0 - conforto térmico', 'c0 - proximidade de colegas', 'q1b', 'q1c - estação de trabalho', 'q1c - estações de trabalho rotativas', 'q1c - áreas para atividades em grupo', 'q1c - áreas para atividades focadas ou individuais', 'q1c - salas comerciais ou de reunião', 'q1c - atividades externas ou fica fora do escritório', 'q2 - desconforto pelo calor', 'q2 - desconforto pelo frio', 'q2 - desconforto por excesso de vento', 'q2 - desconforto por falta de vento', 'q2 - desconforto por sol direto', 'q2 - desconforto com temperatura de superfícies próximas', 'q2 - desconforto por frio ou calor em partes específicas do corpo', 'q2a - controle de ar-condicionado', 'q2a - controle de ventiladores', 'q2a - satisfacao em meses quentes', 'q2a - satisfacao em meses frios', 'q2a - ambiente térmico em meses quentes - temperatura', 'q2a - ambiente térmico em meses frios - temperatura', 'q2a - movimento do ar em meses quentes - ventilação', 'q2a - movimento do ar em meses frios - ventilação', 'q2a - ambiente térmico em meses quentes - conforto', 'q2a - ambiente  térmico em meses frios - conforto', 'q2a - ar-condicionado', 'q2a - aquecedores', 'q2a - ventilador de teto e/ou parede', 'q2a - ventilador portátil, de mesa e/ou individual', 'q2a - sinto desconforto por calor em meses quentes', 'q2a - sinto desconforto por frio em meses quentes', 'q2a - sinto desconforto porque há muito vento em meses quentes', 'q2a - sinto desconforto porque há pouco vento em meses quentes', 'q2a - o sol direto me atrapalha em meses quentes', 'q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses quentes', 'q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses quentes', 'q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses quentes', 'q2a - outros motivos de desconforto em meses quentes', 'q2a - sinto desconforto por calor em meses frios', 'q2a - sinto desconforto por frio em meses frios', 'q2a - sinto desconforto porque há muito vento em meses frios', 'q2a - sinto desconforto porque há pouco vento em meses frios', 'q2a - o sol direto me atrapalha em meses frios', 'q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses frios', 'q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses frios', 'q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses frios', 'q2a - outros motivos de desconforto em meses frios', 'q3 - desconforto por cheiros e odores', 'q3 - desconforto por ambiente abafado', 'q3 - desconforto com ar interno seco ou úmido demais', 'q3 - desconforto devido à poeira', 'q3a - sinto cheiros e/ou odores no ambiente', 'q3a - sensação de fadiga e/ou sonolência', 'q3a - sensação de ressecamento nos olhos, nariz e/ou mãos', 'q3a - irritações na pele e/ou alergias', 'q3a - nível de satisfação com o ar interno', 'q3a - insatifação por cheiros e odores', 'q3a - insatifação por ambiente abafado', 'q3a - insatifação por ar interno muito seco', 'q3a - insatifação por ar interno muito úmido', 'q3a - insatifação por haver poeira que causa irritação ou alergias', 'q3a - insatifação por haver produtos que causam irritação ou alergias', 'outros motivos', 'q4 - sinto desconforto com o ambiente muito claro (muito iluminado)', 'q4 - sinto desconforto com o ambiente muito escuro (pouco iluminado)', 'q4 - sinto desconforto com o ofuscamento', 'q4 - sinto desconforto com os reflexos na tela do meu computador', 'q4 - sinto desconforto com luzes piscando', 'q4 - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', 'q4a - a disponibilidade de iluminação artificial (lâmpadas e luminárias)?', 'q4a - a ocorrência de ofuscamento gerado pela iluminação artificial?', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o verão e/ou meses quentes', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da manhã', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o inverno e/ou meses frios', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da tarde', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o verão e/ou meses quentes', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da manhã', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o inverno e/ou meses frios', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da tarde', 'q4a - nível de controle sobre iluminação artificial', 'q4a - nível de satisfação com privacidade visual', 'q4a - nível de satisfação com ambiente luminoso', 'q4a - sinto desconforto com o ambiente muito claro (muito iluminado)', 'q4a - sinto desconforto com o ambiente muito escuro (pouco iluminado)', 'q4a - sinto desconforto com o ofuscamento gerado por lâmpadas e luminárias', 'q4a - sinto desconforto com o ofuscamento gerado pela luz do sol e do céu', 'q4a - sinto desconforto com a iluminação que gera reflexos na tela do meu computador', 'q4a - sinto desconforto com luzes piscando', 'q4a - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', 'q4a - outros motivos', 'q5 - sinto desconforto com conversas dos colegas', 'q5 - sinto desconforto com ruídos de equipamentos', 'q5 - sinto desconforto com o barulho externo, vindo da rua', 'q5a - conversas que consigo entener tudo que é dito', 'q5a - conversas de fundo, que não consigo entender o que é dito', 'q5a - teclados, passos, abertura e fechamento de gavetas, etc', 'q5a - ar-condicionado', 'q5a - outros equipamentos', 'q5a - telefones tocando', 'q5a - barulho externo, vindo da rua', 'q5a - qual seu nível de satisfação com a acústica da sua estação de trabalho', 'q5a - as conversas dos colegas me incomodam', 'q5a - o barulho do ar-condicionado me incomoda', 'q5a - o barulho de outros equipamentos me incomoda', 'q5a - o barulho de telefones tocando me incomoda', 'q5a - o barulho externo, vindo da rua, me incomoda', 'q5a - não há um local adequado para ter uma conversa privada com colegas', 'q5a - não hpa um local adequado para fazer um telefonema ou chamada de vídeo', 'hi - conforto térmico', 'hi - qualidade do ar', 'hi - conforto visual', 'hi - conforto acústico', 'hi - ambientes específicos para atividades diferenciadas', 'hi - proximidade e/ou acesso a vistas externas', 'hi - privacidade visual', 'hi - privacidade acústica', 'hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável', 'cg - nível de satisfação com o conforto geral da estação de trabalho', 'cg - comentários', 'cp - controle de ar-condicionado e aquecedores', 'cp - controle de ventiladores', 'cp - controle de janelas', 'cp - controle de cortinas', 'cp - controle de luzes', 'sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento', 'sp - velocidade de resposta à solicitação de controle de ventilação', 'sp - velocidade de resposta à solicitação de alteração de iluminação', 'sp - comentários', 'q6 - faixa etária', 'q6 - escolaridade', 'q6 - gênero']

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

while True:
    
    break
