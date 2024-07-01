import csv

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

domain = 'https://remote.com/'
with open('1-remote-com-28-05-2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['job_link', 'Job Title', 'Company Name', 'Company Link', 'Job Description', 'work_place', 'location',
                  'job_type', 'salary','apply_now']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(2, 7):
        send_request = f'{domain}jobs/all?employmentType=full_time&country=GBR&page={i}'
        response = requests.get(send_request)
        soup = BeautifulSoup(response.content, 'html.parser')
        div_elements = soup.find_all('div', class_='sc-18d118e1-0 sc-39e987ab-0 lkAjHZ gmuqsn')
        for div_element in div_elements:
            get_a_tags = div_element.find_all('a')
            for tag in get_a_tags:
                job_link = tag.get('href')
                print(job_link)
                job_title = tag.get_text()
                print(job_title)

                hit_job = requests.get(domain + job_link)
                job_soup = BeautifulSoup(hit_job.content, 'html.parser')
                company_name = job_soup.find('span', class_='sc-7b9b9acb-0 epkbnY').text
                print(company_name)
                company_link = job_soup.find('a', class_="sc-aa54dee-8 kGeUTm sc-e8382fa-0 bGMmKZ").get('href')
                print(company_link)

                driver = webdriver.Chrome()
                driver.get(domain + job_link)
                time.sleep(3)
                job_description = driver.find_element(By.XPATH, '//section/div/div/div').text
                print(job_description)
                work_place = driver.find_element(By.XPATH, '//aside[1]/div/div/div[2]/div/dl/div[1]/dd/span').text
                print(work_place)
                location = driver.find_element(By.XPATH, '//aside[1]/div/div/div[2]/div/dl/div[2]/dd/span').text
                print(location)
                job_type = driver.find_element(By.XPATH, '//aside[1]/div/div/div[2]/div/dl/div[3]/dd/span').text
                pay = driver.find_element(By.XPATH, '//aside[1]/div/div/div[2]/div/dl/div[4]').text
                apply_now = driver.find_element(By.XPATH, '//div/div/div[1]/div[2]/div/div/a').get_attribute('href')

                if apply_now.__contains__('source'):
                    apply_now_link= apply_now.split("?")
                    apply_now_link=apply_now_link[0]
                if pay.startswith('Pay'):
                    salary = pay
                else:
                    salary = "N/A"

                writer.writerow({'job_link': domain + job_link,
                                 'Job Title': job_title,
                                 'Company Name': company_name,
                                 'Company Link': company_link,
                                 'Job Description': job_description,
                                 'work_place': work_place,
                                 'location': location,
                                 'job_type': job_type,
                                 'salary': salary,
                                 'apply_now': apply_now_link
                                 })
