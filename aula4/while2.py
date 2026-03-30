continuar = True

while continuar:
    print("Digite o nome do aluno:\n")
    aluno = input()

    resp = int(input("Deseja continuar? 0 para Não, 1 para Sim\n"))
    if resp == 0:
        continuar = False