import json

import requests

jobs_list = []

for i in range(1,10):
    url = f"https://careers.uipath.com/api/jobs?page={i}&sortBy=relevance&descending=false&internal=false&deviceId=undefined&domain=uipath.jibeapply.com"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '__cf_bm=TkxKlfNJ5ue3ujzbYhsXAjOXdr_I9E8kpO5olvPTWnM-1725045077-1.0.1.1-r6C_gRC0PnleOGULJvDVZ8_11DLiFBQ2TycQ98ruHUcpONP3Y.EUm36hDJfjM2iwJHNqzHeQz2QSRuAq.JhRXQ; _cfuvid=KcyxD5biVNF7DVVtbeN2N0M8GAYLvUYrH8opUQlEzbc-1725045077534-0.0.1.1-604800000; locale-prod=en-US; optimizelyEndUserId=oeu1725045080831r0.8436469403419056; i18n=en-US; searchSource=external; session_id=ce964e39-84d7-478f-876e-c6b719e3848f; jrasession=12f7954a-a106-4a5c-9eec-6416c6ea0483; jasession=s%3Ayt_cmvPlNcdvngDrAxI5xtbX8OJNmWDb.t%2FuVfBEHvoZPcH7PH8X1bLI2MGVlgvJ16N0%2F9mbqT30; _janalytics_ses.9e71=*; _ga_D20QK619Y0=GS1.1.1725045093.1.0.1725045093.0.0.0; _gid=GA1.2.2034257159.1725045094; _gat_gtag_UA_35875149_15=1; _ga=GA1.1.2005899578.1725045094; _ga_TQ72BH8CSS=GS1.1.1725045093.1.0.1725045094.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Aug+31+2024+00%3A11%3A34+GMT%2B0500+(Pakistan+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f3d0f888-fe21-418a-8d14-a32f62d7c47f&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0005%3A0%2CC0004%3A0&AwaitingReconsent=false; _janalytics_id.9e71=0d93407f-c48d-433c-92c7-4134c696d8c5.1725045084.1.1725045094.1725045084.f179cac6-69aa-4e38-8477-754790191da8; jasession=s%3Ayt_cmvPlNcdvngDrAxI5xtbX8OJNmWDb.t%2FuVfBEHvoZPcH7PH8X1bLI2MGVlgvJ16N0%2F9mbqT30; jrasession=12f7954a-a106-4a5c-9eec-6416c6ea0483',
        'priority': 'u=1, i',
        'referer': 'https://careers.uipath.com/careers/jobs',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'session-id': 'f179cac6-69aa-4e38-8477-754790191da8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'user-id': '0d93407f-c48d-433c-92c7-4134c696d8c5'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    jobs_details = data["jobs"]
    numberOfPositionsAvailable = data["totalCount"]
    for job in jobs_details:
        jobID = job['data']['req_id']
        jobTitle = job['data']['title']
        jobLocation = job['data']["full_location"]
        employmentType = job['data']['employment_type']
        experienceLevel = " "
        salaryRange = " "
        responsibilities = job['data']['responsibilities']
        qualifications = job['data']['qualifications']
        benefits = " "
        briefJobDescription = job['data']['description']
        linkToApply = job['data']["apply_url"]
        postedDate = job['data']['posted_date']
        applicationDeadline = " "
        remoteOption = " "
        companyProfile = " "
        jobFunction = job['data']['categories'][0]['name']
        workSchedule = " "
        applicationProcessDescription = " "
        equalOpportunityStatement = " "
        requiredSkills = " "
        preferredSkills = " "
        careerGrowthOpportunities = " "
        companyCulture = " "
        numberOfPositionsAvailable = " "
        companyBenefitsLink = " "
        companyLogoUrl = job['data']["hiring_organization_logo"]
        job_dict = {
            "jobID": jobID,
            "jobTitle": jobTitle,
            "company": "thalesgroup",
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
            "numberOfPositionsAvailable": numberOfPositionsAvailable,
            "companyBenefitsLink": " ",
            "companyLogoUrl": companyLogoUrl
        }
        jobs_list.append(job_dict)
        print(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('ui-path.json', 'w') as json_file:
    json_file.write(jobs_json)