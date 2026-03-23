nota1=int(input("Digite sua primeira nota:\n"))

nota2=int(input("Digite sua segunda nota:\n"))

nota = ((nota1 + nota2)/2)

if (nota >=6):
    print("Aprovado.")
elif(nota < 6):
    media=float(input("informe a média:\n"))
    notafinal = (media + nota) / 2
    if (notafinal>=6):
        print("Aprovado.")
    else:
        print("Reprovado.")
