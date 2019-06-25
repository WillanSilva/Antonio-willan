#include<stdio.h>
#include<string.h>
void escreva_string(FILE* f, char* str){
    f=fopen("arq2.txt","w");
    int tam=strlen(str);
    for (int i=0;i<tam;i++){
        fputc(str[i],f);
    }
    fclose(f);
}
void main(void){
    FILE* m;
    char stri[25];
    printf("Digite uma string: ");
    scanf("%s",stri);
    escreva_string(m,stri);
}


