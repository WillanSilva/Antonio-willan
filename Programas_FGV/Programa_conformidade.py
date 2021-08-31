import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import locale
#proximo passo é pegar os dados da porcentagem
def pegando_sheet(a,tamanho,dados,shet):
    for i in range(1,tamanho+1):
        try:
            arquivo_exel2=pd.read_excel(a,sheet_name=i)
            aux1=arquivo_exel2.columns[0][0].upper()
            aux1=aux1+arquivo_exel2.columns[0][1::]
            arquivo_exel2=arquivo_exel2.values
        except:
            print('\nErro ao encontrar o nome do ct!')
            print("\nO nome da Sheet cujo deu erro foi: ")
            try:
                print(shet[i])
            except:
                print("Erro ao indentificar a shet")
    
        lista=[0]*2
        aux3=[]
        for k in range(4,20,5):
            for j in range(4,6):
                try:
                    pega=arquivo_exel2[k][j]
                    try:
                        if(pega!=0.000):
                            aux=round(pega*100)
                            lista[j-4]=aux
                        else:
                            lista[j-4]=0
                    except:
                        aux="Não tem resultado de porcentagem!"
                except:
                    print("Erro ao localizar as porcentagens")
                    try:
                        print(shet[i])
                    except:
                        print("Erro ao indentificar a shet")
                    
            aux3.append(lista)
            lista=[0]*2
        dicio={'CT':aux1,'local':aux3[0],'ambiente': aux3[1],'qualidade':aux3[2],'etica':aux3[3]}
        dados.append(dicio)
    return (dados)
def colocar_emordem(dados):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')
    dados=sorted(dados,key=lambda dados: (locale.strxfrm(dados['CT'])))
    return (dados)
def calculando_porcentagem(dados,tamanho):
    cts_problema=[]
    for i in range(tamanho):
        local=dados[i]['local'][0]+dados[i]['local'][1]
        ambiente=dados[i]['ambiente'][0]+dados[i]['ambiente'][1]
        quali=dados[i]['qualidade'][0]+dados[i]['qualidade'][1]
        etica=dados[i]['etica'][0]+dados[i]['etica'][1]
        novo_dados={'CT':dados[i]['CT'],'Localização':'Regular: '+ str(dados[i]['local'][0])+'  e  '+'Ruim: '+str(dados[i]['local'][1]),'soma_L':str(local),
                  'Ambiente':'Regular: '+ str(dados[i]['ambiente'][0])+'  e  '+'Ruim: '+ str(dados[i]['ambiente'][1]),'soma_A':str(ambiente),
                  'Qualidade':'Regular: '+ str(dados[i]['qualidade'][0])+'  e  '+'Ruim: '+ str(dados[i]['qualidade'][1]),'soma_Q':str(quali),
                  'Ética':'Regular: '+ str(dados[i]['etica'][0])+'  e  '+'Ruim: '+ str(dados[i]['etica'][1]),'soma_E':str(etica)}
        if((dados[i]['local'][0]+dados[i]['local'][1])>=10):
            cts_problema.append(novo_dados)
        elif((dados[i]['ambiente'][0]+dados[i]['ambiente'][1])>=10):
            cts_problema.append(novo_dados)
        elif((dados[i]['qualidade'][0]+dados[i]['qualidade'][1])>=10):
            cts_problema.append(novo_dados)
        elif((dados[i]['etica'][0]+dados[i]['etica'][1])>=10):
            cts_problema.append(novo_dados)
        dados[i]={'CT':dados[i]['CT'],'Localização':'Regular: '+ str(dados[i]['local'][0])+'  e  '+'Ruim: '+str(dados[i]['local'][1]),'soma_L':str(local),
                  'Ambiente':'Regular: '+ str(dados[i]['ambiente'][0])+'  e  '+'Ruim: '+ str(dados[i]['ambiente'][1]),'soma_A':str(ambiente),
                  'Qualidade':'Regular: '+ str(dados[i]['qualidade'][0])+'  e  '+'Ruim: '+ str(dados[i]['qualidade'][1]),'soma_Q':str(quali),
                  'Ética':'Regular: '+ str(dados[i]['etica'][0])+'  e  '+'Ruim: '+ str(dados[i]['etica'][1]),'soma_E':str(etica)}
    return cts_problema,dados
def criando_arquivo(cts_problema,dados):
    df=pd.DataFrame(cts_problema)
    de=pd.DataFrame(dados)
    try:
        arquivo=pd.ExcelWriter("Resultado_programa.xlsx")
    except:
        print("Erro na abertura de arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    try:
        de.to_excel(arquivo,sheet_name='TODOS OS CTs')
        df.to_excel(arquivo, sheet_name='CTs DE NÃO CONFORMIDADE')
        arquivo.save()
    except:
        print("\nErro em colocar os dados no arquivo do arquivo")
        print("\nVerifique se o arquivo está aberto\n")
    return ()
Tk().withdraw() # Isto torna oculto a janela principal
a = askopenfilename() # Isto te permite selecionar um arquivo
while True:
    try:
        arquivo_exel=pd.read_excel(a)
        tamanho=pd.ExcelFile(a)
        tamanho=tamanho.sheet_names
        break
    except:
        print("\nVerifique o nome do arquivo digitado")
        print("\nLembrando que o arquivo tem que estar na mesma pasta do programa!\n")
shet=tamanho
tamanho=len(tamanho)-1
dados=[]
arquivo_exel=arquivo_exel.values
print("\nPegando os nomes dos CTs na Planilha...")
print("\nPegando os dados das porcentagens...")
print("\nEsse processo pode demorar um pouco por favor aguarde...")
dados=pegando_sheet(a,tamanho,dados,shet)
print("\nordenando os dados...")
print("\nCalculando a porcentagem...")
dados=colocar_emordem(dados)
cts_problema,dados=calculando_porcentagem(dados,tamanho)
print("\nCriando arquivo plailha...")
criando_arquivo(cts_problema,dados)
print("\nPrograma finalizado!!\n")
print("Por favor cheque o arquivo na pasta!\n")
