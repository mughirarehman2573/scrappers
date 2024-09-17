import json

import requests
from bs4 import BeautifulSoup
response = requests.get('https://juvenescence.ca/careers')
jobs_list = []
soup = BeautifulSoup(response.content, 'html.parser')

get_job_link = soup.find_all("a")

for link in get_job_link:
    if link.get('href'):
        jobTitle = link.text
        sort_link = link.get('href')
        jobID = sort_link.split('/')[-1]
        if sort_link.startswith('https'):
            get_details = requests.get(sort_link)
            detail_soup = BeautifulSoup(get_details.content, 'html.parser')
            employmentType = detail_soup.find_all("span")[3].text
            jobLocation = detail_soup.find_all("span")[5].text
            linkToApply = sort_link+"/apply"
            briefJobDescription = detail_soup.find_all('div')[11].text

            job_dict = {
                "jobID": jobID,
                "jobTitle": jobTitle,
                "company": "juvenescence",
                "jobLocation": jobLocation,
                "employmentType": employmentType,
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
                "numberOfPositionsAvailable": '1',
                "companyBenefitsLink": " ",
                "companyLogoUrl": "https://cdn.filestackcontent.com/GQxgNwdXQ43rLbPqH"
                                  "…11ab3a0dd44556468de10e07f794944fb429cf5c7fbd12120"
            }
            jobs_list.append(job_dict)
            break

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('juvenescence.json', 'w') as json_file:
    json_file.write(jobs_json)

