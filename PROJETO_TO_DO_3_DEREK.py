quantidadedecandidatos = int(input('Quantos candidatos você gostaria de cadastras? '))
contador = 0
lista_de_candidatos = []

def pegarNota(palavra = ''):
    notae = int(input(f'Digite a nota{palavra}para Entrevista: '))
    notatt = int(input(f'Digite a nota{palavra}para Teste Teórico: '))
    notatp = int(input(f'Digite a nota{palavra}para Teste Prático: '))
    notass = int(input(f'Digite a nota{palavra}para Soft Skills: '))
    return [notae , notatt , notatp , notass]


while contador < quantidadedecandidatos:
    notas = pegarNota()
    lista_de_candidatos.append(notas)
    contador = contador + 1

lista_requisitos = pegarNota(palavra= ' de requisito ')

def validarNota(nota, nota_corte):
    if nota[0] < nota_corte[0]:
        return False

    elif nota[1] < nota_corte[1]:
        return False

    elif nota[2] < nota_corte[2]:
        return False


    elif nota[3] < nota_corte[3]:
        return False

    return True

def formatarNota(notas, posicao):
    a = notas[0]
    b = notas[1]
    c = notas[2]
    d = notas[3]

    return f'Candidato {posicao}: e{a}_t{b}_p{c}_s{d}'


def candidatos_validados(candidatos, nota_corte):

    for posicao, candidado in enumerate(candidatos):
        if validarNota(candidado, nota_corte):
            print(formatarNota(candidado, posicao))

candidatos_validados(lista_de_candidatos, lista_requisitos)