#include<stdio.h>
#include<string.h>
void main(void){
    char str[25];
    printf("Digite a string: ");
    scanf("%s",str);
    int p=strlen(str);
    FILE*arq=fopen("/home/ime/Área de Trabalho/antarqu.txt","w");
    for(int i=0;i<p;i++){
        fputc(str[i],arq);
    }
    fclose(arq);
}
