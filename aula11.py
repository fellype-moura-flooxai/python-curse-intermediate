# exercicios
# crie funçoes que duplicam, tripicam e quadruplicam
# o número recebido como parametro

# def duplicar (numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4


def criarmulti(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criarmulti(2)
print(duplicar(7))

triplicar = criarmulti(3)
print(triplicar(3))

quadruplicar = criarmulti(4)
print (quadruplicar(10))