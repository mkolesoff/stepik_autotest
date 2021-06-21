from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    check1 = browser.find_element_by_css_selector('[name="firstname"]')
    check1.send_keys('ivan')
    check2 = browser.find_element_by_css_selector('[name="lastname"]')
    check2.send_keys('petrov')
    check3 = browser.find_element_by_css_selector('[name="email"]')
    check3.send_keys('petrov@ghj.ss')
    
    
    
    import os 
     

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input5 = browser.find_element_by_id('file')
    input5.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
     
    button.click()
    
      
      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()