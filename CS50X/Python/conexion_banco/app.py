import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = webdriver.EdgeService(executable_path="C:/Users/nusa9/Downloads/EdgeDriver/MicrosoftWebDriver.exe")

driver = webdriver.Edge(service = service)

# Accede a la página de inicio de sesión del banco
driver.get('https://www.bancsabadell.com/bsnacional/es/particulares/login/')

# Pausar para permitir que la página cargue
time.sleep(3)

# Rellenar el formulario de inicio de sesión
username = driver.find_element(By.ID, 'username')  # Actualiza con el selector correcto
password = driver.find_element(By.ID, 'password')  # Actualiza con el selector correcto

load_dotenv()

tu_usuario = os.getenv("tu_usuario")
tu_contraseña = os.getenv("tu_contraseña")

username.send_keys(tu_usuario)
password.send_keys(tu_contraseña)

# Enviar el formulario
password.send_keys(Keys.RETURN)

# Pausar para permitir la autenticación y carga del balance
time.sleep(10)

# Obtener el balance de la cuenta
balance_element = driver.find_element(By.CLASS, "bs-modulo-amount")  # Actualiza con el selector correcto
balance = balance_element.text

print(f'Tu balance es: {balance}')

# Cerrar el navegador
driver.quit()
