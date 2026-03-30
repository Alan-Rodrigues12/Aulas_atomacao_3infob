SenhaVerify=False
usuarioVerify=False
Senha = "admin123"
usuario = "admin"
resposta1 = str(input("Digite o usúario:\n"))
while resposta1 != usuario:
    resposta1 = str(input("Este usuário não existe! tente novamente:\n"))
    
if resposta1 == usuario:
    usuarioVerify = True

if usuarioVerify==True:
    resposta2 = str(input("Digite a senha:\n"))
    while resposta2 != Senha:
        resposta2 = str(input("Senha incorreta! Tente novamente!:\n"))
    if resposta2 == Senha:
        SenhaVerify = True
    
if SenhaVerify and usuarioVerify == True:
    print("Acesso concedido!")