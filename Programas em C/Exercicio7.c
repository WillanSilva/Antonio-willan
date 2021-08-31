//O Campeonato Brasileiro está na reta final com 20 times na disputa.

//Uma vitória vale 3 pontos, um empate vale 1 ponto e uma derrota vale 0 pontos. Escreva um programa que, para cada time, leia o nome, número de vitórias, número de empates e número de derrotas.

//Ao final, o programa deve escrever o nome dos times com mais e menos pontos até o momento.
#include <stdio.h>
    int main(void){
    int vit[5],der[5],emp[5],soma[5],tim[5],maior;
    for (int i=1;i<=5;i++){
        printf("time %d:\n",i);
        tim[i]=i;
        for (int k=1;k<=1;k++){
            printf("Numero de vitórias: ");
            scanf("%d",& vit[i]);
            printf("Numero de empates: ");
            scanf("%d",& emp[i]);
            printf("Numero de derrotas: ");
            scanf("%d",& der[i]);
            soma[i]=(vit[i]*3)+(emp[i]*1)+(der[i]*0);
            }
    }
for(int l=1;l<=5;l++){
        printf("****************************\n");
        printf("time %d com %d pontos!\n",l,soma[l]);
        }
return 0;
}    
