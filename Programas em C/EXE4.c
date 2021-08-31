#include<stdio.h>
struct caixa {
    int valor;
    struct caixa * prox;
};
int contem(struct caixa *lista,int valor){
    while(lista->prox!=NULL){
        if (lista->valor==valor){
            break;
        }
        lista=lista->prox;
    }
    if (lista->valor==valor){
        return valor;
    }
    else{
        return 0;
    }
}
void main(void){
    struct caixa c[5];
    for(int i=0;i<5;i++){
        if (i==4){
            printf("Digite o valor da caixa: ");
            scanf("%d",&c[i].valor);
            c[i].prox=NULL;
        }
        else{
            printf("Digite o valor da caixa: ");
            scanf("%d",&c[i].valor);
            c[i].prox=(&c[i+1]);
        }
    }
    printf("Digite o numero a ser encontrado na lista:");
    int f,d;
    scanf("%d",&f);
    d=contem(&c[0],f);
    if (d==0){
        printf("elemento %d Não encontrado!\n",f);
    }
    else{
        printf("elemento %d encontrado!\n",d);
    }
}
