inicio = 0
fim = 100

def gerar_lista_sequencial(inicio, fim):
    lista = []
    while inicio < fim:
        inicio += 1
        lista.append(inicio)

    return lista


