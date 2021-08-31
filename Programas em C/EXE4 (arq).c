#include<stdio.h>
#include<string.h>
void main(void){
    FILE* m;
    m=fopen("arq01.txt","w");
    char veto[10][25];
    for (int i=0;i<10;i++){
        printf("Digite a string: ");
        scanf("%s",veto[i]);
    }
    for (int k=0;k<10;k++){
        int tam=strlen(veto[k]);
        for(int j=0;j<tam;j++){
            fputc(veto[k][j],m);
        }
    }
    fclose(m);
    
   }
