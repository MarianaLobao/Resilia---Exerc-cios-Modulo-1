produtos = [ 'acr567' , '   ACS865' , 'AFnf45' , 'TfgA89']

texto = '   ACS865'

def tratamentotexto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return (texto)

texto = tratamentotexto

for i , produto in enumerate (produtos):
    produtos[i] = tratamentotexto(produtos)
    print (produtos)



