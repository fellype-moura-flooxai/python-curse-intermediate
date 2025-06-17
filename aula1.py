""" 
introdução as funções (def) em python
funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
por padrão, funçÕes pyhton retornam none (nada)
"""

# def print(a, b, c):
#     print('várias1')
#     print('várias2')
#     print('várias3')
#     print('várias4')

# def imprimir(a, b, c):
#     print(a, b, c)
    

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='sem nome'):
    print(f'ola, {nome}!')


saudacao('fellype moura')
saudacao('maria')
saudacao('junior')

