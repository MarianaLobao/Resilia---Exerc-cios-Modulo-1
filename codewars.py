weight = float(input("Digite o seu peso: "))
height = float(input("Digite a sua altura: "))


def bmi (weight , height) :
    return ( weight / (height))
resultado = bmi(weight, height) 

if (resultado <= 18.5) :
    print("Abaixo do peso. ")
elif (resultado <= 25.0):
    print("Normal. ")
elif (resultado <= 30.0):
    print("Excesso de peso.  ")
else:
    print("Obeso. ")