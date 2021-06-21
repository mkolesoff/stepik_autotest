from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    sunduk = browser.find_element_by_id("treasure")
    x = sunduk.get_attribute("valuex")
    print(x)
    y=calc(x)
    
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    check2 = browser.find_element_by_id("robotsRule")
    check2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()