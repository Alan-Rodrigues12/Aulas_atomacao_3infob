#usando as funções
import aula4.funcao as funcao

funcao.imprimir('Digite o número 1')
n1 = funcao.ler()
funcao.pulaLinha()
funcao.pulaLinha()

funcao.imprimir('Digite o número 2')
n2 = funcao.ler()

resposta = funcao.somar(n1, n2)
funcao.imprimir(f'O resultado é {resposta}')