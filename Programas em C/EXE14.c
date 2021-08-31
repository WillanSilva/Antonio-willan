#include<stdio.h>
struct preco{
    int sub;
    union {
        float reais;
        float dolares;
        float euros;        
        };
};
void exibe(struct preco *p){
    switch (p->sub){
    case 1:
        printf("R$: %5.2f\n",p->reais);
        break;
    case 2:
        printf("U$: %5.2f\n",p->dolares);
        break;
    case 3:
        printf("E$: %5.2f\n",  p->euros);
        break;
    default:
        printf("ERRO");
        break;
    }
}
void altera(struct preco *s){
        switch (s->sub){
                case 1:
                    printf("Digite 2 para dolares:\nDigite 3 para euros:\n");
                    scanf("%d",&s->sub);
                    switch (s->sub){
                        case 2:
                            s->dolares=s->reais*0.25;
                            break;
                        case 3:
                            s->euros=s->reais*0.22;
                             break;
                        default:
                            printf("ERRO");
                            break;
                    }
                    break;
                case 2:
                    printf("Digite 1 para reais:\nDigite 3 para euros:\n");
                    scanf("%d",&s->sub);
                    switch(s->sub){
                        case 1:
                            s->reais=s->dolares/0.25;
                            break;
                        case 3:
                            s->euros=s->dolares*0.89;
                            break;
                        default:
                            printf("ERRO");
                            break;
                    }
                    break;
                case 3:
                    printf("Digite 1 para reais:\nDigite 2 para dolares:\n");
                    scanf("%d",&s->sub);
                    switch(s->sub){
                        case 1:
                            s->reais=s->euros*4.53;
                            break;
                        case 2:
                            s->dolares=s->euros*0.89;
                            break;
                        default:
                            printf("ERRO");
                            break;
                    }
                    break;
                default:
                    printf("ERRO");
                    break;

        }
}
void main(void){
    struct preco p1;
    p1.sub=2;
    p1.euros=10;
    exibe(&p1);
    altera(&p1);
    exibe(&p1);
}
