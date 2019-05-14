#include<stdio.h>
struct personagem{
    int forca;
    int energia;
    int experiencia;
    };
struct personagem preencheA(void){
    struct personagem s;
    printf("Digite a força: ");
    scanf("%d",&s.forca);
    printf("Digite a energia: ");
    scanf("%d",&s.energia);
    printf("Digite a experiencia: ");
    scanf("%d",&s.experiencia);
    return s;
    }
void main(void){
    struct personagem p1=preencheA();
    struct personagem p2=preencheA();
    printf("p1:%d %d %d\np2:%d %d %d\n",p1.forca,p1.energia,p1.experiencia,p2.forca,p2.energia,p2.experiencia);
    }
