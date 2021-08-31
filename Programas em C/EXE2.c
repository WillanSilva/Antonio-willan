#include<stdio.h>
struct caixa{
    int valor;
    struct caixa *prox;
};
void escrever(struct caixa *caixa){
    printf("%d->%d->%d->%d->%d\n",caixa->valor,caixa->prox->valor,caixa->prox->prox->valor,caixa->prox->prox->prox->valor,caixa->prox->prox->prox->prox->valor);
}
void main(void){
    struct caixa c5={5,NULL};
    struct caixa c4={7,&c5};
    struct caixa c3={9,&c4};
    struct caixa c2={3,&c3};
    struct caixa c1={1,&c2};
    escrever(&c1);
}
