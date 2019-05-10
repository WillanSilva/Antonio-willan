#include<stdio.h>
struct alunos{
    char nome[256];
    float nota1;
    float nota2;
    float media;
};
void muda(struct alunos *p){
    printf("Digite o nome do aluno: ");
    scanf("%s",p->nome);
    printf("Digite a nota1 do aluno: ");
    scanf("%f",&(p->nota1));
    printf("Digite a nota2 do aluno: ");
    scanf("%f",&(p->nota2));
    float media=((p->nota1)+(p->nota2))/2;
    p->media=media;
    }
void ver(struct alunos* s){
    printf("nome:%s\nnota1:%5.2f nota2: %5.2f\nmedia=%5.2f\n",s->nome,s->nota1,s->nota2,s->media);
} 
void main(void){
    struct alunos antonio;
    muda(&antonio);
    struct alunos lucas;
    muda(&lucas);
    ver(&antonio);
    ver(&lucas);
    //printf("%f %f", antonio.nota2,lucas.nota2);
    }
    
    
    

