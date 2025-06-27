import json

pessoa = {
  "nome": "Fellype edit",
  "sobrenome": "Moura",
  "enderecos": [
    {
      "rua": "R1",
      "numero": 32
    },
    {
      "rua": "R2",
      "numero": 55
    }
  ],
  "altura": 1.8,
  "numeros_preferidos": [
    2,
    4,
    6,
    8,
    10
  ],
  "dev": True,
  "nada": None,
}

with open('aula55.json', 'w') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        indent=2,
    )

with open('aula55.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])
