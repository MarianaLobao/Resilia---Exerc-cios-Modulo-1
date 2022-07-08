def previsaorodagem (litros , kmmediaporlitros) :
    return (litros * kmmediaporlitros) 
    


litros = float(input("Digite quantidade de litros que seu carro possui: "))
kmmediaporlitros = float(input("Digite a média por litro que o seu carro faz: "))

print("A estimativa de km por litros é: " , previsaorodagem(litros , kmmediaporlitros) , "km." )

