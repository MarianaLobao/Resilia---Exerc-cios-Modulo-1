nome = 'Jaqueline'
turno = input("Digite o turno: \n [M] Matutuno\n [V] Vesp\n [N] Noturno \n = ")

condicao = True

while condicao:
    turno = input("Digite o turno: \n [M] Matutuno\n [V] Vesp\n [N] Noturno \n = ")
    if turno == 'M':
        print('Bom dia ' +nome)
        condicao = False
    elif turno == 'V':
        print('Boa tarde '+nome)
        condicao = False
    elif turno == 'N':
        print('Boa noite '+nome)
        condicao = False
    else:
        print("Valor inválido, tente novamente")
