import json

import requests

url = "https://boards-api.greenhouse.io/v1/boards/graphcore/departments"
jobs_list = []
payload = {}
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"1cb939f5c0e4c8742e3cc147c6d102c2"',
    'origin': 'https://www.graphcore.ai',
    'priority': 'u=1, i',
    'referer': 'https://www.graphcore.ai/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
department = data["departments"]
for data in department:
    get_job_details = data["jobs"]
    if len(get_job_details) > 0:
        job_link = get_job_details[0]["absolute_url"]
        jobTitle = get_job_details[0]["title"]
        jobLocation = get_job_details[0]["location"]['name']
        jobID = get_job_details[0]["id"]
        postedDate = get_job_details[0]['updated_at']
        linkToApply = job_link+"#app"
        get_job_details = requests.get(job_link)
        description = get_job_details.content
        briefJobDescription = get_job_details.text.split('<div id="content" class="">')[1].split("<div id='application'")[0]
        job_dict = {
            "jobID": jobID,
            "jobTitle": jobTitle,
            "company": "DataRobot",
            "jobLocation": jobLocation,
            "employmentType": " ",
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
            "numberOfPositionsAvailable": " ",
            "companyBenefitsLink": " ",
            "companyLogoUrl": ""
        }
        jobs_list.append(job_dict)
        print(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('graph-core.json', 'w') as json_file:
    json_file.write(jobs_json)



