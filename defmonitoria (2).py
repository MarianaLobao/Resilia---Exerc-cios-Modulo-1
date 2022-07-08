#29-06 ----------------------------------------------------------------------------------------------------------




'''
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

def printLista():
    lista = []

    for i in range(5):
        lista.append(input('Digite o valor da posição ' + str(i) + ' : '))

    print(lista)


def printLista2(lista):
    print(lista)


# XASOAJDO = []

# for i in range(5):
#     XASOAJDO.append(input('Digite o valor da posição ' + str(i) + ' : '))

# printLista2(XASOAJDO)


'''
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

def media(lista):
    soma_notas = 0
    for i in range(len(lista)):
        soma_notas = soma_notas + lista[i]

    # Outra forma de fazer o for acima
    # for posicao, valor in enumerate(lista):
    #     soma_notas += valor
    print(lista)
    print(soma_notas/len(lista))


def mediaRetorno(lista):
    soma_notas = 0
    for i in range(len(lista)):
        soma_notas = soma_notas + lista[i]

    # Outra forma de fazer o for acima
    # for posicao, valor in enumerate(lista):
    #     soma_notas += valor
    
    return lista, soma_notas/len(lista)



# notas = []

# for i in range(4):
#     notas.append(int(input('Digite o valor da nota ' + str(i+1) + ' : ')))


# notaslidas, media =  mediaRetorno(notas)

# print(notaslidas)
# print(media)


'''
    Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

def printListaInversa(lista):
    lista.reverse()
    print(lista)


def ordernaImprime(lista):
    lista.sort(reverse=True)
    print(lista)


numeros = []

for i in range(5):
    numeros.append(float(input('Digite o numero ' + str(i+1) + ' : ')))


ordernaImprime(numeros)