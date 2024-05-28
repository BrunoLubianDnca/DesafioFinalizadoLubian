import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#navegador
def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

#YouTube
def acessar_youtube(driver):
    driver.get("https://www.youtube.com")
    time.sleep(5)
def buscar_canal(driver, nome_canal):
    #Procura pelo canal
    barra_pesquisa = driver.find_element(By.NAME, "search_query")
    barra_pesquisa.send_keys(nome_canal)
    barra_pesquisa.send_keys(Keys.RETURN)
    time.sleep(5)
    
    #tempo de espera1
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "channel-title")))
    
    # abre o link do canal
    link_canal = driver.find_element(By.ID, 'channel-title')
    link_canal.click()
    time.sleep(5)
def abrir_video(driver):
    # Encontra os vídeos do canal
    videos = driver.find_elements(By.XPATH, "//ytd-grid-video-renderer")
    if not videos:
        print("Nenhum vídeo encontrado.")
        return
    
    # selecionar video
    video_escolhido = random.choice(videos)
    driver.execute_script("arguments[0].scrollIntoView(true);", video_escolhido)
    
    # tempo de espera2
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ytd-grid-video-renderer")))
    #
    video_escolhido.click()
    time.sleep(5)

#informações do vídeo, visualizações, descrição e hasgtags
def extrair_informacoes(driver):
    visualizacoes = driver.find_element(By.CSS_SELECTOR, "span.view-count").text
    descricao_element = driver.find_element(By.CSS_SELECTOR, "#content #description")
    descricao = descricao_element.text if descricao_element else "Sem descrição"
    tags = [word for word in descricao.split() if word.startswith("#")]
    return visualizacoes, descricao, " ".join(tags)


def main():
    driver = configurar_driver()
    try:
        acessar_youtube(driver)
        buscar_canal(driver, "Qontrol Alt")
        abrir_video(driver)
        
        # Extrai informações do vídeo
        visualizacoes, descricao, tags = extrair_informacoes(driver)
        
        # Exibe as informações
        print(f"Visualizações: {visualizacoes}")
        print(f"Descrição: {descricao}")
        print(f"Tags: {tags}")
        
        # Salva as informações
        with open("informacoes_video.txt", "w", encoding="utf-8") as file:
            file.write(f"Visualizações: {visualizacoes}\n")
            file.write(f"Descrição: {descricao}\n")
            file.write(f"Tags: {tags}\n")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
