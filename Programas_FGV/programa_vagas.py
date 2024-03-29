import pandas as pd
from datetime import date, datetime

###########################################################################################
def vagas_totais(vagas): #1 nas opções
    cont=0
    for i in range(len(ct_conteudo)):
        for j in range(len(ct_conteudo[i])):
            cont+=int(vagas[i][j])
    print()
    print("vagas totais de todos os CT e todos os meses são: {} Vagas".format(cont)) 
###########################################################################################
def vagas_mes(vagas,ct_conteudo):
    mes=input("Digite o mes exe (02): ")#2 nas opções
    cont=0
    for i in range(len(vagas)):
        for j in range(len(vagas[i])):
            if (ct_conteudo[i][j][9:11]==mes):
                cont+=int(vagas[i][j])
    print()
    print("numero total de vagas no mês:",meses[int(mes)-1])
    print("é de : ",cont)
    return cont
###########################################################################################
def vaga_estado_mes(estado,vagas,ct_conteudo,meses):#3 nas opções
    mes=input("Digite o mes exe (06)->junho: ")
    mes2=input("Digite o segundo mes exe (07)->julho: ")
    cont=cont2=0
    ufs = ['AM','RR','AP','PA','TO','RO','AC','MA','PI','CE','RN','PE','PB','SE','AL','BA','MT','MS','GO','DF','RJ','SP','ES','MG','PR','RS','SC']
    ct_estado=[]
    ct_estado2=[]
    total=total2=0
    for k in range(len(ufs)):
        for i in range(len(vagas)):
            for j in range(len(vagas[i])):
                if (ct_conteudo[i][j][9:11]==mes and ufs[k]==estado[i]):
                    cont+=int(vagas[i][j])
                elif(ct_conteudo[i][j][9:11]==mes2 and ufs[k]==estado[i]):
                  cont2+=int(vagas[i][j])
        dicio={"Estado":ufs[k],"Vagas": cont}
        dicio2={"Estado":ufs[k],"Vagas": cont2}
        ct_estado.append(dicio)
        ct_estado2.append(dicio2)
        total+=cont
        total2+=cont2
        cont=cont2=0
    dicio={"Estado":"Total","Vagas": total}
    dicio2={"Estado":"Total","Vagas": total2}
    ct_estado.append(dicio)
    ct_estado2.append(dicio2)
    de=pd.DataFrame(ct_estado)
    df=pd.DataFrame(ct_estado2)
    try:
        mes=int(mes)
        mes=meses[mes-1]
        mes2=int(mes2)
        mes2=meses[mes2-1]
        arquivo=pd.ExcelWriter("Resultado_"+data+"_"+mes+" e "+mes2+".xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Resultado "+mes)
        df.to_excel(arquivo,sheet_name="Resultado "+mes2)
        arquivo.save()
        print()
        print("Arquivo salvo com sucesso!")
        print("Verifique o arquivo no diretório do programa!")
        print()
    except:
        print("\nErro em colocar os dados do arquivo")
        print("\nVerifique se o arquivo está aberto\n")
