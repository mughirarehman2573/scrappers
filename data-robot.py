import json
import requests
response = requests.get('https://www.datarobot.com/careers/')
jobs_list = []
job_ids = response.text.split('JobRequisitionId')
numberOfPositionsAvailable = len(job_ids)-1
for ids in job_ids[1:]:
    jobID = ids.split('"')[2]
    briefJobDescription = ids.split("<b>Job Description:<\/b>")[1].split("All applicant data submitted is handled in "
                                                                         "accordance with our ")[0]
    linkToApply = ids.split("apply_url")[1].split(',"title":')[0].split('":"')[1]
    jobLocation = ids.split('AdditonalLoc":"')[1].split('","')[0]
    jobTitle = ids.split("title")[1].split('","')[0].split('":"')[1]
    job_dict = {
        "jobID": jobID,
        "jobTitle": jobTitle,
        "company": "DataRobot",
        "jobLocation": jobLocation,
        "employmentType":  " ",
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
        "companyLogoUrl": "https://datarobot.wd1.myworkdayjobs.com/DataRobot_External_Careers/assets/logo"
    }
    jobs_list.append(job_dict)
    print(job_dict)

jobs_json = json.dumps(jobs_list, indent=4)

print(jobs_json)
with open('data-robot.json', 'w') as json_file:
    json_file.write(jobs_json)

