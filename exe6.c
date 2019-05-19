#include<stdio.h>
struct atleta{
        char nome[256];
        int velocidade;
        int reflexo;
        int concentracao;
};
void propr(struct atleta *p){
        printf("\nDigite o nome:");
        scanf("%s",p->nome);
        printf("\nDigite a velocidade: ");
        scanf("%d",&p->velocidade);
        printf("Digite o reflexo: ");
        scanf("%d",&p->reflexo);
        printf("Digite a concentração: ");
        scanf("%d",&p->concentracao);
}
void impr(struct atleta *s){
        printf("\nnome:%s",s->nome);
        printf("velocidade: %d\n",s->velocidade);
        printf("reflexo: %d\n",s->reflexo);
        printf("concentração: %d\n",s->concentracao);
}
void main(void){
        struct atleta u;
        propr(&u);
        struct atleta d;
        propr(&d);
        struct atleta e;
        propr(&e);
        impr(&u);impr(&d);impr(&e);
}
