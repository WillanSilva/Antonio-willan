//Faça um programa que leia um número N e calcule o somatório:
#include <stdio.h>
    int main(void){
    int n,soma=0;
    printf("Digite o N: ");
    scanf("%d",& n);
    for(int i=1;i<=n;i++){
        soma+=i*i;
        }
    printf("---> O  somatorio É: %d\n",soma);
return 0;
}    
