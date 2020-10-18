import selenium 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd 
import numpy as np 
import csv
import io
# driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
chrome_options = Options()
chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver = webdriver.Chrome(chrome_options=options)
# =============================================================================
# name = []
# price = []
# stars = []
# ratings = []
# description = []
# =============================================================================
with io.open('home_detail.csv','a', encoding="utf-8",newline='') as file:
    write = csv.writer(file, delimiter = ',' )
    with open('home_link.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        rows = list(readCSV)
        for row in rows[1:]:
            print(row[0])
            URL = row[1]
    
            driver.get(URL)
            line = []
            
            #GET NAME
            try:
                product_name = driver.find_element_by_class_name('prod-ProductTitle').text
                #print(product_name)
                line.append(product_name)
            except:
                continue
     
            #GET PRICE
            try:
                product_price = driver.find_element_by_class_name('price-group').text
                line.append(product_price)
                #print(product_price)
            except:
                line.append('null')
                #print("no price")
                
            #GET STARS
            try:
                product_stars = driver.find_element_by_class_name('ReviewsRating-rounded-overall').text
                line.append(product_stars)
                #print(product_stars)
            except:
                line.append('null')
                #print("no stars")
                
            #GET RATINGS
            try:
                product_ratings = driver.find_element_by_class_name('stars-reviews-count-node').text
                line.append(product_ratings)
                #print(product_ratings)
            except:
                line.append('null')
                #print("no ratings")  
                
            #DESCRIPTION
            try:
                product_description = driver.find_element_by_class_name('about-desc').text.split("\n")
                description_text = " ".join(product_description)
                line.append(description_text)
                #print(description_text)
            except:
                line.append('null')
                #print("no description")
            #print(line)
            write.writerow(line)
            
# =============================================================================
#         product_name = product.find_element_by_class_name('product-title-link').text
#         l1.append(product_name)
#         try: 
#             product_price = product.find_element_by_class_name('price-group').text
#             l2.append(product_price)
#             #print('null')
#         except: 
#             #print('No price')
#             price_element = "0.00"
#             product_price = 0.00
#             l2.append(product_price)
#             
#             # print(product_name)
#             # print(product_price)
# =============================================================================
        
# =============================================================================
#     df = pd.DataFrame({'Name': name, 'Price': price, 'Stars': stars, 'Rating':ratings, 'Description' : description}, columns=['Name', 'Price', 'Stars', 'Rating', 'Description'])
#         
#     df.to_csv(r'elec_prodcts_detail.csv')
# =============================================================================
