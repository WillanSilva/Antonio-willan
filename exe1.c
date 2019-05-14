#include<stdio.h>
struct personagem{
    int forca;
    int energia;
    int experiencia;
    };
void main(void){
    struct personagem p1;
    p1.forca=10;
    p1.energia=50;
    p1.experiencia=30;
    struct personagem p2={18,20,25};
    printf("%d %d %d\n%d %d %d\n",p1.forca,p1.energia,p1.experiencia,p2.forca,p2.energia,p2.experiencia);
    }
    
