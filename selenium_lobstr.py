from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
import time
from selenium.webdriver.chrome.options import Options


def lob_str_scraper():
    lobstr_csv = open('csv_files/lobstr.csv', 'w')
    lobstr_csv.write('Title_url, Title_text, Summary, Date_time, Read_time, \n')
    url = "https://lobstr.io/blog"
    for i in range(2, 7):
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(3)
        driver.refresh()
        time.sleep(12)

        data = driver.find_elements(By.XPATH, '//div[@class="post__Mirror__Background_Container m-p-lr-mpb"]')
        for post in data:
            title_anchor_tag = post.find_element(By.XPATH, './a[@href]')
            if title_anchor_tag:
                title_url = title_anchor_tag.get_attribute('href')
            title_text = post.find_element(By.XPATH, './a/div/p[1]').text.replace(',', '')
            summary = post.find_element(By.XPATH, './a/div/p[2]').text.replace(',', '')
            date_time_span = post.find_element(By.XPATH, './a/div/div/div/span').text
            if date_time_span:
                date_time = date_time_span.split('\n')[0].replace(',', '')
                read_time = date_time_span.split('\n')[1].replace(',', '')
            lobstr_csv.write(f"{title_url}, {title_text}, {summary}, {date_time}, {read_time}, \n")

            print("DATA : ", title_url, title_text, summary, date_time, read_time)
        url = f"https://lobstr.io/blog/page/{i}"


lob_str_scraper()
