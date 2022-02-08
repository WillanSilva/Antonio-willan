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
    num=int(input("Digite a quantidade de meses a colocar no exel: "))
    if (num==2):
        mes=input("Digite o mes exe (06)->junho: ")
        mes2=input("Digite o segundo mes exe (07)->julho: ")
        mes3=0
    elif(num==3):
        mes=input("Digite o mes exe (06)->junho: ")
        mes2=input("Digite o segundo mes exe (07)->julho: ")
        mes3=input("Digite o terceiro mes exe (08)->agosto: ")
    cont=cont2=cont3=0
    ufs = ['AM','RR','AP','PA','TO','RO','AC','MA','PI','CE','RN','PE','PB','SE','AL','BA','MT','MS','GO','DF','RJ','SP','ES','MG','PR','RS','SC']
    ct_estado=[]
    ct_estado2=[]
    ct_estado3=[]
    total=total2=total3=0
    for k in range(len(ufs)):
        for i in range(len(vagas)):
            for j in range(len(vagas[i])):
                if (ct_conteudo[i][j][9:11]==mes and ufs[k]==estado[i]):
                    cont+=int(vagas[i][j])
                elif(ct_conteudo[i][j][9:11]==mes2 and ufs[k]==estado[i]):
                  cont2+=int(vagas[i][j])
                elif (num==3 and ct_conteudo[i][j][9:11]==mes3 and ufs[k]==estado[i]):
                    cont3+=int(vagas[i][j])
        dicio={"Estado":ufs[k],"Vagas": cont}
        dicio2={"Estado":ufs[k],"Vagas": cont2}
        dicio3={"Estado":ufs[k],"Vagas": cont3}
        ct_estado.append(dicio)
        ct_estado2.append(dicio2)
        if(num==3):
            ct_estado3.append(dicio3)
            total3+=cont3
        total+=cont
        total2+=cont2
        cont=cont2=cont3=0
    dicio={"Estado":"Total","Vagas": total}
    dicio2={"Estado":"Total","Vagas": total2}
    dicio3={"Estado":"Total","Vagas": total3}
    ct_estado.append(dicio)
    ct_estado2.append(dicio2)
    if(num==3):
        ct_estado3.append(dicio3)
        dh=pd.DataFrame(ct_estado3)
    for i in ct_estado:
        print("ctestado",i)
    de=pd.DataFrame(ct_estado)
    df=pd.DataFrame(ct_estado2)
    mes=int(mes)
    mes=meses[mes-1]
    mes2=int(mes2)
    mes2=meses[mes2-1]
    mes3=int(mes3)
    mes3=meses[mes3-1]
    try:
        if num==3:
            arquivo=pd.ExcelWriter("Resultado_"+data_hoje+"_"+mes+" e "+mes2+" e "+mes3+".xlsx")
        else:
            arquivo=pd.ExcelWriter("Resultado_"+data_hoje+"_"+mes+" e "+mes2+".xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Resultado "+mes)
        df.to_excel(arquivo,sheet_name="Resultado "+mes2)
        if(num==3):
            dh.to_excel(arquivo,sheet_name="Resultado "+mes3)
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
def para_vagas_totais_no_mes_porct(ct,estado,vagas,ct_conteudo,meses):#5 nas opções
    mes=input("Digite o mes exe 06->junho: ")
    mes2=input("Digite o segundo mes exe (07)->julho: ")
    cont=0
    cont2=0
    vagas_por_ct=[]
    vagas_por_ct2=[]
    for i in range(len(vagas)):
        for j in range(len(vagas[i])):
            if (ct_conteudo[i][j][9:11]==mes):
                cont+=int(vagas[i][j])
            elif(ct_conteudo[i][j][9:11]==mes2):
                cont2+=int(vagas[i][j])
        vagas_por_ct.append(cont)
        vagas_por_ct2.append(cont2)
        cont=0
        cont2=0
    exel=[]
    exel2=[]
    for i in range(len(vagas_por_ct)):
        ct[i]=ct[i].replace('\n','')
        ct[i]=ct[i].replace('CT: ','')
        dicio={'CT':ct[i],'Vagas':vagas_por_ct[i]}
        exel.append(dicio)
        cont+=vagas_por_ct[i]
    dicio={"CT":"TOTAL","Vagas":cont}
    for i in range(len(vagas_por_ct2)):
        ct[i]=ct[i].replace('\n','')
        ct[i]=ct[i].replace('CT: ','')
        dicio2={'CT':ct[i],'Vagas':vagas_por_ct2[i]}
        exel2.append(dicio2)
        cont2+=vagas_por_ct2[i]
    dicio2={"CT":"TOTAL","Vagas":cont2}
    exel.append(dicio)
    de=pd.DataFrame(exel)
    exel2.append(dicio2)
    df=pd.DataFrame(exel2)
    try:
        mes=int(mes)
        mes=meses[mes-1]
        mes2=int(mes2)
        mes2=meses[mes2-1]
        arquivo=pd.ExcelWriter("Resultado_porCT_.xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Vagas em "+mes)
        df.to_excel(arquivo,sheet_name="Vagas em "+mes2)
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
  cont2=0
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
            cont2+=int(vagas[i][j])
          elif(veri==2):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
            cont2+=int(vagas[i][j])
          achei=False
        elif ((aux>=data and aux<=data2) and achei):
          if(veri==3 and hora==int(ct_conteudo[i][j][25:27])):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
            cont2+=int(vagas[i][j])
            achei=True
          elif(veri==1):
            print(ct_conteudo[i][j])
            cont+=int(vagas[i][j])
            cont2+=int(vagas[i][j])
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
  print('Vagas totais de todos os cts no intervalo {} até {}: {}'.format(data,data2,cont2))  
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
#######################################################################################
def para_vagas_por_semana(ct_conteudo,ct,vagas,ct_cidade,ct_cidade_sem,stop_lista):#8
    aux_cidade=[]
    data_formatada=[]
    for i in range(len(data_pegar)-1):
        data_formatada.append(data_pegar[i]+'-'+data_pegar[i+1])
    for i in range(len(data_pegar)):
        data_pegar[i]=sorted_data(data_pegar[i])
    ct_cidade_sem.sort()
    cont=cont2=cont3=cont4=cont5=cont6=cont7=cont8=0
    for k in range(len(ct_cidade_sem)):
        for i in range(len(ct_conteudo)):
            for j in range(len(ct_conteudo[i])):
                aux=ct_conteudo[i][j][6:16]
                aux=datetime.strptime(aux, '%d/%m/%Y').date()
                if((data_pegar[0]<=aux and data_pegar[1]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont+=int(vagas[i][j])
                elif((data_pegar[1]<=aux and data_pegar[2]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont2+=int(vagas[i][j])
                elif((data_pegar[2]<=aux and data_pegar[3]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont3+=int(vagas[i][j])
                elif((data_pegar[3]<=aux  and data_pegar[4]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont4+=int(vagas[i][j])
                elif((data_pegar[4]<=aux and data_pegar[5]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont5+=int(vagas[i][j])
                elif((data_pegar[5]<=aux and data_pegar[6]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont6+=int(vagas[i][j])
                elif((data_pegar[6]<=aux and data_pegar[7]>aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont7+=int(vagas[i][j])
                elif((data_pegar[7]<=aux and data_pegar[8]>=aux) and ct_cidade_sem[k]==ct_cidade[i]):
                    cont8+=int(vagas[i][j])
        total=cont+cont2+cont3+cont4+cont5+cont6+cont7+cont8
        dicio={"Cidade":ct_cidade_sem[k],"UF":ct_cidade_sem[k][-2::],
        data_formatada[0]:cont,data_formatada[1]:cont2,data_formatada[2]:cont3,
        data_formatada[3]:cont4,data_formatada[4]:cont5,data_formatada[5]:cont6,data_formatada[6]:
        cont7,data_formatada[7]:cont8,"Total":total}
        total=0
        aux_cidade.append(dicio)
        cont=cont2=cont3=cont4=cont5=cont6=cont7=cont8=0
    de=pd.DataFrame(aux_cidade)
    try:
        arquivo=pd.ExcelWriter("Resultado_dadosPorCidade.xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name="Resultado Por Cidade")
        arquivo.save()
        print()
        print("Arquivo salvo com sucesso!")
        print("Verifique o arquivo no diretório do programa!")
        print()
    except:
        print("\nErro em colocar os dados do arquivo")
        print("\nVerifique se o arquivo está aberto\n")   
    return 0
###########################################################################################
#aqui começa a formatação de dados
'''data=date.today()
data=str(data)
data=data.split("-")
data=data[-1::-1]'''
data_hoje="17-01-22"
passou=True
print(data_hoje)
try:
  arq=open("arquivo.txt",'r+')
except:
  passou=False
  print("\nArquivo: Dados\dado"+data_hoje+".txt Não encontrado!\n")
  print("Verifique se o arquivo está com a data de hoje!!!\n")
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
  data=[]
  ct_cidade=[]
  meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
  for i in range(len(dados)):
      if(dados[i][:3]=='CT:'):#pega a linha que contém as 3 letras CT:
          dados[i]=dados[i].replace("CT: ","")
          dados[i]=dados[i].replace("\n","")
          ct.append(dados[i])
          numero=len(dados[i])
          estado.append(dados[i][numero-2:numero])#pega o UF e adiciona na lista estado
          cidade=''
          stop=0
          stop_lista=[]
          for k in range(numero):
              if (dados[i][k]=="-"):
                  stop_lista.append(stop)
                  break
                  
              else:
                  stop+=1
          cidade=dados[i][stop+2:]
          ct_cidade.append(cidade)
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
  ct_cidade_sem=[]
  for i in range(len(ct_cidade)):
    if (ct_cidade[i] in ct_cidade_sem):
        continue
    else:
        ct_cidade_sem.append(ct_cidade[i])
  print(ct_conteudo[0][0][6:16])
  for i in range(len(ct_conteudo)):
    for j in range(len(ct_conteudo[i])):
        if ( ct_conteudo[i][j][6:16] in data):
            continue
        else:
            data.append(ct_conteudo[i][j][6:16])
  def sorted_data(x):
      aux=datetime.strptime(x, '%d/%m/%Y').date()
      return aux
  japa=sorted(data,key=sorted_data)
  resto=len(data)%5
  data_pegar=[]
  for i in range(0,len(data),5):
      if(i==(int(len(data)//5))*5):
          data_pegar.append(japa[i+(resto-1)])
          print(i)
          print(resto)
      else:
          data_pegar.append(japa[i])  
  for i in data_pegar:
      print(i)
  data_pegar=data
  data_pegar.append("01/04/2022")
  
  while  True:
        print("Digite 1- para VAGAS TOTAIS")
        print("Digite 2- para VAGAS TOTAIS NO MES")
        print("Digite 3- para VAGAS TOTAIS NO MÊS E NO REFERIDO ESTADO (EXCEL)")
        print("Digite 4- para criar arquivo Excel(vivian)")
        print("Digite 5- para VAGAS TOTAIS NO MÊS E NO REFERIDO CT (EXCEL)")
        print("Digite 6- por data")
        print("Digite 7- para resultado na pasta reultado_dados")
        print("Digite 8- para vagas por semana e por cidade")
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
            para_vagas_totais_no_mes_porct(ct,estado,vagas,ct_conteudo,meses)
        elif (entrada==6):
            por_dia(ct,vagas,ct_conteudo)
        elif(entrada==7):
            para_vagas_totais_no_mes(ct,estado,vagas,ct_conteudo,meses)
        elif(entrada==8):
            para_vagas_por_semana(ct_conteudo,ct,vagas,ct_cidade,ct_cidade_sem,stop_lista)
        print()
        ence=int(input("Encerrar programa? 1 - Sim, 2 - Não: "))
        if (ence==1):
            break

