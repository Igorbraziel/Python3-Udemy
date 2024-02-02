import os

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
    arq.seek(0, 0)
    while True:
        linha = arq.readline()
        if linha == -1:
            break
        linha = linha[:len(linha) - 1]
        if linha not in tarefas:
            tarefas.append(linha)
            break


def nothing_to_do(comando):
    print()
    print(f"Nada para '{comando.upper()}'")
    print()   
    
    
arquivo = open("tarefas.txt", "w+")

lista = []
k = 0

while True:
    arquivo = open("tarefas.txt", "a+")
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
            refaz_lista(lista, arquivo)
            print_lista(lista)
        else:
            nothing_to_do(comando)
            
    elif comando == "clear":
        os.system(comando)
        
    else:
        lista.append(comando)
        arquivo.write(f"{comando}\n")
        arquivo.close()
        k += 1
        print_lista(lista)
    