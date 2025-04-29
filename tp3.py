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

anuncios = [['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE 1.6 MSI FLEX 16V 4P AUT', '2019', 'Manual', 'Sedã','Preto', '49999', 'Vila Velha'], ['FORD', 'FORD KA+ SEDAN 1.0 TIVCT FLEX 4P', '2019', 'Manual', 'Sedã','Prata', '55000', 'Vila Velha'], ['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE TRENDLINE 1.6 T.FLEX 8V 4P', '2018',
'Manual', 'Sedã', 'Branco', '53900', 'Vitória'], ['CHEVROLET', 'CHEVROLET PRISMA SED. LT 1.4 8V FLEXPOWER4P AUT.', '2019', 'Automático', 'Sedã', 'Preto', '49990', 'Serra'], ['FORD', 'FORD KA 1.5 SEDAN SE 12V FLEX 4P MEC.', '2020', 'Manual', 'Sedã', 'Cinza', '56900', 'Vila Velha'], ['HYUNDAI', 'HYUNDAI HB20COMFORT PLUS 1.0 TB FLEX 12V MEC.', '2017', 'Manual', 'Sedã', 'Branco', '55000', 'Colatina'], ['RENAULT','RENAULT LOGAN ZEN FLEX 1.0 12V 4P MEC.', '2020', 'Manual', 'Sedã', 'Branco', '51990', 'Vitória'],['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE 1.6 MSI FLEX 8V 4P', '2020', 'Manual', 'Sedã', 'Branco', '59500', 'VilaVelha'], ['FIAT', 'FIAT CRONOS DRIVE 1.8 16V FLEX AUT', '2020', 'Automático', 'Sedã', 'Cinza', '60000','Serra'], ['CHEVROLET', 'CHEVROLET ONIX SED. PLUS PREM. 1.0 12V TB FLEX AUT', '2020', 'Automático',
'Sedã', '4 portas', '600', 'Cariacica'], ['FORD', 'FORD KA+ SEDAN 1.0 SEL TICVT FLEX 4P', '2018',
'Manual', 'Sedã', 'Preto', '50000', 'Jaguaré']]

url = "http://weka.inf.ufes.br/IFESTP/login.php"
driver = webdriver.Firefox()
driver.get(url)
nao_usuario_de_crack = driver.find_element(By.ID, user)
senha_do_nao_usuario = driver.find_element(By.ID, senha)
nao_usuario_de_crack.send_keys('Bigorna')
senha_do_nao_usuario.send_keys('senhadeverdade123')
login_buton =  driver.find_element(By.XPATH,'/html/body/div/div/div/form/div[4]/div/input')
login_buton.click()

sleep(1)

insert_buton = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/button')
insert_buton.click()
sleep(1)


for anuncio in anuncios:
    
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
        
    
    
    input_marca.send_keys(anuncio[0])
    input_modelo.send_keys(anuncio[1])
    input_ano.send_keys(anuncio[2])
    
    if(anuncio[3] != 'Manual'):
        input_cambio.click()
    if(anuncio[4] == 'Sedã'):
        input_sedan.click()
    else:
        input_hatch.click()
    selecionar_cor(driver,anuncio[5])
    input_valor.send_keys(anuncio[6])
    input_municipio.send_keys(anuncio[7])
    register_buton.click()
    sleep(1)
    insert_buton = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/button')
    insert_buton.click()

driver.quit()