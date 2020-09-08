import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

def Creacion_de_cuneta():
    #CREACION DE CUENTA
    driver.get("https://preunic.cl/signup")
    print("Empezo")
    time.sleep(5)
    nombre = driver.find_element_by_name("spree_user[firstname]")
    nombre.send_keys("Elizabeth")
    apellido = driver.find_element_by_name("spree_user[lastname]")
    apellido.send_keys("Pareja")
    cumple = driver.find_element_by_xpath('//input[@name="spree_user[birthday]"][@class="form-control"]')
    cumple.click()
    cumple.send_keys("13061998")
    sexo = driver.find_element_by_name("spree_user[gender]")
    sexo.send_keys(Keys.ARROW_DOWN)
    boton = driver.find_element_by_xpath('//label[@for="run_type_rut"]/*[@class="radio-circle"]')
    boton.click()
    rut = driver.find_element_by_name("spree_user[run]")
    rut.send_keys("199565540")
    email = driver.find_element_by_name("spree_user[email]")
    email.send_keys("eli_pareja@hotmail.com")
    tel = driver.find_element_by_name("spree_user[phone]")
    tel.send_keys("+56966082889")
    contra = driver.find_element_by_name("spree_user[password]")
    contra.send_keys("cripto")
    contra2 = driver.find_element_by_name("spree_user[password_confirmation]")
    contra2.send_keys("cripto")
    boton2 = driver.find_element_by_xpath('//label[@for="spree_user_taxon_ids_1880"]')
    boton2.click()
    boton3 = driver.find_element_by_xpath('//label[@for="spree_user_accept_terms_and_conditions"]/*[@class="checkbox"]')
    boton3.click()
    crear = driver.find_element_by_name("button")
    crear.click()
    return
    
def iniciar_sesion():
    
    #ENTRAR A LA CUENTA
    driver.get("https://preunic.cl/login")
    correo = driver.find_element_by_name("spree_user[email]")
    correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys("cripto",Keys.TAB)
    boton = driver.find_element_by_name("button")
    boton.click()
    return

def recuperar_contraseña():    
    #RECUPERAR CONTRASEÑA
    driver.get("https://preunic.cl/password/recover")
    correo = driver.find_element_by_name("spree_user[email]")
    correo.send_keys("eli_pareja@hotmail.com")
    boton = driver.find_element_by_name("commit")
    boton.click()
    return
    
def cambiar_contraseña():

    #CAMBIAR CONTRASEÑA
    driver.get("https://preunic.cl/login")
    correo = driver.find_element_by_name("spree_user[email]")
    correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys("cripto",Keys.TAB)
    boton = driver.find_element_by_name("button")
    boton.click()
    time.sleep(2)
    driver.get("https://preunic.cl/account")
    time.sleep(10)
    contra = driver.find_element_by_name("user[password]")
    contra.send_keys("cripto2")
    contra2 = driver.find_element_by_name("user[password_confirmation]")
    contra2.send_keys("cripto",Keys.TAB)
    boton = driver.switch_to_active_element()
    boton.send_keys(Keys.RETURN)
    return

def fuerza_bruta():
    driver.get("https://preunic.cl/login")
    i=0
    while i <=100:
        correo = driver.find_element_by_name("spree_user[email]")
        correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
        elem = driver.switch_to_active_element()
        elem.send_keys("a",Keys.TAB)
        boton = driver.find_element_by_name("button")
        boton.click()
        i = i+1
    return






