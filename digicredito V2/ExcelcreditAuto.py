
from time import sleep
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import casesListas as CL 



# Datos de credito
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://digicredito-dev2.excelcredit.co/login")
wait = WebDriverWait(driver, 10)



#Login
driver.find_element(By.ID, 'login-button').click()
driver.find_element(By.ID, 'username').send_keys("jtellez@excelcredit.co")
driver.find_element(By.ID, 'password').send_keys("Suaita01")
driver.find_element(By.NAME, 'login').click()
sleep(2)

span_element = WebDriverWait(driver,2).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div/div/div[3]/span'))
    )
span_element.click()

enlace_pendientes = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div[2]/div[2]/a[1]/p')
enlace_pendientes.click()
sleep(5)



"""""
driver.find_element(By.ID, 'search-field').send_keys("71605230")  
#60291918
#23554825
#60291918
#8390920

sleep(5)



driver.find_element(By.ID, 'select-item').click()
sleep(5)


#driver.get("https://digicredito-dev2.excelcredit.co/admin/simulator")
#sleep(10)

datos =  CL.dataSimulador()
print(datos)


# DATOS COMPLEMENTARIOS -> EN_REGISTRO_DATOS_ADICIONALES_CLIENTE 

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div[1]').click()
sleep(2)

input_element = driver.find_element(By.ID, 'lugarNacimiento2')
input_element.clear() 
input_element.send_keys(datos['nCiudad']) 
sleep(2)



driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div/div[2]/div[6]').click()
sleep(2)


#input_element = driver.find_element(By.ID, 'departamento')
#input_element.clear() 
#input_element.send_keys(datos['departamento']) 
#sleep(4)

driver.find_element(By.ID, 'departamento').send_keys("Amazonas")
sleep(2)
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/div/div/div').click()
sleep(2)

#input_element = driver.find_element(By.ID, 'ciudad')
#input_element.clear() 
#input_element.send_keys(datos['ciudad']) 
#sleep(4)

driver.find_element(By.ID, 'ciudad').send_keys("Leticia")
sleep(2)
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/div/div/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[5]/div[1]/input').click()
sleep(2)

driver.find_element(By.ID, 'calleModal').send_keys("CARRERA")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/input').send_keys("10")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/input').send_keys("27")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[5]/input').send_keys("11")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/button').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/input').send_keys("CENTRO")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[8]/div[1]/input').send_keys("1")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[8]/div[2]/input').send_keys("1")
sleep(2)

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[9]/div[1]/input')
input_element.clear() 
input_element.send_keys("PENSIONADO") 
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[9]/div[2]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[9]/div[2]/div/div[2]/div[1]').click()
sleep(2)

driver.find_element(By.ID, 'submit').click()
sleep(10)



# DATOS LABORALES O PENSIONALES -> SIMULACION_FINAL_ASESOR

#driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div/input').send_keys("906522914100")
#sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/div/input').send_keys("22/08/2023")
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[7]/div/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[7]/div/div/div[2]/div').click()
sleep(2)

upload_file = "D:\\Usuarios\\aprendiz.desarrollo1\\Desktop\\digicredito V2\\imgns\\2.png"  # Ruta de tu archivo de imagen
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[8]/div/label/div").click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[9]/button[2]').click()
sleep(10)




#DATOS PARA EL CREDITO

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/input')
input_element.clear() 
input_element.send_keys("P.A. COLPENSIONES") 
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/div/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div[1]').click()
sleep(2)


driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[3]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[3]/div/div[2]/div[5]').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div').click()
sleep(2)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div[2]').click()
sleep(2)

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input[1]')
input_element.clear() 
input_element.send_keys(datos['totalActivos']) 
sleep(4)


#driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[1]/input[1]').send_keys("30000000")
#sleep(2)

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[1]/input[1]')
input_element.clear() 
input_element.send_keys("30000000") 
sleep(4)


input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/input[1]')
input_element.clear() 
input_element.send_keys(datos['descuentosNomina']) 
sleep(4)


input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[5]/div[1]/input[1]')
input_element.clear() 
input_element.send_keys(datos['descuentosLey']) 
sleep(4)


driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div/div[2]/div[3]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[8]/button[2]').click()
sleep(10)

#RESULTADOS CALCULO CREDITO 

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/form/div[2]/div/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/form/div[2]/div/div/div[2]/div[2]').click()
sleep(5)


driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div/button').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/button').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div[3]/button').click()
sleep(10)


#INFORMACIÓN BASICA SOLICITANTE -> ENDEUDAMIENTO GLOBAL 

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div/div[2]/div[2]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/div[1]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/div[1]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[1]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[1]/div/div[2]/div[1]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div/div[2]/div[4]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/button').click()
sleep(10)

#INFORMACION FINANCIERA -> ENDEUDAMIENTO GLOBAL 

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/div/input[1]')

input_element.send_keys(datos['descuentosLey']) 
sleep(4)

input_element = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/input[1]')

input_element.send_keys(datos['descuentosNomina']) 
sleep(4)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[6]/div/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[6]/div/div/div[2]/div[1]').click()
sleep(5)

upload_file = "D:\\Usuarios\\aprendiz.desarrollo1\\Desktop\\digicredito V2\\imgns\\2.png"  # Ruta de tu archivo de imagen
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)
driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[7]/div/label/div").click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[8]/button[2]').click()
sleep(10)



#MODALIDAD DE DESEMBOLSO -> EN SELECCION MEDIO DESEMBOLSO 

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[1]/div[1]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/div/div[2]/div[18]').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[2]/input').send_keys("12345678912345")
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div[1]/div/input').send_keys("Amazonas")
sleep(1)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div[1]/div/div/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div[2]/div/input').send_keys("Leticia")
sleep(1)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div[2]/div/div/div').click()
sleep(5)

driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/button').click()
sleep(5)

"""