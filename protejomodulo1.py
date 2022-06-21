petvet = int(input("""Seja Bem vindo(a). Para informações sobre emergência digite 1. Para informações sobre exames digite 2. Para informações sobre financeiro, digite 3. Para informações sobre consultas/especialidades digite 4. Ou informações de contato, digite 5: """))
petvet_emergencia = ""
condicao = True

while(petvet == 1 and condicao) :
    petvet_emergencia = input("""Digite 1 para: Sou cliente conveniado. 
Digite 2 para: Não sou cliente conveniado. 
Digite 3 para: Como cuidar do meu pet até o atendimento. 
Digite 4 para: Retornar ao início. E 5 para: Encerrar atendimento: """)

    if(petvet_emergencia == "1") :
        print("Entre em contato com o veterinário do convênio. Número: (21)9999-9999")
    elif (petvet_emergencia =="2") :
        print("Entre em contato com o veterinário. Número: (21) 88888-8888")
    elif (petvet_emergencia == "3" ) :
        print("""Engasgamento em cães:
        Se possível, abra a boca do animal e tente retirar manualmente o objeto responsável pelo engasgamento. Caso o cachorro ou gato se mostre agressivo e tente morder, ajude-o a se livrar do objeto dando alguns tapinhas nas costas dele, na altura das patas da frente.
        No caso de bichinhos menores, você também pode segurá-los pelas patas, deixando-os de cabeça para baixo e sacudindo-os com cuidado até que o objeto seja liberado.

        Queimaduras e primeiros socorros:
        Nos primeiros socorros em cães e gatos com queimaduras, lave a região atingida com água fria corrente por pelo menos 10 minutos. Isso ajuda a resfriar o local e a diminuir a dor.
        Não aplique pomadas nem tente seguir receitas caseiras, evitando vinagre, pasta de dente, entre outros. Apenas cubra a queimadura com um pano limpo e úmido, tomando cuidado para que não grude na ferida. Depois, leve o bichinho a uma clínica veterinária e aguarde as orientações do especialista.
        Fraturas internas e externas em cães e gatos
        Muito comuns em casos de atropelamento ou mesmo de quedas (no caso de cães de pequeno porte), as fraturas devem ser imobilizadas com a ajuda de esparadrapo e objetos retos, como um pedaço de papelão. Ao se aproximar do cão ou gato, tome cuidado, visto que a dor e o susto do acidente podem deixar o animal agressivo.

        No caso de primeiros socorros para cachorro e gato com fratura exposta, o melhor é cobrir a região com um pano limpo. Nunca tente colocar os ossos no lugar. Somente um veterinário terá condições de fazer isso de forma adequada.

        Intoxicação ou envenenamento de cães e gatos:
        Antes de tentar desintoxicar cachorro ou gato, procure identificar a causa, a quantidade e há quanto tempo a substância foi ingerida. Isso ajudará o veterinário a seguir o melhor protocolo durante o atendimento de emergência. Caso o pet tenha vomitado, também é possível recolher uma amostra do conteúdo.
        Se tiver carvão ativado em casa, siga as orientações do fabricante e ofereça o produto diluído ao seu amigo pela boca, usando uma seringa sem agulha. O carvão ativado ajuda a reduzir a absorção do agente tóxico pelo organismo.
        Leve o animalzinho a uma clínica veterinária e nunca tente provocar o vômito. Dependendo da substância, ela pode queimar o esôfago do peludo e agravar o quadro.

        Cortes em cães e gatos:
        Se possível, lave a região afetada com água corrente para diminuir o risco de infecções. Com a ajuda de um pano limpo, pressione a região do corte. Isso ajuda a controlar a hemorragia, evitando a perda de muito sangue até a chegada à clínica veterinária.""")
    
    elif(petvet_emergencia == "4"):
        print("Você será redirecionado ao início. ")
        petvet = int(input("""Seja Bem vindo(a). Para informações sobre emergência digite 1. Para informações sobre exames digite 2. Para informações sobre financeiro, digite 3. Para informações sobre consultas/especialidades digite 4. Ou informações de contato, digite 5: """))
        
    else:
        (petvet_emergencia == 5)
        print("Atendimento encerrado. ")
        condicao = False
        
