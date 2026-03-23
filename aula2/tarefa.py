nota1=int(input("Digite sua primeira nota:\n"))


if (nota1 >=6):
    print("Aprovado.")
elif(nota1 < 6):
    media1=int(input("informe a média:\n"))
    notafinal1 = media1 + nota1/2
    if (notafinal1>=6):
        print("Aprovado.")
    else:
        print("Reprovado.")


nota2=int(input("Digite sua segunda nota:\n"))

if (nota2 >=6):
    print("Aprovado.")
elif(nota2 < 6):
    media2=int(input("informe a média:\n"))
    notafinal2 = media2 + nota2/2
    if (notafinal2>=6):
        print("Aprovado.")
    else:
        print("Reprovado.")
