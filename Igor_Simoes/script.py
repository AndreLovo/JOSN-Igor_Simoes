import json

def escrever_json (dados):
    with open ('meu_arquivo.json', 'w') as f:
         json.dump(dados, f)


meu_dict = {
    'nome': 'Andre Gustavo Silva Lovo',
    'idade': '44 anos' 
}

escrever_json(meu_dict)
