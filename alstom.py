import json

import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.expected_conditions import element_located_to_be_selected

url = "https://jobsearch.alstom.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_country=&optionsFacetsDD_department=&optionsFacetsDD_shifttype="

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'JSESSIONID=w7~AF515D9C928B222C8185A0E30DCC4409; _pk_ses.c7074d61-f54b-4894-a606-a511843dc124.f12f=*; _pk_id.c7074d61-f54b-4894-a606-a511843dc124.f12f=cb2423d85759122c.1724966560.1.1724968379.1724966560.',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = bs(response.text, "xml")
company_logo = "https://rmkcdn.successfactors.com/44ea18da/ff6f3396-32e1-421d-915a-5.jpg"
job_data = soup.find_all("tr", class_='data-row')
ls = []
domain = "https://jobsearch.alstom.com/"
for link in job_data:
    data_dict = {}
    data_dict["companyLogoUrl"] = company_logo
    job_link = f'{domain}{link.find("a", class_="jobTitle-link").get("href")}'
    data_dict["linkToApply"] = job_link
    data_dict["JobID"] = link.find("a", class_="jobTitle-link").get("href").split('/')[-2]
    data_dict["jobTitle"] = link.find("a", class_="jobTitle-link").text.replace('\n', '').replace('\t', '').strip()
    data_dict["jobLocation"] = link.find("span", class_='jobLocation').text.replace('\n', '').replace('\t', '').strip()
    data_dict["employmentType"] = link.find("span", class_='jobDepartment').text if link.find("span", class_='jobDepartment') else " "
    data_dict["experienceLevel"] = link.find("span", class_='jobShifttype').text if link.find("span", class_='jobShifttype') else " "
    data_dict["postedDate"] = link.find("span", class_='jobDate').text.replace('\n', '').replace('\t', '').strip() if link.find("span", class_='jobDate') else " "
    request_url = requests.get(job_link)
    soup = bs(request_url.text, "xml")
    company = soup.find("p", class_="jobCompany").find('span').text.strip() if soup.find("p", class_="jobCompany") else " "
    data_dict["company"] = company
    data_dict["job_description"] = soup.find("div", class_="jobDescription").text if soup.find("div", class_="jobDescription") else " "
    data_dict["equalOpportunityStatement"] = f"{company} is an Equal Opportunity Employer"
    data_dict["responsibilities"] = soup.find("div", class_="jobDescription").find("p", class_="jobDescription").text if soup.find("div", class_="jobDescription") else " "
    data_dict["qualifications"] = soup.find("div", class_="jobQualification").text if soup.find("div", class_="jobQualification") else " "
    data_dict["benefits"] = soup.find("div", class_="jobBenefits").text if soup.find("div", class_="jobBenefits") else " "
    data_dict["applicationDeadline"] = soup.find("div", class_="jobDeadline").text if soup.find("div", class_="jobDeadline") else " "
    data_dict["remoteOption"] = soup.find("div", class_="jobOptions").text if soup.find("div", class_="jobOptions") else " "
    data_dict["companyProfile"] = soup.find("div", class_="jobProfile").text if soup.find("div", class_="jobProfile") else " "
    data_dict["jobFunction"] = soup.find("div", class_="jobFunction").text if soup.find("div", class_="jobFunction") else " "
    data_dict["workSchedule"] = soup.find("div", class_="jobSchedule").text if soup.find("div", class_="jobSchedule") else " "
    data_dict["applicationProcessDescription"] = soup.find("div", class_="jobProcessDescription").text if soup.find("div", class_="jobProcessDescription") else " "
    data_dict["requiredSkills"] = soup.find("div", class_="jobRequiredSkills").text if soup.find("div", class_="jobRequiredSkills") else " "
    data_dict["preferredSkills"] = soup.find("div", class_="jobPreferredSkills").text if soup.find("div", class_="jobPreferredSkills") else " "
    data_dict["careerGrowthOpportunities"] = soup.find("div", class_="careerGrowthOpportunities").text if soup.find("div", class_="careerGrowthOpportunities") else " "
    data_dict["companyCulture"] = soup.find("div", class_="jobCulture").text if soup.find("div", class_="jobCulture") else " "
    data_dict["companyBenefitsLink"] = soup.find("div", class_="jobBenefits").find("a").get("href") if soup.find("div", class_="jobBenefits") else " "

    ls.append(data_dict)

with open("alstom.json", "w") as file:
    file.write(json.dumps(ls, indent=4))
print(ls)
