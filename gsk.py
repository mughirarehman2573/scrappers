import json

import requests
jobs_list = []
for i in range(1, 12):

    url = f"https://jobs.gsk.com/api/jobs?limit=100&page={i}&lang=en-GB&sortBy=relevance&descending=false&internal=false"
    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'searchSource=external; diversificationLevel=SIMPLE; session_id=6dd8501c-e597-494c-bec4-79322e5bcc80; jrasession=23cf2f7d-e8f7-49ca-97e8-63c6ad004807; jasession=s%3AXiu38BOptahkcvWXUypo1drFVahcihrS.O6yv5yio2bBKeq13Lvcz1%2FaKDg2LUvO9Sipnh5h%2FA%2Fs; _janalytics_ses.06c1=*; _gid=GA1.2.358867002.1724990584; _janalytics_id.06c1=560d2707-a1e0-4cb0-b191-eb647b7a4d96.1724990579.1.1724992191.1724990579.02e73342-4e31-4b1a-a80b-37df100fcd70; i18n=en-GB; _ga_5Y2BYGL910=GS1.1.1724990584.1.1.1724992283.60.0.0; _ga_D20QK619Y0=GS1.1.1724990583.1.1.1724992285.0.0.0; _gat_gtag_UA_35875149_15=1; _gat_UA-35875149-10=1; _ga_TQ72BH8CSS=GS1.1.1724990584.1.1.1724992285.0.0.0; _ga=GA1.1.1667114460.1724990584; jasession=s%3AXiu38BOptahkcvWXUypo1drFVahcihrS.O6yv5yio2bBKeq13Lvcz1%2FaKDg2LUvO9Sipnh5h%2FA%2Fs; jrasession=23cf2f7d-e8f7-49ca-97e8-63c6ad004807',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    data = response.json()
    get_job_data = data["jobs"]
    numberOfPositionsAvailable = data["totalCount"]

    for data in get_job_data:
        jobID = data['data']["slug"]
        jobTitle = data['data']["title"]
        company = "GSK"
        jobLocation = data["data"]["full_location"]
        employmentType = data["data"]["employment_type"]
        experienceLevel = " "
        salaryRange = " "
        responsibilities = " "
        qualifications = " "
        benefits = " "
        briefJobDescription = data["data"]["description"]
        linkToApply = data["data"]["apply_url"]
        postedDate = data["data"]["create_date"]
        applicationDeadline = " "
        remoteOption = " "
        companyProfile = " "
        jobFunction = " "
        workSchedule = " "
        applicationProcessDescription = " "
        equalOpportunityStatement = " "
        requiredSkills = " "
        preferredSkills = " "
        careerGrowthOpportunities = " "
        companyCulture = " "
        print(data)
        job_dict = {
            'jobID': jobID,
            'jobTitle': jobTitle,
            "company": company,
            'jobLocation': jobLocation,
            'employmentType': employmentType,
            'experienceLevel': " ",
            'salaryRange': " ",
            'responsibilities': " ",
            "qualifications": " ",
            "briefJobDescription": briefJobDescription,
            "linkToApply": linkToApply,
            "postedDate": postedDate,
            'applicationDeadline': applicationDeadline,
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
            "companyLogoUrl": "https://rollsroyce.wd3.myworkdayjobs.com/Apprentice/assets/logo"
        }
        jobs_list.append(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

# Print or save the JSON object
with open('gsk.json', 'w') as json_file:
    json_file.write(jobs_json)