###########################################################################################  
def criando_arquivo(ct,estado,vagas,ct_conteudo):#4 nas opções
    resultado=[]
    for  i in range(len(ct)):
        for j in range(len(vagas[i])):
            dicio={'CT':ct[i],'CT_CONTEUDO':ct_conteudo[i][j][9:16],'vagas': vagas[i][j],'Estado':estado[i]}
            resultado.append(dicio)
    de=pd.DataFrame(resultado)         
    try:
        arquivo=pd.ExcelWriter("Resultado_programa.xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name='TODOS OS CTs')
        arquivo.save()
    except:
        print("\nErro em colocar os dados no arquivo do arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    return ()
###########################################################################################
def para_vagas_totais_no_mes1(ct,estado,vagas,ct_conteudo,meses):#5 nas opções
    mes=input("Digite o mes exe 06->junho: ")
    cont=0
    vagas_por_ct=[]
    for i in range(len(vagas)):
        for j in range(len(vagas[i])):
            if (ct_conteudo[i][j][9:11]==mes):
                cont+=int(vagas[i][j])
        vagas_por_ct.append(cont)
        cont=0
    exel=[]
    
    for i in range(len(vagas_por_ct)):
        ct[i]=ct[i].replace('\n','')
        ct[i]=ct[i].replace('CT: ','')
        dicio={'CT':ct[i],'Vagas':vagas_por_ct[i]}
        exel.append(dicio)
        cont+=vagas_por_ct[i]
    dicio={"CT":"TOTAL","Vagas":cont}
    exel.append(dicio)
    de=pd.DataFrame(exel)
    try:
        mes=int(mes)
        mes=meses[mes-1]
        arquivo=pd.ExcelWriter("Resultado_porCT_"+mes+".xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Vagas em "+mes)
        arquivo.save()
        print()
        print("Arquivo salvo com sucesso!")
        print("Verifique o arquivo no diretório do programa!")
        print()
    except:
        print("\nErro em colocar os dados do arquivo")
        print("\nVerifique se o arquivo está aberto\n")
###########################################################################################
def por_dia(ct,vagas,ct_conteudo):#6
  while True:
    try:
      data=input("Digite a data inicial EXE dd/mm/aa: ")
      data = datetime.strptime(data, '%d/%m/%Y').date()
      break
    except:
      print("Digite novamente a data inicial!!")
  while True:
    try:
      data2=input("Digite a data limite exe dd/mm/aa: ")
      data2 =datetime.strptime(data2, '%d/%m/%Y').date()
      break
    except:
      print("Digite novamente a data limite !!")
  print("\nGostaria de visualisar o resultado por: ")
  print("1- Por CT")
  print("2- por todos os CTs")
  print("3- Por CT e por hora ")
  print("4- por todos os CTs e por hora")
  while True:
    try:
      veri=int(input("Digite o numero: "))
      if(veri==4 or veri==3):
        hora=int(input("Digite a hora: "))
      break
    except:
      print("Digite novamente  !!!")
  cont=0
  if (veri==1 or veri==3):
    nome_ct=input("Digite o nome do CT: ")
    tamanho=len(nome_ct)
  achei=False
  for i in range(len(ct_conteudo)):
    if(veri==2 or veri==4):
      print(ct[i])
      print()
    elif(veri==1 or veri==3):
      if(nome_ct.upper()==ct[i][:tamanho].upper()):
        print()
        print(ct[i])
        achei=True
        print()
      else:
        achei=False
    for j in range(len(ct_conteudo[i])):
        aux=ct_conteudo[i][j][6:16]
        aux=datetime.strptime(aux, '%d/%m/%Y').date()
        if ((aux>=data and aux<=data2) and (veri==2 or veri==4)):
          if(veri==4 and hora==int(ct_conteudo[i][j][25:27])):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
          elif(veri==2):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
          achei=False
        elif ((aux>=data and aux<=data2) and achei):
          if(veri==3 and hora==int(ct_conteudo[i][j][25:27])):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
            achei=True
          elif(veri==1):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
            achei=True
    if((veri==1 or veri==3) and achei):
      print("Total: ",cont)
      print("\n" + "-"*70)
      cont=0
    elif(veri==2 or veri==4):
      print()
      print('Vagas totais: ',cont)
      cont=0
      print("\n" + "-"*70)
#########################################################################################
def para_vagas_totais_no_mes(ct,estado,vagas,ct_conteudo,meses):#7 nas opções
    mes=input("Digite o mes exe (06)->junho: ")
    mes2=input("Digite o segundo mes exe (07)->julho: ")
    cont=cont2=0
    ufs = ['AM','RR','AP','PA','TO','RO','AC','MA','PI','CE','RN','PE','PB','SE','AL','BA','MT','MS','GO','DF','RJ','SP','ES','MG','PR','RS','SC']
    ct_estado=[]
    ct_estado2=[]
    total=total2=0
    for k in range(len(ufs)):
        for i in range(len(vagas)):
            for j in range(len(vagas[i])):
                if (ct_conteudo[i][j][9:11]==mes and ufs[k]==estado[i]):
                    cont+=int(vagas[i][j])
                elif(ct_conteudo[i][j][9:11]==mes2 and ufs[k]==estado[i]):
                  cont2+=int(vagas[i][j])
        dicio={"Estado":ufs[k],"Vagas": cont}
        dicio2={"Estado":ufs[k],"Vagas": cont2}
        ct_estado.append(dicio)
        ct_estado2.append(dicio2)
        total+=cont
        total2+=cont2
        cont=cont2=0
    dicio={"Estado":"Total","Vagas": total}
    dicio2={"Estado":"Total","Vagas": total2}
    ct_estado.append(dicio)
    ct_estado2.append(dicio2)
    de=pd.DataFrame(ct_estado)
    df=pd.DataFrame(ct_estado2)
    try:
        mes=int(mes)
        mes=meses[mes-1]
        mes2=int(mes2)
        mes2=meses[mes2-1]
        arquivo=pd.ExcelWriter("Resultado_dados\ "+data+mes+"e"+mes2+".xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Resultado "+mes)
        df.to_excel(arquivo,sheet_name="Resultado "+mes2)
        arquivo.save()
        print()
        print("Arquivo salvo com sucesso!")
        print("Verifique o arquivo no diretório do programa!")
        print()
    except:
        print("\nErro em colocar os dados do arquivo")
        print("\nVerifique se o arquivo está aberto\n")
###########################################################################################
#aqui começa a formatação de dados
data=date.today()
data=str(data)
data=data.split("-")
data=data[-1::-1]
data=data[0]+"-"+data[1]+"-"+data[2][-2::]
passou=True
try:
  arq=open("Dados\dado"+data+".txt",'r+')
except:
  passou=False
  print(data)
  print("\nVerifique se o arquivo está com a data de hoje!!!\n")
  print("\nVefique se o arquivo está no diretório dos Dados!!!\n")
if (passou):
  dados=arq.readlines()
  ct_conteudo=[] #contem todas as vagas dos cts. cts são listas dentro dessa lista.
  vagas=[] #contem todas as vagas referentes aos cts. a estrutura e analogada ao ct_conteudo
  tamanho=len(dados)-1
  aux_vagas=[]
  estado=[]
  ct=[]
  linhas=[]
  meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
  for i in range(len(dados)):
      if(dados[i][:3]=='CT:'):#pega a linha que contém as 3 letras CT:
          dados[i]=dados[i].replace("CT: ","")
          dados[i]=dados[i].replace("\n","")
          ct.append(dados[i])
          numero=len(dados[i])
          estado.append(dados[i][numero-2:numero])#pega o UF e adiciona na lista estado
      elif(dados[i][:3]=="Dat"):#pega a linha que contém 3 letras Dat 
          linhas.append(dados[i].replace("\n",''))#adiciono a linha em uma lista sem o /n
          numero=len(dados[i])
          aux_vagas.append(dados[i][numero-3:numero-1])#adiciono a qtd de vagas nessa linha em uma lista auxiliar
      if((dados[i]=='\n' and i!=1) or tamanho==i):#final do ct o /n se refere que a leitura dos dados daquele ct acabou
          ct_conteudo.append(linhas)#adiciono a lista linhas, assim cada elemento de ct_conteudo corresponde ao ct e o conteudo desse elemento corresponde as linhas das datas 
          linhas=[]#coloco como vazio pois a linhas é somente uma auxilar para pegar as linhas e colocalas no ct_conteudo 
          vagas.append(aux_vagas)#adiciono aux_vagas em  vagas para cada elemento de vagas corresponder ao ct, mesma logica do ct_conteudo
          aux_vagas=[]#como é auxiliar é vazio tmb só para pegar o numero das vagas
  print(vagas[-1])#só para verificar se esta pegando o ultimo elemento do arquivo
  #opções 
  while  True:
      print("Digite 1- para VAGAS TOTAIS")
      print("Digite 2- para VAGAS TOTAIS NO MES")
      print("Digite 3- para VAGAS TOTAIS NO MÊS E NO REFERIDO ESTADO (EXCEL)")
      print("Digite 4-para criar arquivo Excel(vivian)")
      print("Digite 5- para VAGAS TOTAIS NO MÊS E NO REFERIDO CT (EXCEL)")
      print("Digite 6- por data")
      print("Digite 7- para resultado na pasta reultado_dados")
      entrada=int(input("Digite o numero: "))
      if (entrada==1):
          vagas_totais(vagas)
      elif(entrada==2):
          vagas_mes(vagas,ct_conteudo)
      elif(entrada==3):
          vaga_estado_mes(estado,vagas,ct_conteudo,meses)
      elif(entrada==4):
          criando_arquivo(ct,estado,vagas,ct_conteudo)
      elif(entrada==5):
          para_vagas_totais_no_mes1(ct,estado,vagas,ct_conteudo,meses)
      elif (entrada==6):
        por_dia(ct,vagas,ct_conteudo)
      elif(entrada==7):
        para_vagas_totais_no_mes(ct,estado,vagas,ct_conteudo,meses)
      print()
      ence=int(input("Encerrar programa? 1 - Sim, 2 - Não: "))
      if (ence==1):
          break
