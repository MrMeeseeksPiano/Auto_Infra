from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

tempo = 2

def button_click_css(path):
    def encontrar_botao_visivel():
        botoes = driver.find_elements(By.CSS_SELECTOR, path)
        for botao in botoes:
            if botao.is_displayed() and botao.is_enabled():
                return botao
        return None

    botao_visivel = wait.until(lambda d: encontrar_botao_visivel())
    time.sleep(tempo)  
    botao_visivel.click()

def field_enter_css(path,texto):
    def encontrar_campo_visivel():
        campos = driver.find_elements(By.CSS_SELECTOR, path)
        for campo in campos:
            if campo.is_displayed() and campo.is_enabled():
                return campo
        return None

    campo_visivel = wait.until(lambda d: encontrar_campo_visivel())
    time.sleep(tempo)  
    campo_visivel.send_keys(texto)
    


def encontrar_input_file(path="div[data-test='is-file-upload_upload'] input[type='file']"):
    return wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path))
    )

photo_folder = input("Digite o caminho da pasta com as fotos: ").replace("\\","/")
caminho_webdriver = input("Digite o caminho do webdriver: ")
photos = os.listdir(photo_folder)
print(photos)

os.environ['PATH'] += rf"{caminho_webdriver}"

options_chrome = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options_chrome)
driver.get("https://new.infraspeak.com/")

wait = WebDriverWait(driver, 100)

css_new_photo = 'button[data-test="card-element-task-measurement_upload-file"]'
css_adicionar_button ='button[data-test="IsActionButtonSubmit"]'
login_path = 'input[name="user"]'
seguinte_button = 'button[data-test="screen-login_submit"]'
senha_path = 'input[type="password"]'
email = ''
senha = ''

field_enter_css(login_path,email)
button_click_css(seguinte_button)
field_enter_css(senha_path,senha)
button_click_css(seguinte_button)

for photo in photos:
    button_click_css(css_new_photo)
    input_upload = encontrar_input_file()
    caminho = photo_folder + f'/{photo}'
    input_upload.send_keys(caminho)
    button_click_css(css_adicionar_button)


input("Pressione Enter para sair...")
