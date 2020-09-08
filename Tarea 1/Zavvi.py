import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

    
def registrarse():   
    driver.get("https://www.zavvi.es/accountCreate.account")
    print("Empezo")
    time.sleep(5)
    nombre = driver.find_element_by_name("customerName")
    nombre.send_keys("Elizabeth Pareja")
    email = driver.find_element_by_name("customerEmail")
    email.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys("eli_pareja@hotmail.com")
    contra = driver.find_element_by_name("customerPassword")
    contra.send_keys("cripto")
    contra2 = driver.find_element_by_name("confirmPassword")
    contra2.send_keys("cripto")
    nomail = driver.find_element_by_id("OptInReceiveNewsLetterRadio2")
    nomail.click()
    elem = driver.switch_to_active_element()
    elem.send_keys(Keys.TAB)
    elem.send_keys(Keys.RETURN)
    return
    
    
def iniciar_sesion():
    driver.get("https://www.zavvi.es/login.jsp?returnTo=https%3A%2F%2Fwww.zavvi.es%2FaccountHome.account")
    time.sleep(5)
    correo = driver.find_element_by_name("elysium_username")
    correo.clear()
    correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys("cripto",Keys.TAB,Keys.TAB,Keys.TAB)
    elem.send_keys(Keys.RETURN)
    return
    
def recuperar_contraseña():
    driver.get("https://www.zavvi.es/login.jsp?returnTo=https%3A%2F%2Fwww.zavvi.es%2FaccountHome.account")
    time.sleep(5)
    elem = driver.find_element_by_name("elysium_password")
    elem.send_keys(Keys.TAB,Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys(Keys.RETURN)
    correo = driver.find_element_by_id("forgotten-password-email-field")
    correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys(Keys.RETURN)
    return
    

def cambiar_contraseña():   
    driver.get("https://www.zavvi.es/login.jsp?returnTo=https%3A%2F%2Fwww.zavvi.es%2FaccountHome.account")
    time.sleep(5)
    correo = driver.find_element_by_name("elysium_username")
    correo.clear()
    correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys("cripto",Keys.TAB,Keys.TAB,Keys.TAB)
    elem.send_keys(Keys.RETURN)
    driver.get("https://www.zavvi.es/accountSettings.account")
    time.sleep(5)
    contra = driver.find_element_by_name("oldPassword")
    contra.send_keys("crpto")
    contra2 = driver.find_element_by_name("newPassword")
    contra2.send_keys("cripto")
    contra3 = driver.find_element_by_name("confirmPassword")
    contra3.send_keys("cripto",Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys(Keys.RETURN)
    return

def fuerza_bruta():
    driver.get("https://www.zavvi.es/login.jsp?returnTo=https%3A%2F%2Fwww.zavvi.es%2FaccountHome.account")
    i=0
    while i<=100:
        correo = driver.find_element_by_name("elysium_username")
        correo.clear()
        correo.send_keys("eli_pareja@hotmail.com",Keys.TAB)
        elem = driver.switch_to_active_element()
        elem.send_keys("a",Keys.TAB,Keys.TAB,Keys.TAB)
        elem.send_keys(Keys.RETURN)
        i=i+1
    return



