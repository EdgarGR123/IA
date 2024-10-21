from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configuración de opciones de Firefox
firefox_options = Options()
firefox_options.add_argument("--headless")  # Ejecuta Firefox en modo headless (sin interfaz gráfica)
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Inicializa el driver de Firefox
driver = webdriver.Firefox(options=firefox_options)

try:
    # Abre Google
    driver.get("https://www.google.com")

    # Encuentra la barra de búsqueda por nombre del elemento
    search_box = driver.find_element("name", "q")

    # Escribe algo en la barra de búsqueda
    search_box.send_keys("Selenium con Python")
    
    # Simula presionar la tecla "Enter"
    search_box.send_keys(Keys.RETURN)

    # Espera unos segundos para que se carguen los resultados
    time.sleep(5)

    # Imprime el título de la página
    print(driver.title)

finally:
    # Cierra el driver
    driver.quit()
