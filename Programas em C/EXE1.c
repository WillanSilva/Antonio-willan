#include<stdio.h>
struct caixa{
    int valor;
    struct caixa *prox;
};
void main(void){
    struct caixa c5={5,NULL};
    struct caixa c4={7,&c5};
    struct caixa c3={9,&c4};
    struct caixa c2={3,&c3};
    struct caixa c1={1,&c2};
    printf("%d->%d->%d->%d->%d\n",c1.valor,c2.valor,c3.valor,c4.valor,c5.valor);
}
