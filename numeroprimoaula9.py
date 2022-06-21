numero_inteiro = int(input("Digite um número inteiro: "))

for a in range (1 , numero_inteiro +1 ) :
    if numero_inteiro % a == 0:
        print(" Número não é primo" , numero_inteiro , )