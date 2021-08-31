#include <stdio.h>
struct notas{
    char nome[265];
    float nota1;
    float nota2;
    float media;
};
void pree(struct notas *j){
    printf("\nnome:");
    scanf("%s",j->nome);
    printf("\nDigite nota1: ");
    scanf("%f",&j->nota1);
    printf("Digite a nota2: ");
    scanf("%f",&j->nota2);
    j->media=(j->nota1+j->nota2)/2;
}
void impr(struct notas *k){
    printf("\nnome:%s\n",k->nome);
    printf("nota1:%5.2f\n",k->nota1);
    printf("nota2:%5.2f\n",k->nota2);
    printf("media:%5.2f\n",k->media);
}
void main(void){
    struct notas s;
    pree(&s);
    struct notas t;
    pree(&t);
    struct notas h;
    pree(&h);
    impr(&s);impr(&t);impr(&h);
}
