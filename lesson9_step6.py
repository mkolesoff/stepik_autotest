from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    knopka = browser.find_element_by_class_name('btn')
    knopka.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input1 = browser.find_element_by_id('input_value')
    x = input1.text
    y = calc(x)
    input2 = browser.find_element_by_id('answer')
    input2.send_keys (y)
    knopka2 = browser.find_element_by_class_name('btn').click()
    
      
      
      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()