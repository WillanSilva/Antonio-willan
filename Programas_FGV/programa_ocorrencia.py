from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
while True:
    login_1=input("Digite o seu Login: ")
    senha_1=input("Digite a sua Senha: ")
    certeza=input("Tem certeza que o login e senha estão corretos ? (s - sim/ n- não): ")
    if certeza.lower()=='s' or certeza.lower()=='sim':
        print()
        break
    else:
        print("\nDigite Novamente! \n")
mes=input("Digite o mês de busca (05 -> Maio): ")
ano=input("Digite o ano de busca (exemplo 2024): ")
navegador = webdriver.Chrome()
navegador.get("https://certpessoas.fgv.br/ct/")
nome = navegador.find_element(By.NAME, "UserName")  
senha = navegador.find_element(By.NAME, "Password")
navegador.implicitly_wait(2)
nome.send_keys(login_1)#teu login 
senha.send_keys(senha_1)#tua senha
navegador.implicitly_wait(2)
senha.send_keys(Keys.RETURN)
navegador.implicitly_wait(2)
ok=input("\nColocou o aceitar nos cooks ?")
navegador.find_element("xpath",'//*[@id="aspnetForm"]/div[4]/div/div[1]/dl/dd[11]/a').click()
time.sleep(2)
navegador.find_element("xpath",'//*[@id="aspnetForm"]/div[4]/div/div[1]/dl/dd[11]/div/a[1]').click()
time.sleep(2)
opcoes_mes=navegador.find_element(By.ID, "ctl00_ContentMain_dropMes")
time.sleep(2)
opcoes_mes=Select(opcoes_mes)
opcoes_mes.select_by_value(mes)
opcoes_ano=navegador.find_element(By.ID, "ctl00_ContentMain_dropAno")
time.sleep(2)
opcoes_ano=Select(opcoes_ano)
opcoes_ano.select_by_value(ano)
navegador.find_element("xpath",'//*[@id="ctl00_ContentMain_btnProcurar"]').click()
#lopp
dados=[]
pagina=1
while True:
    elementos = navegador.find_elements(By.CLASS_NAME, "td-descricao")
    descricoes=[]
    for i, elemento in enumerate(elementos, start=1):
        descricao = elemento.text.strip()
        #print(f'Descrição {i}:', descricao)
        descricoes.append(descricao)
    for i in range(len(descricoes)):
        if (i+2)<10:
            navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl0'+str(i+2)+'_btVisualizar').click()
            time.sleep(1)
            data=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl0'+str(i+2)+'_lblData')
            data=data.text.strip()
            tipo=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl0'+str(i+2)+'_lblTipo')
            tipo=tipo.text.strip()
            Centro_de_teste=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl0'+str(i+2)+'_lblCentroTeste')
            Centro_de_teste=Centro_de_teste.text.strip()
            usuario=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl0'+str(i+2)+'_lblUsuario')
            usuario=usuario.text.strip()
            
        else:
            navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl'+str(i+2)+'_btVisualizar').click()
            time.sleep(1)
            data=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl'+str(i+2)+'_lblData')
            data=data.text.strip()
            tipo=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl'+str(i+2)+'_lblTipo')
            tipo=tipo.text.strip()
            Centro_de_teste=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl'+str(i+2)+'_lblCentroTeste')
            Centro_de_teste=Centro_de_teste.text.strip()
            usuario=navegador.find_element(By.ID,'ctl00_ContentMain_gvAcontecimento_ctl'+str(i+2)+'_lblUsuario')
            usuario=usuario.text.strip()
        aux={'Data':data,'Tipo':tipo,'Centro_de_Teste':Centro_de_teste, 'Descrição':descricoes[i],'Usuario':usuario}
        dados.append(aux)
    print(f"\nFeito Pagina {pagina}")
    pagina+=1
    try:
        link = navegador.find_element(By.LINK_TEXT, str(pagina))
        link.click()
    except NoSuchElementException:
        try:
            xpath_link = f"//a[contains(@href, 'Page${pagina}')]"
            link = navegador.find_element(By.XPATH, xpath_link)
            link.click()
        except NoSuchElementException:
            try:
                if pagina % 11 == 0:
                    navegador.find_element(By.XPATH, '//*[@id="ctl00_ContentMain_gvAcontecimento"]/tbody/tr[13]/td/table/tbody/tr/td[11]/a').click()
                elif pagina % 21 == 0 or pagina % 31 == 0 :
                    navegador.find_element(By.XPATH, '//*[@id="ctl00_ContentMain_gvAcontecimento"]/tbody/tr[13]/td/table/tbody/tr/td[13]/a').click()
                else:
                    break
            except NoSuchElementException:
                break
de=pd.DataFrame(dados)
print("\nColocando os dados no arquivo Excel\n")
nome_arquivo=f"Resultado_programa_Ocorrencia_{meses[int(mes)-1]}_Ano_{ano}.xlsx"
with pd.ExcelWriter(nome_arquivo, engine='xlsxwriter') as arquivo:
    de.to_excel(arquivo, sheet_name="Ocorrencias", index=False)
print("\nPrograma Finalizado!\n")
