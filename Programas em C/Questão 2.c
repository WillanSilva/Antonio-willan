#include <stdio.h>
int main(void){
int a,b,i,cont;
printf("Digite o primeiro numero: ");
scanf("%d", & a);
printf("Digite o segundo numero: ");
scanf("%d",& b);
cont=a;
while(a>b){
    if (cont%2==0){
        printf("%d\n",cont);
    }
    cont=cont-1;
    a=a-1;
    }
cont=b;
while (b>=a){
    if (cont%2==0){
        printf("%d\n",cont);
        }
    cont=cont-1;
    b=b-1;
    }
return 0;
}
