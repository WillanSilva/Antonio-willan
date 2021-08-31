//Faça um programa que leia números continuamente até que seja digitado 0. Ao final, o programa deve exibir a soma de todos os números lidos.
#include <stdio.h>
    int main(void){
    int c,soma=0;
    while (1){
    printf("Digite os numeros: ");
    scanf("%d",& c);
    if (c==0){
        printf("----> A soma é: %d\n",soma); 
        break;
        }
    soma=c+soma;
    }
return 0;
}    
