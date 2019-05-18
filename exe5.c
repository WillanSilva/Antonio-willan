#include<stdio.h>
struct ponto{
    int x;
    int y;
    int z;
    };
void soma(struct ponto *p){
    p->z=p->z+10;
    }
void main(void){
    struct ponto v1;
    struct ponto v2;
    struct ponto v3;
    v1.x=1;v1.y=0;v1.z=5;
    v2.x=3;v2.y=3;v2.z=3;
    v3.x=0;v3.y=10;v3.z=0;
    printf("%d %d %d\n",v1.y,v2.y,v3.y);
    soma(&v1);soma(&v2);soma(&v3);
    printf("v2= %d %d %d\n",v2.x,v2.y,v2.z);
    }
    
    

