import json

import requests
from bs4 import BeautifulSoup
response = requests.get('https://jobs.sanofi.com/en/search-jobs')
base_url = "https://jobs.sanofi.com/"

soup = BeautifulSoup(response.content, 'html.parser')
jobs_list = []
for i in range(32,47):
    get_link = soup.find_all("a")[i]
    link = get_link.get("href")
    print(link)
    job_details = base_url+link
    response = requests.get(job_details)
    job_soup = BeautifulSoup(response.content, 'html.parser')
    jobID = link.split('/')[-1]
    jobTitle = job_soup.find("h1").text.strip()
    jobLocation = job_soup.find(class_="job-location job-info").text.strip()
    employmentType = job_soup.find(class_="job-type job-info").text.strip()
    postedDate = job_soup.find(class_="job-date job-info").text.strip()
    linkToApply = job_soup.find(class_="button job-apply bottom").get('href')
    briefJobDescription = job_soup.find(class_="section7-second").text.split("Apply Now")[0].strip()
    job_dict = {
        'jobID': jobID,
        'jobTitle': jobTitle,
        "company": "snofi",
        'jobLocation': jobLocation,
        'employmentType': employmentType,
        'experienceLevel': " ",
        'salaryRange': " ",
        'responsibilities': " ",
        "qualifications": " ",
        "briefJobDescription": briefJobDescription,
        "linkToApply": linkToApply,
        "postedDate": postedDate,
        'applicationDeadline': " ",
        "remoteOption": " ",
        "companyProfile": " ",
        "jobFunction": " ",
        "applicationProcessDescription": " ",
        "equalOpportunityStatement": " ",
        "requiredSkills": " ",
        "preferredSkills": " ",
        "careerGrowthOpportunities": " ",
        "numberOfPositionsAvailable": " ",
        "companyCulture": " ",
        "companyBenefitsLink": " ",
        "companyLogoUrl": "https://cdn.radancy.eu/company/2649/img/logo/sanofi_logo.svg"
    }
    jobs_list.append(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

# Print or save the JSON object
with open('snofi.json', 'w') as json_file:
    json_file.write(jobs_json)
