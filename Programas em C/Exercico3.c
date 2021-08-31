//Um aluno de LP1 está indo aos Estados Unidos e quer comprar um celular novo.
//Ele não quer gastar mais do que 1000 reais. Um dólar está custando 3.17 reais.
//Faça um programa que leia o preço de um celular em dólares e, caso seja um bom negócio, escreva BOM NEGÓCIO
#include <stdio.h>
    int main(void){
    int a;
    printf("Digite o preço do celular (US$): ");
    scanf("%d",& a);
    a=a*3.17;
    if (a>1000){
        printf("---> mal negocio!\n");
        }
    else{
        printf("-----> Bom negocio!\n");
        }
    
return 0;
}
