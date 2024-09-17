
import json

import requests
from bs4 import BeautifulSoup

url = "https://boards-api.greenhouse.io/v1/boards/spacex/jobs"

payload = ""
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.spacex.com',
    'priority': 'u=1, i',
    'referer': 'https://www.spacex.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
job_details = data['jobs']
jobs_list = []
for jobs in job_details:
    jobID = jobs["internal_job_id"]
    jobTitle = jobs['title']
    company = "SpaceX"
    jobLocation = jobs['location']['name']
    employmentType = jobs["metadata"][0]["value"]
    job_url = jobs['absolute_url']
    numberOfPositionsAvailable = data["meta"]['total']

    # Send a request to the job URL and parse the response
    job_data = requests.get(job_url)
    if job_data.status_code == 200:
        response = job_data.content
        soup = BeautifulSoup(response, 'html.parser')
        briefJobDescription = "SpaceX" + soup.text.split("SpaceX")[5].split("COMPENSATION")[0]
        briefJobDescription = briefJobDescription + "COMPENSATION" + soup.text.split("COMPENSATION")[1].split("Apply for this Job")[0]
        print(briefJobDescription)
        linkToApply = job_url + "#app"
        postedDate = jobs['updated_at']
        try:
            applicationProcessDescription = ""
        except Exception as e:
            print("fail")
        requiredSkills = ""
        companyLogoUrl = ("https://s2-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/071/500"
                          "/resized/SPACEX_LOGO_black2.png?1538526201")

        # Create a dictionary for the job
        job_dict = {
            "jobID": jobID,
            "jobTitle": jobTitle,
            "company": company,
            "jobLocation": jobLocation,
            "employmentType": employmentType,
            "briefJobDescription": briefJobDescription,
            "linkToApply": linkToApply,
            "postedDate": postedDate,
            "equalOpportunityStatement": "SpaceX is an Equal Opportunity Employer",
            "numberOfPositionsAvailable": numberOfPositionsAvailable,
            "companyLogoUrl": companyLogoUrl,
            "experienceLevel": "",
            "salaryRange": "",
            "responsibilities": "",
            "qualifications": "",
            "benefits": "",
            "applicationDeadline": "",
            "remoteOption": "",
            "companyProfile": "",
            "jobFunction": "",
            "workSchedule": "",
            "applicationProcessDescription": "",
            "requiredSkills": "",
            "preferredSkills": [],
            "careerGrowthOpportunities": "",
            "companyCulture": "",
            "companyBenefitsLink": ""

        }

        # Append the job dictionary to the jobs_list
        jobs_list.append(job_dict)

# Convert the list of jobs to JSON
jobs_json = json.dumps(jobs_list, indent=4)

# Print or save the JSON object
print(jobs_json)
with open('spaceX_data.json', 'w') as json_file:
    json_file.write(jobs_json)