import copy


def troia(familias, p1, p2):
    k = 0
    pessoas = []
    dicionario = {}
    for indice, familia in enumerate(familias):
        if p1 in familia["pessoas"]:
            if p2 not in familia["pessoas"]:
                familias[indice]["pessoas"].append(p2)
            k = 1
            break
        
    if k == 0:
        pessoas.append(p1)
        pessoas.append(p2)
        
        dicionario["pessoas"] = pessoas.copy()
        familias.append(copy.deepcopy(dicionario))
        
    return familias
            
        
    
    


string = input()
num_pessoas = int(string[0:string.find(" ")])
qtd_linhas = int(string[string.find(" ") + 1:])

familias = []
dicionario = {}
pessoas = []

for i in range(qtd_linhas):
    string = input()
    pessoa1 = int(string[0:string.find(" ")])
    pessoa2 = int(string[string.find(" ") + 1:])
    if i == 0:
        pessoas.append(pessoa1)
        pessoas.append(pessoa2)
        
        dicionario["pessoas"] = pessoas.copy()
        familias.append(copy.deepcopy(dicionario))
        
        dicionario.clear()
        pessoas.clear()
    else:
        familias = troia(familias, pessoa1, pessoa2)
        
print(*familias, sep = "\n")
print(len(familias))