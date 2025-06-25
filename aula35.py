import importlib

import aula35_m

print(aula35_m.variavel)

for i in range(10):
    importlib.reload(aula35_m)
    print(i)

print('Fim')