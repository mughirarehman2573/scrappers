import json

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


base_url = "https://careers.thalesgroup.com/global/en/search-results?from={}&s=1"

# Calculate the number of pages
total_jobs = 2198
jobs_per_page = 10
total_pages = (total_jobs // jobs_per_page) + (1 if total_jobs % jobs_per_page else 0)

# Generate the list of URLs
urls = [base_url.format(page * jobs_per_page) for page in range(total_pages)]
jobs_list = []
job_link_list = []

for url in urls:
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    links = driver.find_elements(By.XPATH, "//span/a")
    postedDate = driver.find_elements(By.XPATH, "//li/div[1]/div[1]/p[1]/span[2]/span")
    jobID = driver.find_elements(By.XPATH, "//div[1]/p[1]/span[3]/span/span[2]")
    employmentType = driver.find_elements(By.XPATH, "//div[1]/p[1]/span[4]/span/span[2]")
    jobLocation = driver.find_elements(By.XPATH, "//div[1]/div[1]/p[1]/span[7]/span/span[2]")
    jobTitle = driver.find_elements(By.XPATH, "//div[1]/div[1]/span/a/div/span")
    numberOfPositionsAvailable = driver.find_element(By.XPATH, "//div/div/div/div[1]/div[1]/div[2]/div[1]/p/span[2]").text
    jobs_list = []
    job_link_list = []
    for link, date, job_id, emp_type, location, title in zip(links, postedDate, jobID, employmentType, jobLocation,
                                                         jobTitle):
        job_link = link.get_attribute('href')
        print(job_link)
        job_link_list.append(job_link)

        posted_date_text = date.text
        print(posted_date_text)
        job_id_text = job_id.text
        print(job_id_text)
        emp_type_text = emp_type.text
        print(emp_type_text)
        jobLocation = location.text
        print(jobLocation)
        title = title.text
        new_driver = webdriver.Chrome()

        new_driver.get(job_link)
        time.sleep(2)
        briefJobDescription = new_driver.find_element(By.XPATH,
                                                  "//div[2]/div[2]/div/div[1]/section/div/section[1]").text
        linkToApply = new_driver.find_element(By.XPATH, "//div[2]/div/div[1]/section/div/div[3]/a").get_attribute(
            "href")
        new_driver.quit()

        job_dict = {
            "jobID": job_id_text,
            "jobTitle":title,
            "company": "thalesgroup",
            "jobLocation": jobLocation,
            "employmentType": emp_type_text,
            "briefJobDescription": briefJobDescription,
            "linkToApply": linkToApply,
            "experienceLevel": " ",
            "salaryRange": " ",
            "responsibilities": " ",
            "qualifications": " ",
            "benefits": " ",
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
            "companyLogoUrl": "https://cdn.phenompeople.com/CareerConnectResources/TGPTGWGLOBAL/images/Thales_LOGO_Pantone-1682075372118.png"
        }
        jobs_list.append(job_dict)
        print(job_dict)

    jobs_json = json.dumps(jobs_list, indent=4)

    print(jobs_json)
    with open('thelasgroup.json', 'w') as json_file:
        json_file.write(jobs_json)