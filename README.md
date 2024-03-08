# DigiV2

--Borrar datos adicionales que llegn con el dato desde el objeto
# dato_completo = datos['departamento'] 
# dato_sin_iniciales = dato_completo[3:] 
# campo_departamento = driver.find_element(By.ID, 'departamento0')
# campo_departamento.send_keys(dato_sin_iniciales)
# driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[4]/div[2]/div/div/div').click()

--posibles soluciones a problemas al momento de poner a ejecutar el codigo 
pip install webdriver_manager
C:\Python311\python.exe -m pip install --upgrade pip
from webdriver_manager.chrome import ChromeDriverManager
