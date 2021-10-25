import json

def ler_json ():
    with open ('meu_arquivo.json', 'r') as f:
        #data = json.load(f) 
        return json.load(f)

data = ler_json()

# print(data['nome'])

# Adicionando um texto
text = "Eu gosto muito das videos aulas do %s" %(data['nome'])

print(text)