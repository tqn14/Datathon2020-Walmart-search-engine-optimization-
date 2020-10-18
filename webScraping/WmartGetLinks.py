import selenium 
from time import sleep
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import numpy as np 
import csv
# driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver = webdriver.Chrome(chrome_options=options)

URL = "https://www.walmart.com/m/deals/home-savings/home"
driver.get(URL)

link_list = []
i= 1
paginator_next_button = driver.find_element_by_class_name('paginator-btn-next')
while(paginator_next_button):
    print("PAGE #" + str(i))
    
    #GRAB PRODUCT LIST ON PAGE
    product_list = driver.find_element_by_class_name('search-product-result')
    products = product_list.find_elements_by_tag_name('li')
    # print(products.text)
     
    # ITERATE OVER PRODUCTS
    for product in products:
        #product_gridview = product.find_element_by_class_name('search-product-title')
        #links = product.find_elements_by_tag_name("a")
        #for link in links:
            #print(link.get_attribute("href"))
        product_link = product.find_element_by_class_name('product-title-link')
        link_text = product_link.get_attribute('href')
        link_list.append(link_text)
        
    try:
        paginator_next_button.click()
        sleep(2)
        i+=1
    except:
        print("Done")
        break
    
print("TOTAL # PAGE ", i)

df = pd.DataFrame({'url': link_list}, columns=['url'])

df.to_csv(r'home_link.csv')


