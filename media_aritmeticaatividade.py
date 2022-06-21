print("Calculadora Aritmética")

nome = input("Digite o seu nome:")
turma = input("Digite a sua turma:")

nota1 = float(input("Digite sua primeira nota:"))
nota2 =  float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))
nota4 = float(input("Digite sua quarta nota:"))

resultado_media = (nota1 + nota2 + nota3 + nota4) /4

print("Olá," , nome , "da turma" , turma , ". A sua média é:" , resultado_media)