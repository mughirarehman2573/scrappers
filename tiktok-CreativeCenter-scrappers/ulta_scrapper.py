
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime


toq = open("ulta-store.csv", "a")

toq.write('Links, Store_Name, Store_Phone, Store_Address, Store_Time, \n')
url = 'https://www.ulta.com/stores/directory'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)
link_list = []

quotes = driver.find_elements(By.XPATH, '//*[@id="sls-app"]/div/div/div/div/div/div[2]/div')
for quote in quotes[11::]:
    try:
        find_links = quote.find_elements(By.XPATH, './/div/div')
        for link in find_links:
            try:
                links = link.find_element(By.XPATH, './/a[@href]').get_attribute('href')
                # toq.write(f'{links}')
                browser = webdriver.Chrome()
                if "http" not in links:
                    links = "https://www.ulta.com/stores" + links

                browser.get(links)
                time.sleep(5)

                store_name = browser.find_element(By.XPATH, '//*[@id="sls-location-details-container"]/div/div[1]/h1').text.replace(',', ' ')
                store_phone = browser.find_element(By.XPATH, '//*[@id="sls-location-details-container"]/div/div[3]/a').text.replace(',', ' ')
                store_address = browser.find_element(By.XPATH, '//*[@id="sls-location-details-container"]/div/div[2]/div').text.replace("\n", ' ').replace(',', ' ')
                store_time = browser.find_element(By.XPATH, '//*[@id="sls-location-details-container"]/div/span/span').text.replace(',', ' ')
                toq.write(f'{links}, {store_name}, {store_phone}, {store_address}, {store_time}, \n')
                link_list.append([links, store_name, store_phone, store_address, store_time])
                browser.close()

                print(links, store_time, store_address, store_phone, store_name)
            except Exception as e:
                print("THERE : ", e)
    except Exception as e:
        print("ERROR : ", e)