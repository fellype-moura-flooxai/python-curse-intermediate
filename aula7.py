# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult (*args):
    total = 1
    for numeros in args:
        total *= numeros
    print(total)

mult(1, 2, 3, 4, 5, 6)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(5))