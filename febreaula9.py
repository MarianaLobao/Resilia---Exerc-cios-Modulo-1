temperatura = ""
while(temperatura != 'sair'):
    temperatura = (input("digite sua temperatura: "))
    if float(temperatura) >= 38 and float(temperatura) < 39:
        print("Você está com febre. Tome um remédio! ")
    elif float(temperatura) >= 39:
        print("Você está com febre. Procure um médico!")
    else:
        print("Você não está com febre!")
