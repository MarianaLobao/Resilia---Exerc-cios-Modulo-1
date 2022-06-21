#Faça um programa com uma função chamada somaImposto. A função irá ler dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item do imposto antes do imposto. A fubção "altera" o valor de custo para incluir o imposto sobre vendas.


def somaImposto():
    custo = int(input("Digite o custo do produto: "))
    imposto = int(input("Digite o imposto sobre o produto (%): "))

    print(custo + custo * imposto/100)



somaImposto()