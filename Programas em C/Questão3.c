#include<stdio.h>
int main(void){
    char alunos[50];
    float soma=0,media=0,x;
    int k,i,quant=0;
    for(i=0;i<50;i++){
        printf("Digite as notas: ");
        scanf("%f",&x);
        alunos[i]=x;
        soma=x+soma;
        }
media=soma/50;
//printf("%5.2f\n",media);
for (k=0;k<50;k++){
    if (alunos[k]>=media){
        quant=quant+1;
        }
    }
printf("a media das notas:%5.2f\na quantidade é: %d\n",media,quant);   
return (0);
}
