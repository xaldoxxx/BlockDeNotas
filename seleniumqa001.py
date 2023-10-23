from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class BuscadorEmpleoGoogle:
    def __init__(self):
        self.driver = self._iniciar_driver()

    def _iniciar_driver(self):
        opciones = Options()
        opciones.page_load_strategy = 'normal'
        return webdriver.Chrome(options=opciones)

    def navegar_a_empleos_google(self):
        self.driver.get("https://www.google.com/about/careers/applications/jobs/results/")
        time.sleep(3)

    def buscar_empleos(self, palabra_clave):
        cuadro_busqueda = self.driver.find_element(By.XPATH, "/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/input[1]")
        cuadro_busqueda.send_keys(palabra_clave)
        time.sleep(3)

    def aplicar_filtros(self):
        boton_filtro = self.driver.find_element(By.XPATH, "//button[@aria-label='Locations filter options']//i[@aria-hidden='true']")
        boton_filtro.click()
        time.sleep(3)

        lista_trabajos = self.driver.find_element(By.XPATH, "/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]")
        lista_trabajos.click()
        time.sleep(3)

    def ordenar_por(self):
        boton_ordenar = self.driver.find_element(By.XPATH, "(//i[@class='google-material-icons VfPpkd-kBDsod'][normalize-space()='expand_more'])[6]")
        boton_ordenar.click()
        time.sleep(3)

        boton_enviar = self.driver.find_element(By.XPATH, '/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]')
        boton_enviar.click()
        time.sleep(3)

    def obtener_descripcion_trabajo(self):
        descripcion_trabajo = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div[2]/main')
        return descripcion_trabajo.text

    def cerrar_navegador(self):
        self.driver.quit()

if __name__ == "__main__":
    buscador = BuscadorEmpleoGoogle()
    try:
        buscador.navegar_a_empleos_google()
        buscador.buscar_empleos("python")
        buscador.aplicar_filtros()
        buscador.ordenar_por()
        texto_trabajo = buscador.obtener_descripcion_trabajo()
        print(texto_trabajo)
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        buscador.cerrar_navegador()
