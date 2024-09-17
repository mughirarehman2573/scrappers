import requests
import json

url = "https://automationanywhere.wd5.myworkdayjobs.com/wday/cxs/automationanywhere/AutomationAnywhereJobs/jobs"
job_links = []
jobs_list = []
for i in range(2):
    offset = i * 20

    payload = json.dumps({
        "appliedFacets": {},
        "limit": 20,
        "offset": offset,
        "searchText": ""
    })
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US',
        'content-type': 'application/json',
        'cookie': 'PLAY_SESSION=8f6665720148abc7c1ac0c711f41ce2756d0cab2-automationanywhere_pSessionId=6bfan9n437214tomo4pn60jsen&instance=vps-prod-ygk7bo04.prod-vps.pr501.cust.pdx.wd; wday_vps_cookie=1978309642.53810.0000; __cf_bm=8ztNH4xQzb8Bk5WNMye1_Maa34QLy01KerD7jdfekMQ-1725048786-1.0.1.1-97MhAi._64193DFHaJtkf9qGciUxlpR.q7U0uS2hgdKH2liDwqCJM3BRDTR6DAoiOH1EmkWMYOXzvZN47N0mXg; __cflb=02DiuHJZe28xXz6hQKLeTYyWYf7NxYcM1mBkwEGty9wCG; _cfuvid=qjll1tICxNCaEMaGARMwzO.4DoBZGAbsprH8wBUatIE-1725048786461-0.0.1.1-604800000; timezoneOffset=-300; CALYPSO_CSRF_TOKEN=153d06e9-5e55-413e-8323-f0136bc74e7c; PLAY_SESSION=8f6665720148abc7c1ac0c711f41ce2756d0cab2-automationanywhere_pSessionId=6bfan9n437214tomo4pn60jsen&instance=vps-prod-ygk7bo04.prod-vps.pr501.cust.pdx.wd; __cf_bm=tT2V3OR9dl1ggoISly7gIY8Wmo.8znaiOKTId_V9ZjI-1725049232-1.0.1.1-9jzrUDGwldj0BCj_3tFhJhdnN3TXpL2IzDROVuJXWM6thhy5lMerChy7YBsT0F3F9smuqJK43dEZbQrCZ7C90Q; _cfuvid=rTaQNwuu.1yn1CXaEyMzvv_aqubKfodwBk_xZIAc_9E-1725049232611-0.0.1.1-604800000; wd-browser-id=3b0ede3e-1f55-4624-8b57-0cd8a736def2; wday_vps_cookie=1978309642.53810.0000',
        'origin': 'https://automationanywhere.wd5.myworkdayjobs.com',
        'priority': 'u=1, i',
        'referer': 'https://automationanywhere.wd5.myworkdayjobs.com/AutomationAnywhereJobs',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-calypso-csrf-token': '153d06e9-5e55-413e-8323-f0136bc74e7c'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()
    jobs = data['jobPostings']
    print(data)
    for job in jobs:
        job_link = job["externalPath"]
        job_links.append(job_link)
print(job_links)
for job_link in job_links:
    url = f"https://automationanywhere.wd5.myworkdayjobs.com/wday/cxs/automationanywhere/AutomationAnywhereJobs{job_link}"

    payload = {}
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'PLAY_SESSION=8f6665720148abc7c1ac0c711f41ce2756d0cab2-automationanywhere_pSessionId=6bfan9n437214tomo4pn60jsen&instance=vps-prod-ygk7bo04.prod-vps.pr501.cust.pdx.wd; wday_vps_cookie=1978309642.53810.0000; __cf_bm=8ztNH4xQzb8Bk5WNMye1_Maa34QLy01KerD7jdfekMQ-1725048786-1.0.1.1-97MhAi._64193DFHaJtkf9qGciUxlpR.q7U0uS2hgdKH2liDwqCJM3BRDTR6DAoiOH1EmkWMYOXzvZN47N0mXg; __cflb=02DiuHJZe28xXz6hQKLeTYyWYf7NxYcM1mBkwEGty9wCG; _cfuvid=qjll1tICxNCaEMaGARMwzO.4DoBZGAbsprH8wBUatIE-1725048786461-0.0.1.1-604800000; timezoneOffset=-300; wd-browser-id=8dff6a2e-63ec-485f-a7eb-3ff4982827a7; CALYPSO_CSRF_TOKEN=4423592b-5756-4cad-a9d1-c314991b0df2; PLAY_SESSION=8f6665720148abc7c1ac0c711f41ce2756d0cab2-automationanywhere_pSessionId=6bfan9n437214tomo4pn60jsen&instance=vps-prod-ygk7bo04.prod-vps.pr501.cust.pdx.wd; __cf_bm=Mac7ubgf3VQLX.DkgdM0XPO9wnvNFx8u3EA3yz6hsJY-1725049080-1.0.1.1-.VhILtVCDizExBIpTJauKGnbi5Wt_N_w592leziqkZlw2_QSmI4F2quQxK7M9p4AC6LcOaJJ.QLKRarb69Clig; _cfuvid=jSPw.DZjOY4sNb.Fq6j2kTbmtSN..YoAngdJvoGI_.E-1725049080826-0.0.1.1-604800000; wd-browser-id=3b0ede3e-1f55-4624-8b57-0cd8a736def2; wday_vps_cookie=1978309642.53810.0000',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-calypso-csrf-token': '4423592b-5756-4cad-a9d1-c314991b0df2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    jobID = data["jobPostingInfo"]["jobReqId"]
    jobTitle = data["jobPostingInfo"]["title"]
    company = "automation-anywhere"
    jobLocation = data["jobPostingInfo"]["jobRequisitionLocation"]["country"]["descriptor"]
    employmentType = " "
    experienceLevel = " "
    salaryRange = " "
    responsibilities = " "
    qualifications = " "
    benefits = " "
    briefJobDescription = data["jobPostingInfo"]["jobDescription"]
    apply_id = data["jobPostingInfo"]["jobPostingId"] + "/apply"
    linkToApply = "https://automationanywhere.wd5.myworkdayjobs.com/en-US/AutomationAnywhereJobs/job/" + apply_id
    postedDate = data["jobPostingInfo"]["postedOn"]
    applicationDeadline = " "
    check_remote = data["jobPostingInfo"]['location']
    remoteOption = "Remote" in check_remote
    companyProfile = " "
    jobFunction = " "
    workSchedule = " "
    applicationProcessDescription = " "
    equalOpportunityStatement = " "
    requiredSkills = " "
    preferredSkills = " "
    careerGrowthOpportunities = " "
    companyCulture = " "
    numberOfPositionsAvailable = ""
    companyBenefitsLink = " "
    companyLogoUrl = "https://www.automationanywhere.com/sites/default/files/images/default-images/logo-aa-new.svg"
    job_dict = {
        "jobID": jobID,
        "jobTitle": jobTitle,
        "company": company,
        "jobLocation": jobLocation,
        "employmentType": employmentType,
        "briefJobDescription": briefJobDescription,
        "linkToApply": linkToApply,
        "experienceLevel": " ",
        "salaryRange": " ",
        "responsibilities": " ",
        "qualifications": " ",
        "benefits": " ",
        "postedDate": postedDate,
        "applicationDeadline": "",
        "remoteOption": remoteOption,
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
        "companyLogoUrl": "https://cdn.phenompeople.com/CareerConnectResources/TGPTGWGLOBAL/images"
                          "/Thales_LOGO_Pantone-1682075372118.png"
    }
    jobs_list.append(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('automation-anywhere.json', 'w') as json_file:
    json_file.write(jobs_json)
