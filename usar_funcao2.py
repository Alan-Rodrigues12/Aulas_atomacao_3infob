#usando as funções
import aula4.funcao as imprimir
import aula4.funcao as ler
import aula4.funcao as pulaLinha
import aula4.funcao as somar

imprimir('Digite o número 1')
n1 = ler()
pulaLinha()
pulaLinha()

imprimir('Digite o número 2')
n2 = ler()

resposta = somar(n1, n2)
imprimir(f'O resultado é {resposta}')