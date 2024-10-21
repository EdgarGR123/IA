import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Clase_IA():
    def __init__(self, titulo):
        self.titulo = titulo
        self.driver = None

    def Iniciar_driver(self):
        firefox_options = Options()
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.set_preference("general.useragent.override", 
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Firefox(options=firefox_options)

    def Iteractuar(self):
        try:
            self.driver.get("https://copilot.microsoft.com/")
            time.sleep(2)
           
            boton_inicio = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div[2]/aside/div[1]/div/div[3]/button"))
            )
            boton_inicio.click()
            time.sleep(2)
    
            textarea_nombre = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div[2]/aside/div[1]/div/div[2]/div/div[1]/div/div/div/div/textarea"))
            )

            textarea_nombre.send_keys("muchacho123")
            textarea_nombre.send_keys(Keys.RETURN)
            time.sleep(2)
    
            self.driver.refresh()            
    
            textarea = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/textarea"))
            )

            textarea.click()
            textarea.send_keys(f"Puedes generar la descripción y características de este producto de computadoras : {self.titulo}")
            textarea.send_keys(Keys.RETURN)
            time.sleep(2)
    
            body = self.driver.find_element(By.TAG_NAME, 'body')
            body.click()
            time.sleep(2)
    
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
           
            texto_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".space-y-3.break-words"))
            )
            
            parrafos = texto_div.find_elements(By.TAG_NAME, 'p')
            texto_respuesta = ' '.join([p.text for p in parrafos])
    
            if texto_respuesta:
                return texto_respuesta
            else:
                print("No se encontraron respuestas.")
        
        except NoSuchElementException:
            print("No se encontró el elemento.")
        except TimeoutException:
            print("El tiempo de espera se agotó.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.driver:
                self.driver.quit()

if __name__ == "__main__":
    titulo_producto = sys.argv[1]
    mi_ia = Clase_IA(titulo_producto)
    mi_ia.Iniciar_driver()
    texto_generado = mi_ia.Iteractuar()
    if texto_generado:
        print(texto_generado)  # Esto se capturará en la salida del subprocess
