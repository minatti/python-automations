Automacoes com Python 

DOTENV (não exponha senhas de API, DB, e outras informações sensíveis no seu código)

0. Lib dotenv vem como default no python, pelo menos na versão que eu to utilizando 3.8.3
1. crie o arquivo em modo oculto ".env"
2. crie as CONSTANTES no arquivo ".env"
    Exemplo:
    
    MAIL_USER = 'meuemail@py.com'
    MAIL_PWD = '1234'

3. no script, no meu caso: "send_mail.py" 

Importacao: "from dotenv import load_dotenv"
Carregamento: "load_dotenv(verbose=True)"

4.  mail_user = os.getenv('MAIL_USER')
    mail_password = os.getenv('MAIL_PWD')

Abaixo site da documentação oficial para implentar a boa prática
https://pypi.org/project/python-dotenv/

Seguido da boa prática segue um exemplo básico para enviar e-mail,
aos poucos implementaremos outras versões...