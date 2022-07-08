data_analytics = dict()
data_analytics ['variável'] = 'Definir um ou mais valores.'
data_analytics ['print'] = 'Exibir mensagens na tela.'
data_analytics ['input'] = 'Guardar a entrada de uma nova informação.'

pesquisa = input('Qual significado você está procurando? ')

if pesquisa in data_analytics:
    print('A palavra que pesquisou é: {} e o significado é: {}'.format(pesquisa , data_analytics[pesquisa]))
