#Crie um script que usa a função quadrado criada no arquivo exercicio_f1.py. Esse script deve pedir para o usuário digitar um número, depois deve calcular o quadrado usando a função e depois imprimir o resultado.
import exercicio_f1 as function
function.imprimir('Digite o número')
n1 = function.ler()
function.pulaLinha()
function.pulaLinha()

resposta = function.quadrado(n1, n2)
function.imprimir(f'O resultado é {resposta}')