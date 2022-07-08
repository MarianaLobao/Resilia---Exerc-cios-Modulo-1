


nomes_lista = ['Mariana' , 'Diego' , 'Sthepanie' , 'Laura']
tupla_nomes = tuple(nomes_lista)
tupla2 = ['Theo', 'Fabrício' , 'Amora']


for i in tupla_nomes:
    print(f'Boa noite! Seja bem-vindo: {i}')

print(len(tupla_nomes))
print( 'Mariana' in tupla_nomes)
print(nomes_lista + tupla2 )
print(tupla2 *2)