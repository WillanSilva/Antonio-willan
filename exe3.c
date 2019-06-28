#include<stdio.h>
struct caixa{
    int valor;
    struct caixa * prox;
};
void exibe(struct caixa *p){
    while (p->prox!=NULL){
        printf("%d->",p->valor);
        p=p->prox;
    }
    printf("%d",p->valor);
    printf("\n");
}         
void main(void){
    struct caixa c5={5,NULL};
    struct caixa c4={7,&c5};
    struct caixa c3={9,&c4};
    struct caixa c2={3,&c3};
    struct caixa c1={1,&c2};
    struct caixa* cabeca;
    exibe(&c1);
    cabeca=&c1;
    cabeca->prox->prox=&c4;
    exibe(&c1);
    cabeca=&c3;
    cabeca->prox=&c1;
    cabeca->prox->prox->prox=&c4;
    exibe(&c3);
    
}
        
