from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


#INPUT FROM USER
itemA = input("Enter item you want to search: ")

# OPEN AND INTERACT WITH THE SHOPEE WEBSITE
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.lazada.com.ph/")


#ENTER INPUT IN SEARCH BOX
search_box = driver.find_element_by_class_name('search-box__input--O34g')
search_box.send_keys(itemA)
search_box.send_keys(Keys.ENTER)
sleep(3)

nameContainer = []

#SCROLL DOWN SLOWLY
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 2):
    driver.execute_script("window.scrollTo(0, {});".format(i))

#BACK TO TOP
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
sleep(0.5)
driver.find_element_by_xpath('.//div[@class="index__filter-list___1Z8nj"]/div[6]/div[2]/div/ul').click()
sleep(0.5)
#GET DATA FROM WEBSITE INDIVIDUALLY
items = driver.find_elements_by_xpath('//*[@class="index__gridItem___3VkVO"]')

i = int(1)
counter = int(1)
for i in range(5):
        driver.find_element_by_xpath('.//*[@class="index__box___1Ffv-"]/div['+str(counter)+']').click() #open a selected product
        sleep(1)
        Name = driver.find_element_by_xpath('.//*[@id="module_product_title_1"]/div/div/h1').text
        Price = driver.find_element_by_xpath('.//*[@id="module_product_price_1"]/div/div/span').text
        Rating = driver.find_element_by_xpath('.//*[@id="module_product_review_star_1"]/div/a[1]').text
        link = driver.current_url
        try:
            Seller = driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
        except:
            Seller = '---NO SELLER---'
        try:
            img_div = driver.find_element_by_xpath('.//*[@name="og:image"]') #select image
            img_url = img_div.get_attribute("content") #save image and convert to text/link
        except:
            img_url = None

        print('Product Number:'+str(counter))
        print(Name)
        print(Price)
        print(Seller)
        print(Rating)
        print(link)
        print(img_url)
        print(' ')
        driver.back()
        sleep(3)
        counter=counter+1