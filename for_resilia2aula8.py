numero = int(input("Fatorial de: ") )

fatorial = 1

for i in range (numero , 0 , -1) :
    
    fatorial =  fatorial *i

print(" {}! = {} " .format (numero , fatorial))