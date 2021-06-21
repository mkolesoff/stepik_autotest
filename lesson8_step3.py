from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа и вычисляем сумму
    a = browser.find_element_by_id("num1")
    b = browser.find_element_by_id("num2")
    x = a.text
    y = b.text
    sum = str(int(x)+int(y))
    
    # находим список и значение  в нем
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum) # ищем элемент с нужным числом
    
    #   нажимаем кнопку
  
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()