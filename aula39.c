#include <stdio.h>
#include <stdlib.h>

int main(){
    char *nome, *novo_nome;
    char letra;
    int i = 0, k = 0;
    letra = 'A';

    printf("Seu nome: ");

    while(1){
        scanf("%c", &letra);
        if(letra == '\n') break;
        if(i == 0){
            nome = (char *) malloc(sizeof(char));
        } else{
            nome = (char *) realloc(nome, sizeof(char));
        }
        nome[i] = letra;
        i++;
    }

    nome = (char *) realloc(nome, sizeof(char));

    nome[i] = '\0';
    i = 0;
    
    while(nome[i] != '\0'){
        if(i == 0){
            novo_nome = (char *) malloc(3 * sizeof(char));
            novo_nome[k] = '*';
            k++;
        } else{
            novo_nome = (char *) realloc(novo_nome, 2 * sizeof(char));
        }
        novo_nome[k] = nome[i];
        k++;
        novo_nome[k] = '*';
        k++;
        i++;
    }

    printf("Seu nome é %s\n", novo_nome);
    
    free(novo_nome);
    free(nome);

    return 0;
}
