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
megalista = ['email', 'q0', 'q1a', 'c0 - conforto térmico', 'c0 - qualidade do ar', 'c0 - conforto visual', 'c0 - conforto acústico', 'c0 - privacidade visual', 'c0 - privacidade acústica', 'c0 - conforto térmico', 'c0 - proximidade de colegas', 'q1b', 'q1c - estação de trabalho', 'q1c - estações de trabalho rotativas', 'q1c - áreas para atividades em grupo', 'q1c - áreas para atividades focadas ou individuais', 'q1c - salas comerciais ou de reunião', 'q1c - atividades externas ou fica fora do escritório', 'q2 - desconforto pelo calor', 'q2 - desconforto pelo frio', 'q2 - desconforto por excesso de vento', 'q2 - desconforto por falta de vento', 'q2 - desconforto por sol direto', 'q2 - desconforto com temperatura de superfícies próximas', 'q2 - desconforto por frio ou calor em partes específicas do corpo', 'q2a - controle de ar-condicionado', 'q2a - controle de ventiladores', 'q2a - satisfacao em meses quentes', 'q2a - satisfacao em meses frios', 'q2a - ambiente térmico em meses quentes - temperatura', 'q2a - ambiente térmico em meses frios - temperatura', 'q2a - movimento do ar em meses quentes - ventilação', 'q2a - movimento do ar em meses frios - ventilação', 'q2a - ambiente térmico em meses quentes - conforto', 'q2a - ambiente  térmico em meses frios - conforto', 'q2a - ar-condicionado', 'q2a - aquecedores', 'q2a - ventilador de teto e/ou parede', 'q2a - ventilador portátil, de mesa e/ou individual', 'q2a - sinto desconforto por calor em meses quentes', 'q2a - sinto desconforto por frio em meses quentes', 'q2a - sinto desconforto porque há muito vento em meses quentes', 'q2a - sinto desconforto porque há pouco vento em meses quentes', 'q2a - o sol direto me atrapalha em meses quentes', 'q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses quentes', 'q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses quentes', 'q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses quentes', 'q2a - outros motivos de desconforto em meses quentes', 'q2a - sinto desconforto por calor em meses frios', 'q2a - sinto desconforto por frio em meses frios', 'q2a - sinto desconforto porque há muito vento em meses frios', 'q2a - sinto desconforto porque há pouco vento em meses frios', 'q2a - o sol direto me atrapalha em meses frios', 'q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses frios', 'q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses frios', 'q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses frios', 'q2a - outros motivos de desconforto em meses frios', 'q3 - desconforto por cheiros e odores', 'q3 - desconforto por ambiente abafado', 'q3 - desconforto com ar interno seco ou úmido demais', 'q3 - desconforto devido à poeira', 'q3a - sinto cheiros e/ou odores no ambiente', 'q3a - sensação de fadiga e/ou sonolência', 'q3a - sensação de ressecamento nos olhos, nariz e/ou mãos', 'q3a - irritações na pele e/ou alergias', 'q3a - nível de satisfação com o ar interno', 'q3a - insatifação por cheiros e odores', 'q3a - insatifação por ambiente abafado', 'q3a - insatifação por ar interno muito seco', 'q3a - insatifação por ar interno muito úmido', 'q3a - insatifação por haver poeira que causa irritação ou alergias', 'q3a - insatifação por haver produtos que causam irritação ou alergias', 'outros motivos', 'q4 - sinto desconforto com o ambiente muito claro (muito iluminado)', 'q4 - sinto desconforto com o ambiente muito escuro (pouco iluminado)', 'q4 - sinto desconforto com o ofuscamento', 'q4 - sinto desconforto com os reflexos na tela do meu computador', 'q4 - sinto desconforto com luzes piscando', 'q4 - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', 'q4a - a disponibilidade de iluminação artificial (lâmpadas e luminárias)?', 'q4a - a ocorrência de ofuscamento gerado pela iluminação artificial?', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o verão e/ou meses quentes', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da manhã', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o inverno e/ou meses frios', 'q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da tarde', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o verão e/ou meses quentes', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da manhã', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o inverno e/ou meses frios', 'q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da tarde', 'q4a - nível de controle sobre iluminação artificial', 'q4a - nível de satisfação com privacidade visual', 'q4a - nível de satisfação com ambiente luminoso', 'q4a - sinto desconforto com o ambiente muito claro (muito iluminado)', 'q4a - sinto desconforto com o ambiente muito escuro (pouco iluminado)', 'q4a - sinto desconforto com o ofuscamento gerado por lâmpadas e luminárias', 'q4a - sinto desconforto com o ofuscamento gerado pela luz do sol e do céu', 'q4a - sinto desconforto com a iluminação que gera reflexos na tela do meu computador', 'q4a - sinto desconforto com luzes piscando', 'q4a - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', 'q4a - outros motivos', 'q5 - sinto desconforto com conversas dos colegas', 'q5 - sinto desconforto com ruídos de equipamentos', 'q5 - sinto desconforto com o barulho externo, vindo da rua', 'q5a - conversas que consigo entener tudo que é dito', 'q5a - conversas de fundo, que não consigo entender o que é dito', 'q5a - teclados, passos, abertura e fechamento de gavetas, etc', 'q5a - ar-condicionado', 'q5a - outros equipamentos', 'q5a - telefones tocando', 'q5a - barulho externo, vindo da rua', 'q5a - qual seu nível de satisfação com a acústica da sua estação de trabalho', 'q5a - as conversas dos colegas me incomodam', 'q5a - o barulho do ar-condicionado me incomoda', 'q5a - o barulho de outros equipamentos me incomoda', 'q5a - o barulho de telefones tocando me incomoda', 'q5a - o barulho externo, vindo da rua, me incomoda', 'q5a - não há um local adequado para ter uma conversa privada com colegas', 'q5a - não hpa um local adequado para fazer um telefonema ou chamada de vídeo', 'hi - conforto térmico', 'hi - qualidade do ar', 'hi - conforto visual', 'hi - conforto acústico', 'hi - ambientes específicos para atividades diferenciadas', 'hi - proximidade e/ou acesso a vistas externas', 'hi - privacidade visual', 'hi - privacidade acústica', 'hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável', 'cg - nível de satisfação com o conforto geral da estação de trabalho', 'cg - comentários', 'cp - controle de ar-condicionado e aquecedores', 'cp - controle de ventiladores', 'cp - controle de janelas', 'cp - controle de cortinas', 'cp - controle de luzes', 'sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento', 'sp - velocidade de resposta à solicitação de controle de ventilação', 'sp - velocidade de resposta à solicitação de alteração de iluminação', 'sp - comentários', 'q6 - faixa etária', 'q6 - escolaridade', 'q6 - gênero']

