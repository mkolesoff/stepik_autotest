from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа и вычисляем сумму
    a = browser.find_element_by_id("input_value")
    x = a.text
    y=calc(x)
    # Скролим страницу до polya
    tex = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", tex)
    tex.send_keys(y)
    # scrol do knopki
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # zapolnenie 4ekboksov
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    check2 = browser.find_element_by_id("robotsRule")
    check2.click()   
    
    button.click()
    
      
      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()