import random
lista1=["cadeira","mesa","telefone","computador"]
lista2=["brinquedos","crianças","professor","escola"]
lista3=["estágio","torcida","times","bola","quadra"]
baseDados={"trabalho":lista1,"creche": lista2,"futebol":lista3}
temas=list(baseDados)
tema_aleatorio=temas[random.randint(0,len(baseDados)-1)]
palavra1=baseDados[tema_aleatorio][random.randint(0,len(baseDados[tema_aleatorio])-1)]
palavra2=baseDados[tema_aleatorio][random.randint(0,len(baseDados[tema_aleatorio])-1)]
palavra3=baseDados[tema_aleatorio][random.randint(0,len(baseDados[tema_aleatorio])-1)]
palavras_sortidas=[palavra1,palavra2,palavra3]
print(tema_aleatorio)
print(palavras_sortidas)
jogadores=["ana","barbara","carlos"]
roleta=["100","150","200","250","300","350","400","450","500","550","600","650","700","750"...
        ,"800","850","900","950","1000","1000","Passou a vez!","Passou a vez!","Perdeu Tudo!","Perdeu Tudo!"]
turno=0
rodada=0
while :
    roleta_aleatoria=random.randint(0,len(roleta)-1)



        
