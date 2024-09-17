import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

jobs_list = []
for i in range(1, 5):

    url = f'https://atos.net/advancing-what-matters/en/join-us?showpage={i}'
    driver = webdriver.Chrome()
    driver.get(url)
    response = driver.page_source

    titles = driver.find_elements(By.XPATH, "//div/ul/li/div/h4")
    locations = driver.find_elements(By.XPATH, "//div/ul/li/div/p")
    get_dates = driver.find_elements(By.XPATH, "//div/div/ul/li/div/div")
    numberOfPositionsAvailable = driver.find_element(By.XPATH, "//div[2]/div[1]/span[3]").text.strip()

    soup = BeautifulSoup(response, 'html.parser')
    get_links = soup.find_all(class_="aj_atjob")

    for title, location, dates, links in zip(titles, locations, get_dates, get_links):
        job_dict = {
            'jobTitle': title.text.strip(),
            'jobLocation': location.text.strip(),
            'postedDate': dates.text.strip(),
            'link': links.find("div")['data-href'],
            'jobID': '',
            "company": "Atos",
            'employmentType': " ",
            'experienceLevel': " ",
            'salaryRange': " ",
            'responsibilities': " ",
            "qualifications": " ",
            "briefJobDescription": "",
            "linkToApply": "https://career5.successfactors.eu/careers?company=Atos",
            'applicationDeadline': " ",
            "remoteOption": " ",
            "companyProfile": " ",
            "jobFunction": " ",
            "applicationProcessDescription": " ",
            "equalOpportunityStatement": " ",
            "requiredSkills": " ",
            "preferredSkills": " ",
            "careerGrowthOpportunities": " ",
            "numberOfPositionsAvailable": numberOfPositionsAvailable,
            "companyCulture": " ",
            "companyBenefitsLink": " ",
            "companyLogoUrl": "https://atos.net/content/assets/global-images/atos-logo-blue-2023.svg"
        }
        jobs_list.append(job_dict)

    # Reuse the same browser instance for each job link
    new_driver = webdriver.Chrome()
    for job in jobs_list:
        new_driver.get(job['link'])
        try:
            job['jobID'] = new_driver.find_element(By.XPATH, "//div[3]/div/div/div/span[2]").text.strip()
            briefJobDescription_1 = new_driver.find_element(By.XPATH, "//div[6]").text.strip()
            briefJobDescription_2 = new_driver.find_element(By.XPATH, "//div[7]").text.strip()
            job['briefJobDescription'] = briefJobDescription_1 + ' ' + briefJobDescription_2
        except Exception as e:
            print(f"Error extracting additional details: {e}")
            continue

    # Close the browser instances after use
    driver.quit()
    new_driver.quit()

# Convert the combined job details to JSON
jobs_json = json.dumps(jobs_list, indent=4)

# Print or save the JSON object
with open('atos_jobs.json', 'w') as json_file:
    json_file.write(jobs_json)
