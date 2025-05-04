from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


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

for url_anuncio in lista_anuncios[0:3]:
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

for i, info in enumerate(informacoes_carros):
    print(f"\n🔹 Anúncio {i}")
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
