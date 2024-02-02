import os
import json

def print_lista(tarefas):
    if len(tarefas) > 0:
        print()
        print("=-" * 40)
        print("MINHAS TAREFAS:\n")
        for indice, tarefa in enumerate(tarefas):
            print(f"Tarefa {indice + 1}: {tarefa.capitalize()}")
        print()
        print("=-" * 40)
        print()
        
        
def refaz_lista(tarefas, arq):
    total = []
    total = json.load(arq)
    for elemento in total:
        if elemento not in tarefas:
            tarefas.append(elemento)
            return


def nothing_to_do(comando):
    print()
    print(f"Nada para '{comando.upper()}'")
    print()   
    
    
arquivo = open("tarefas.json", "w+")

lista = []
lista_total = []
k = 0

while True:
    print("Comandos: listar, desfazer, refazer")
    
    try:
        comando = str(input("Digite uma tarefa ou um comando: ")).strip().lower()
    except KeyboardInterrupt:
        arquivo.close()
        print("\nEncerrando programa")
        break
    
    if comando == "listar":
        if len(lista) > 0:
            print_lista(lista)
        else:
            nothing_to_do(comando)
            
    elif comando == "desfazer":
        if len(lista) > 0:
            lista.pop()
            print_lista(lista)
        else:
            nothing_to_do(comando)
            
    elif comando == "refazer":
        if len(lista) < k:
            arquivo = open("tarefas.json", "r+")
            refaz_lista(lista, arquivo)
            arquivo.close()
            print_lista(lista)
        else:
            nothing_to_do(comando)
            
    elif comando == "clear":
        os.system(comando)
        
    else:
        arquivo = open("tarefas.json", "w+")
        lista.append(comando)
        lista_total.append(comando)
        json.dump(lista_total, arquivo, indent=2)
        arquivo.close()
        k += 1
        print_lista(lista)
    