def fetch_emails():
    mails_list = []
    email = MailBox('imap.gmail.com').login(user, password)

    listagem_email = email.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True) 

    listagem_email = list(listagem_email)
    tamanho = len(listagem_email)

    if tamanho != 0:
        for msg in listagem_email:
            if len(msg.text) < 10:
                print(f'Empty mail found. {msg}\n')
            elif keyword not in msg.subject:
                print(f'Mail without keyword returned. {msg}\n')
            else:
                answer_mail = msg.subject.replace(keyword, '').replace(' ', '')
                name = answer_mail.replace('.', '').split('@')[0]
                corpo = msg.text.replace("\n", '').replace('None', '"sem comentários"').replace('-', '').replace("'", '"').lower()
                corpo = json.loads(corpo, strict=False)
                corpo['id_pergunta'].append('email')
                corpo['resposta'].append(answer_mail)
                missing_items = set(megalista) - set(corpo['id_pergunta'])
                for item in missing_items:
                    corpo['id_pergunta'].append(item)
                    corpo['resposta'].append(None)
                if len(corpo['id_pergunta']) != len(corpo['resposta']):
                    diferenca = len(corpo['id_pergunta']) - len(corpo['resposta'])
                    if diferenca != 0:
                        print(f'Different lenghts between id_pergunta and resposta ({diferenca}) at mail from {answer_mail}.\n')
                        open(f'diferente_num_pergunta_resposta_at_mail_{name}.txt', 'w').write(f'ERROR. Different lenghts between id_pergunta and resposta ({diferenca}). lenght id_pergunta: {len(corpo["id_pergunta"])} lenght resposta: {len(corpo["resposta"])}\nbody: {corpo}\n')
                    for _ in range(diferenca):
                        corpo['resposta'].append(None)
                df = pd.DataFrame(corpo)
                df.set_index('id_pergunta', inplace=True, drop=True)
                df = df.transpose()
                print(df)
                mails_list.append(df)
                sleep(0.2)
        
        big_df = mails_list[0]
        mails_list.pop(0)
        for mail in mails_list:
            big_df = big_df._append(mail, ignore_index=True)

        big_df.to_csv(f'respostas_retornadas({datetime.now():%d.%m.%y-%I %p}).csv', sep=';', encoding='latin-1')


fetch_emails()
