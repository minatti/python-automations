import random
import unicodedata


qtd = 8
qtd_numero = 4
seq = 0
seq_end = 100
dominio = 'gmail'
senha = '1234@'

texto = '''Hoje é dia de grandes sorrisos, de fazer um pequeno balanço do que passou, de inspirar sonhos e desejos para o futuro, e principalmente de receber carinho e homenagens muito merecidas. Os meus votos são enviados à distância, mas nem por isso são menos sinceros ou sentidos. Feliz aniversário!

E você sabe como é especial para mim, muito especial, e de como eu gostaria de estar hoje do seu lado, de lhe dar este abraço e este beijo que há muito vivem querendo fugir de mim até você.

Mas a vida é mesmo assim, e nem sempre o que queremos se torna realidade. Mas espero que seus desejos se realizem, que a você a vida faça a vontade, pois pessoas especiais como você, merecem o que de melhor existe.

Sorria muito hoje, pois seu sorriso aquece corações como mais nada neste mundo consegue. E seja muito feliz, não só hoje, mas sempre e para sempre!'''

def removendoAcentos(texto):
    texto_normalize = unicodedata.normalize("NFD", texto)
    texto_normalize = texto_normalize.encode("ascii", "ignore")
    formatado = texto_normalize.decode("utf-8")
    return formatado


def lista_txt(texto):
    texto = removendoAcentos(texto)
    lista = list(texto.split(" "))
    return lista

def embaralhar():
    lista = lista_txt(texto)
    random.shuffle(lista)
    return lista

def junta_texto():
    lista = embaralhar()
    texto = ''.join(lista)
    return texto

def normaliza_texto():
        string = junta_texto()
        texto = string.lower()
        return texto


def gerar_lista_sequencial(seq, seq_end):
    lista = []
    while seq < seq_end:
        seq += 1
        lista.append(seq)

    return lista

def gerador_numeros_aleatorios():
    lista_numeros = gerar_lista_sequencial(seq, seq_end)
    random.shuffle(lista_numeros)
    return lista_numeros[0:2]

def juntar_numeros_aleatorios():
    lista = gerador_numeros_aleatorios()
    numeros = ''.join(map(str, lista))
    return numeros
#print(juntar_numeros_aleatorios())

def tamanho_texto(qtd):
     texto = normaliza_texto()
     tm_total = len(texto)
     tm_subtraido = (tm_total - qtd)
     tm_texto =  (tm_total - tm_subtraido)
     return tm_texto

def nome_email(dominio): 

    if dominio == 'gmail':
        email = '@' + dominio + '.com'
    else:
        email = None
        if dominio == 'hotmail':
            email = '@' + dominio + '.com'
        else:
            email = None

    return email   
print(nome_email(dominio))


def gerar_usuario(qtd, dominio):
    lista = gerar_lista_sequencial(seq, seq_end)
    texto = normaliza_texto()
    numero_aleatorio = juntar_numeros_aleatorios()
    posicao_inicial = lista[0]
    posicao_final = tamanho_texto(qtd)
    pos_ini = int(posicao_inicial)
    pos_fim = int(posicao_final)
    nome = texto[pos_ini:pos_fim]
    usuario = nome + numero_aleatorio

    return usuario

def gerar_senha(senha):
    return senha

print()
print("Usuario: ", gerar_usuario(qtd, dominio))
print("Senha: ", gerar_senha(senha))
print()

print("Iniciar próxima etapa")