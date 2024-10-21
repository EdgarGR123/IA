from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class Clase_IA():
    def __init__(self, titulo):
        self.titulo = titulo
        self.driver = None

    def Iniciar_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            '''
        })

    def Iteractuar(self):
        print("hola como estas prueba")
        try:
            self.driver.get("https://copilot.microsoft.com/")
            time.sleep(2)

            boton_inicio = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/aside/div[1]/div/div[3]/button"))
            )
            boton_inicio.click()
            time.sleep(2)

            print("verificar... si llega")
            textarea_nombre = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/aside/div[1]/div/div[2]/div/div[1]/div/div/div/div/textarea"))
            )
            textarea_nombre.send_keys("muchacho123")
            textarea_nombre.send_keys(Keys.RETURN)
            time.sleep(2)

            print("segundo paso")

            siguiente = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/aside/div[1]/div/div[2]/button"))
            )
            print("tercer paso")
            siguiente.click()
            time.sleep(2)
            

            textarea = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/textarea"))
            )
            textarea.click()
            textarea.send_keys(f"Puedes generar la descripción y características de este producto: {self.titulo}")
            textarea.send_keys(Keys.RETURN)
            time.sleep(5)

            print("cuarto paso")

            texto_div = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-content='ai-message']"))
            )
            parrafos = texto_div.find_elements(By.TAG_NAME, 'p')
            texto_respuesta = ' '.join([p.text for p in parrafos])

            print("quinto paso")

            if texto_respuesta:
                print("Respuesta de Copilot:", texto_respuesta)
                return texto_respuesta
            else:
                print("No se encontraron respuestas.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.driver.quit()

    