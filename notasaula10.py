nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
me = float(input("Digite a nota do seu exercício: "))

ma = float(nota1 + nota2 * nota2 + nota3 * 3  + me ) /7
resultado = print("Sua nota referente ao cálculo:(nota1 + nota2 * nota2 + nota3 * 3  + me )/7) é: ",  ma)
    
if (ma > 9.0 ):
    print("Você tirou A. Está aprovado. ")
elif (ma >= 7.5 and  ma <= 9):
    print("Você tirou B. Está aprovado.")
elif (ma >= 6.0 and ma < 7.5):
    print("Você tirou C. Está aprovado. ")
elif (ma >= 4.0 and ma < 6.0):
    print("Você tirou D. Está reprovado.")
else:
    (ma < 4.0 )
    print("Você tirou E. Está reprovado.")
