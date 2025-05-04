from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep


user = "Bigorna"
senha = "senhadeverdade123"

cores = ['Branco','Preto','Prata','Vermelho','Verde','Azul','Rosa']

def selecionar_cor(driver, cor):

    select_elem = driver.find_element(By.ID, "cor")
    select_elem.click()                              
    select = Select(select_elem)                    

    if cor in cores:
        select.select_by_visible_text(cor)           
    else:
        select.select_by_index(len(cores))           

url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/seda/estado-es/norte-do-espirito-santo?pe=60000&me=40000&rs=65"
driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

anuncios = soup.find_all('section', class_='olx-adcard')
lista_anuncios = []
for anuncio in anuncios:
    links = anuncio.find_all('a', class_='olx-adcard__link', href=True)
    for link in links:
        lista_anuncios.append(link['href'])

informacoes_carros = []

for url_anuncio in lista_anuncios[0:10]:
    print(f"Acessando: {url_anuncio}")
    driver = webdriver.Firefox()
    driver.get(url_anuncio)
    sleep(5)
    html = driver.page_source
    driver.quit()

    dados = {}
    soup = BeautifulSoup(html, 'html.parser')
    info_divs = soup.find_all('div', class_='ad__sc-2h9gkk-1')
    preco = soup.find("span","olx-text olx-text--title-large olx-text--block")
    cidade = soup.find_all("span","olx-text olx-text--body-small olx-text--block olx-text--regular ad__sc-k5plwo-1 idmeSY")
    
    dados['cidade'] = cidade[1].get_text().split(',')[1].split('-')[0].strip()
    dados['preço'] = preco.get_text().replace("R$","").replace(".","").strip()
    for div in info_divs:
        label = div.find('span')
        valor = div.find('a') or div.find_all('span')[-1]
        if label and valor:
            chave = label.get_text(strip=True)
            conteudo = valor.get_text(strip=True)
            dados[chave] = conteudo
    
    informacoes_carros.append(dados)
print("Todos os anuncios foram visitados")

url = "http://weka.inf.ufes.br/IFESTP/login.php"
driver = webdriver.Firefox()
driver.get(url)
nao_usuario_de_crack = driver.find_element(By.ID, 'username')
senha_do_nao_usuario = driver.find_element(By.ID, 'password')
nao_usuario_de_crack.send_keys(user)
senha_do_nao_usuario.send_keys(senha)
login_buton =  driver.find_element(By.XPATH,'/html/body/div/div/div/form/div[4]/div/input')
login_buton.click()

sleep(2)

insert_buton = driver.find_element(By.XPATH,'/html/body/div/div/div/button')
insert_buton.click()
sleep(2)

for i in informacoes_carros:
    print(f"\n🔹 Anúncio {i}")
    input_marca = driver.find_element(By.ID, "marca")
    input_modelo = driver.find_element(By.ID, "modelo")
    input_ano = driver.find_element(By.ID, "ano")
    input_cambio = driver.find_element(By.ID, "cambioAutomatico")
    input_sedan = driver.find_element(By.ID, "c_sedan") 
    input_hatch = driver.find_element(By.ID, "c_hatch") 
    input_valor = driver.find_element(By.ID, "valor") 
    input_municipio = driver.find_element(By.ID, "municipio") 

    input_cor = driver.find_element(By.ID, "cor")
    register_buton = driver.find_element(By.NAME, "insert") 
    
    input_marca.send_keys(i['Marca'])
    input_modelo.send_keys(i['Modelo'])
    input_ano.send_keys(i['Ano'])
    
    if(i['Câmbio'] != 'Manual'):
        input_cambio.click()
    if(i['Tipo de veículo'] == 'Sedã'):
        input_sedan.click()
    else:
        input_hatch.click()
        
    cor = i.get('Cor', 'CorInexistente')
    selecionar_cor(driver, cor)

    input_valor.send_keys(i['preço'])
    input_municipio.send_keys(i['cidade'])
    register_buton.click()
    sleep(2)
    insert_buton = driver.find_element(By.XPATH,'/html/body/div/div/div/button')
    insert_buton.click()

driver.quit()