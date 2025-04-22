from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/seda/estado-es/norte-do-espirito-santo?pe=60000&me=40000&rs=65"
driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

anuncios = soup.find_all('section', class_='AdCard_root__Jkql_ AdCard_vertical__GTiaJ')
lista_anuncios = []
for anuncio in anuncios:
    links = anuncio.find_all('a', class_='AdCard_link__4c7W6', href=True)
    for link in links:
        lista_anuncios.append(link['href'])


informacoes_carros = []

for url_anuncio in lista_anuncios:
    print(f"Acessando: {url_anuncio}")
    driver = webdriver.Firefox()
    driver.get(url_anuncio)
    sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    
    
    info_divs = soup.find_all('div', class_='ad__sc-2h9gkk-1')

    dados = {}
    for div in info_divs:
        label = div.find('span')
        valor = div.find('a') or div.find_all('span')[-1]
        if label and valor:
            chave = label.get_text(strip=True)
            conteudo = valor.get_text(strip=True)
            dados[chave] = conteudo
    
    informacoes_carros.append(dados)

# Exibir os dados extraídos
for i, info in enumerate(informacoes_carros):
    print(f"\n🔹 Anúncio {i+1}")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
