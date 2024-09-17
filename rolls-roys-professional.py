import requests
import json

urls = ["https://rollsroyce.wd3.myworkdayjobs.com/wday/cxs/rollsroyce/professional/jobs"]
jobs_list = []

for offset in range(0, 181, 20):
    print(offset)# Loop through offsets: 0, 20, 40, ..., 180
    for url in urls:
        extension = "https://rollsroyce.wd3.myworkdayjobs.com/wday/cxs/rollsroyce/Apprentice"

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
            'cookie': 'PLAY_SESSION=3000bd64ead8bd17a463deeb662ffbed9d98ef99-rollsroyce_pSessionId=57acnk62c2fjfso95b4eol7tkd&instance=vps-prod-pgk6d0rs.prod-vps.pr501.cust.dub.wd; wday_vps_cookie=2606274826.53810.0000; __cf_bm=GP0h3dsn8K12t3YuRS7wEVQAcPC5Aukz1BQ3bqMSEpA-1724957706-1.0.1.1-LlrCRVELvw6kCwzWfBJKoyx1R8EEg8AuPlLYGJYrE9QQXHagEG_mIEr2iITPU5P50K_RZvV5UFHC4abscTe_mg; __cflb=02DiuJFb1a2FCfph91mEfCE19uWmaV9PEbEQMqecbbaya; _cfuvid=PmUP38FwPunlcjG8PbTbHk27KQEnj3VQ7F7umRi2kgM-1724957706940-0.0.1.1-604800000; timezoneOffset=-300; enablePrivacyTracking=true; _ga=GA1.4.20424242.1724957757; _gat=1; wd-browser-id=3c4e8891-e393-4269-97e1-cf83950b0222; CALYPSO_CSRF_TOKEN=42e1e80c-1996-443f-b931-73dc4ebf19c5; PLAY_SESSION=3000bd64ead8bd17a463deeb662ffbed9d98ef99-rollsroyce_pSessionId=57acnk62c2fjfso95b4eol7tkd&instance=vps-prod-pgk6d0rs.prod-vps.pr501.cust.dub.wd; wday_vps_cookie=2606274826.53810.0000',
            'origin': 'https://rollsroyce.wd3.myworkdayjobs.com',
            'priority': 'u=1, i',
            'referer': 'https://rollsroyce.wd3.myworkdayjobs.com/Apprentice',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-calypso-csrf-token': '42e1e80c-1996-443f-b931-73dc4ebf19c5'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        print(data)
        get_links = data['jobPostings']
        available_positions = len(get_links)

        for sub_links in get_links:
            link = sub_links['externalPath']
            job_link = extension + link
            payload = {}
            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US',
                'priority': 'u=1, i',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                'x-calypso-csrf-token': 'b11acd8a-d8f1-4bd8-9788-9a8370371945'
            }

            response = requests.request("GET", job_link, headers=headers, data=payload)

            data = response.json()
            print(data)
            job_dict = {
                'jobID': data['jobPostingInfo']['id'],
                'jobTitle': data['jobPostingInfo']['title'],
                "company": 'rollsroyce',
                'jobLocation': data['jobPostingInfo']['jobRequisitionLocation']['country']['descriptor'],
                'employmentType': data['jobPostingInfo']['timeType'],
                'experienceLevel': " ",
                'salaryRange': " ",
                'responsibilities': " ",
                "qualifications": " ",
                "briefJobDescription": data['jobPostingInfo']['jobDescription'],
                "linkToApply": "https://rollsroyce.wd3.myworkdayjobs.com/en-US/Apprentice/login",
                "postedDate": data['jobPostingInfo']['postedOn'],
                'applicationDeadline': data['jobPostingInfo']['startDate'],
                "remoteOption": " ",
                "companyProfile": " ",
                "jobFunction": " ",
                "applicationProcessDescription": " ",
                "equalOpportunityStatement": " ",
                "requiredSkills": " ",
                "preferredSkills": " ",
                "careerGrowthOpportunities": " ",
                "numberOfPositionsAvailable": available_positions,
                "companyCulture": " ",
                "companyBenefitsLink": " ",
                "companyLogoUrl": "https://rollsroyce.wd3.myworkdayjobs.com/Apprentice/assets/logo"
            }
            jobs_list.append(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

# Print or save the JSON object
print(jobs_json)
with open('rolls-royce-professional.json', 'w') as json_file:
    json_file.write(jobs_json)
