def BatalhaNaval(matriz, linha, coluna, num_linhas, num_colunas):
    global acertos
    new_line = ''
    k = 0
    if matriz[linha][coluna] == '#':
        if linha == 0 and coluna == 0:
            if(matriz[linha][coluna + 1] == 'a' and matriz[linha + 1][coluna] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                    
                
        elif linha == 0 and coluna == num_colunas - 1:
            if(matriz[linha][coluna - 1] == 'a' and matriz[linha + 1][coluna] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                
        elif linha == num_linhas - 1 and coluna == num_colunas - 1:
            if(matriz[linha][coluna - 1] == 'a' and matriz[linha - 1][coluna] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
        
        elif linha == num_linhas - 1 and coluna == 0:
            if(matriz[linha][coluna + 1] == 'a' and matriz[linha - 1][coluna] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
        
        elif linha == 0:
            if(matriz[linha][coluna + 1] == 'a' and matriz[linha + 1][coluna] == 'a' and matriz[linha][coluna - 1] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                
        elif linha == num_linhas - 1:
            if(matriz[linha][coluna + 1] == 'a' and matriz[linha - 1][coluna] == 'a' and matriz[linha][coluna - 1] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                
        elif coluna == 0:
            if(matriz[linha + 1][coluna] == 'a' and matriz[linha - 1][coluna] == 'a' and matriz[linha][coluna + 1] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                
        elif coluna == num_colunas - 1:
            if(matriz[linha + 1][coluna] == 'a' and matriz[linha - 1][coluna] == 'a' and matriz[linha][coluna - 1] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
        
        else:
            if(matriz[linha + 1][coluna] == 'a' and matriz[linha - 1][coluna] == 'a' and matriz[linha][coluna - 1] == 'a' and matriz[linha][coluna + 1] == 'a'):
                acertos += 1
            else:
                for indice, letra in enumerate(matriz[linha]):
                    if indice != coluna:
                        new_line += matriz[linha][indice]
                    else:
                        new_line += 'a'
                matriz[linha] = new_line
                new_line = ''
                  
    return matriz
            
                
            
            

string = input()

num_linhas = int(string[0:string.find(" ")])
num_colunas = int(string[string.find(" ") + 1:])
acertos = 0

matriz = []

for i in range(num_linhas):
    string = input()
    matriz.append(string)
    
k = int(input())

for i in range(k):
    string = input()
    
    linha = int(string[0:string.find(" ")])
    coluna = int(string[string.find(" ") + 1:])
    
    matriz = BatalhaNaval(matriz, linha - 1, coluna - 1, num_linhas, num_colunas)

print(acertos)
    