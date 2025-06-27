import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrirAdd commentMore actions
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\Fellype pc\\Documents\\python-curse-intermediate\\gerado.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('primeira linha\n')
    arquivo.write('escrevendo na segunda linha\n')
    arquivo.writelines(
        ('Na terceira linha\n', 'Na quarta linha\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('.' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

#os.remove(caminho_arquivo)
#os.rename(caminho_arquivo, 'arquivo_renomeado.txt')