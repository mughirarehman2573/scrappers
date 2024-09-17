import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://jobs.ashbyhq.com/Improbable"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
numberOfPositionsAvailable = \
driver.find_element(By.XPATH, "//div[2]/div[1]/h1/span").text.strip().split("(")[1].split(")")[0]
numberOfPositionsAvailable = int(numberOfPositionsAvailable)  # The number stored in the variable
links = driver.find_elements(By.CLASS_NAME, "_container_j2da7_1")
jobs_list = []
link_list = []
for link in links:
    link = link.get_attribute("href")
    link_list.append(link)
for job_link in link_list:
    jobID = job_link.split("/")[-1]
    driver.get(job_link)
    time.sleep(1)
    jobTitle = driver.find_element(By.XPATH, "//div[2]/div[1]/h1").text.strip()
    jobLocation = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/p").text.strip()
    employmentType = driver.find_element(By.XPATH, "//div/div[2]/div[2]/div[1]/div[2]/p").text.strip()
    briefJobDescription = driver.find_element(By.XPATH, "//div/div[2]/div[2]/div[2]/div").text.split("Life at Improbable")[0]
    companyCulture = "https://careers.improbable.io/life-at-improbable/"
    linkToApply = job_link + "/application"

    job_dict = {
        "jobID": jobID,
        "jobTitle": jobTitle,
        "company": "Improbable",
        "jobLocation": jobLocation,
        "employmentType": employmentType,
        "experienceLevel": " ",
        "salaryRange": " ",
        "responsibilities": " ",
        "qualifications": " ",
        "benefits": " ",
        "briefJobDescription": briefJobDescription,
        "linkToApply": linkToApply,
        "postedDate": "",
        "applicationDeadline": "",
        "remoteOption": "",
        "companyProfile": "",
        "jobFunction": "",
        "workSchedule": "",
        "applicationProcessDescription": " ",
        "equalOpportunityStatement": " ",
        "requiredSkills": " ",
        "preferredSkills": " ",
        "careerGrowthOpportunities": "",
        "companyCulture": "",
        "numberOfPositionsAvailable": numberOfPositionsAvailable,
        "companyBenefitsLink": " ",
        "companyLogoUrl": "https://app.ashbyhq.com/api/images/org-theme-wordmark/f698322b-efab-40b6-bbd1-64c4d8deeab5/6aa87c9e-462b-40dc-a56c-e864e05f9159.png"
    }

    jobs_list.append(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('Improbable.json', 'w') as json_file:
    json_file.write(jobs_json)
