#include<stdio.h>
struct caixa{
    int valor;
    struct caixa *prox;
};
int contem(struct caixa *l,int v){
    while(l->prox!=NULL){
        if (l->valor==v){
            break;
        }
        l=l->prox;
    }
    if (l->valor==v){
        return v;
    }
    else{
        return -1;
   }
}
void imprime(struct caixa *s){
    while(s->prox!=NULL){
        printf("%d->",s->valor);
        s=s->prox;
    }
    printf("%d\n",s->valor);
}
struct caixa* remover(struct caixa* lista, int valor){
        int n;
        n=contem(lista,valor);
        if (n!=-1){
            while (lista->prox!=NULL){
                if (lista->valor==valor){
                    lista->valor=lista->prox->valor;
                    lista->prox=lista->prox->prox;
                    break;
                }
                else if(lista->prox->valor==valor){
                     if(lista->prox->prox==NULL){
                           lista->prox=NULL;
                            break;
                    }
                    else{
                         lista->prox=lista->prox->prox;
                         break;
                    }
                }
                lista=lista->prox;       
                      
            }
            return  lista;
        }
       else{
            printf("valor %d não contem na lista!\n",valor);
            return lista;
       }
}
void main(void){
    struct caixa c[10];
     for(int i=0;i<10;i++){
        if (i==9){
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
    imprime(&c[0]);
    int n;
    printf("Digite o elemento a ser removido: ");
    scanf("%d",&n);
    struct caixa *s=&c[0];
    s=remover(&c[0],n);
    imprime(&c[0]);
}
    
    
            
            
            
