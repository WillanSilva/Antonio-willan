#include<stdio.h>
#include<string.h>

struct pessoa{
    int idade;
    int nome[64];
    int peso;
};
void escrever(struct pessoa *p){
    printf("Digite a idade: ");
    scanf("%d",&p->idade);
    printf("Digite o nome: ");
    scanf("%ls",p->nome);
    printf("Digite o peso: ");
    scanf("%d",&p->peso);
    printf("\n");
    }
void escreve(FILE*f,struct pessoa* s){
        fwrite(s,sizeof(struct pessoa),1,f);
   
}
void ler(FILE*s,struct pessoa *k){
    fread(k,sizeof(struct pessoa),1,s);
    printf("idade: %d\n",k->idade);
    printf("nome: %ls\n",k->nome); 
    printf("peso: %d\n",k->peso);
    printf("\n");  
}
void main(void){
    FILE *m;
    m=fopen("arquivo.bin","wb");
    int n=10;
    struct pessoa pessoas[n];
    for (int i=0;i<n;i++){
        escrever(&pessoas[i]);
        escreve(m,&pessoas[i]);
    }
    fclose(m);
    FILE *s;
    s=fopen("arquivo.bin","rb");
    struct pessoa k[n];
    for (int j=0;j<n;j++){
        ler(m,&k[n]);
    }
    fclose(s);   
}   
    

