import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://www.mentorworks.ca/government-funding/"

driver = webdriver.Chrome()
chrome_options = Options()

# Your Selenium script here
driver.get(url)

grand_links = driver.find_elements(By.XPATH, "//td[4]/a")
regions = driver.find_elements(By.XPATH, "//td[2]")
short_descriptions = driver.find_elements(By.XPATH, "//td[3]")

# Create a CSV file and write headers
with open(f"grand-data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Funding program", "Grand link", "Region", "short Description", "Eligible Applicants", "Eligible Activities",
         "Long Description",
         "average_approval_rate", "deadline", "title"])

    sub_driver = webdriver.Chrome()
    # Write data rows
    for link, region, short_description in zip(grand_links, regions, short_descriptions):
        link = link.get_attribute("href")
        region = region.text
        short_description = short_description.text
        sub_driver.get(link)
        date_pattern = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}"

        try:
            deadlines = sub_driver.find_elements(By.XPATH, "//div[2]/div[1]/div/p")
            element = sub_driver.find_element(By.XPATH, "//body")
            title = element.text.split("\n")[10]
        except:
            title = "N/A"

        try:
            deadlines = sub_driver.find_elements(By.XPATH, "//div[2]/div[1]/div/p")
            element = sub_driver.find_element(By.XPATH, "//body")
            date_text = element.text.split("Program Deadline")[1].split("Apply for Funding")[0]
            deadline = date_text.strip()
        except:
            deadline = "N/A"
            print("No Subject Found")
        try:
            average_approval_rate = \
                sub_driver.find_elements(By.XPATH, "//*[@id='apply']/div[3]/div[2]")[0].text.strip().split("an")[
                    2].split(
                    "%")[0]
            average_approval_rate = average_approval_rate + "%"

        except:

            average_approval_rate = "N/A"
            print("No approval rate")
        try:
            funding_program = element.text.split("Do I Qualify?")[1].split("\n")[1]
        except:
            funding_program = "N/A"
        try:

            eligible_applicants = sub_driver.find_element(By.XPATH,
                                                          "//*[@id='kt-layout-id_a4e929-56']/div[2]/div[1]/div/ul")
            print("Eligible Applicants:", eligible_applicants.text)
            eligible_applicants = eligible_applicants.text

        except:
            try:
                eligible_applicants = sub_driver.find_element(By.XPATH, "//*[@id='kt-layout-id_a4e929-56']/div[2]/div["
                                                                        "1]/div/p")
                eligible_applicants = eligible_applicants.text

            except:
                try:
                    eligible_applicants = sub_driver.find_element(By.XPATH, "//*[@id='eligible-applicants']/div[3]/div["
                                                                            "1]/div/ul")
                    eligible_applicants = eligible_applicants.text
                except:
                    try:
                        eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                      "//*[@id='eligible-applicants']/div[3]/div[1]/div/ul")
                        eligible_applicants = eligible_applicants.text
                    except:
                        try:
                            eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                          "//*[@id='kt-info-box_8e030a-93']/div/div[2]/p")
                            eligible_applicants = eligible_applicants.text

                        except:
                            try:
                                eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                              "//*[@id='kt-info-box_cdcfa6-40']/div/div[2]/p")
                                eligible_applicants = eligible_applicants.text


                            except:
                                try:
                                    eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                                  "//*[@id='kt-layout-id_8c0227-65']/div[2]/div[1]").text.split(
                                        "Applicants")[1].strip()
                                except:

                                    try:
                                        eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                                      "//*[@id='kt-layout-id_0992df-c3']/div/div/div/p")
                                        eligible_applicants = eligible_applicants.text
                                    except:
                                        try:
                                            eligible_applicants = sub_driver.find_element(By.XPATH,
                                                                                          "//*[@id='post-7072']/div/div/div[2]/div/div/div/p")
                                            eligible_applicants = eligible_applicants.text
                                        except:
                                            print("Eligible_applicants not found")
                                            eligible_applicants = "N/A"
                                            pass

        try:
            eligible_activities = sub_driver.find_element(By.XPATH,
                                                          "//*[@id='kt-layout-id_45e28a-b9']/div[2]/div[1]/div/ul")
            eligible_activities = eligible_activities.text


        except:
            try:
                eligible_activities = sub_driver.find_element(By.XPATH,
                                                              "//*[@id='kt-layout-id_45e28a-b9']/div[2]/div[1]/div/p")
                eligible_activities = eligible_activities.text
            except:
                try:
                    eligible_activities = sub_driver.find_element(By.XPATH,
                                                                  "//*[@id='eligible-activities']/div[3]/div[1]/div/ul")
                    eligible_activities = eligible_activities.text
                except:
                    try:
                        eligible_activities = sub_driver.find_element(By.XPATH,
                                                                      "//*[@id='kt-info-box_afe34d-81']/div/div[2]/p")
                        eligible_activities = eligible_activities.text


                    except:
                        try:
                            eligible_activities = sub_driver.find_element(By.XPATH,
                                                                          "//*[@id='kt-layout-id_ed986d-ef']/div[2]/div[1]/div").text.split(
                                "Activities")[1].strip()

                        except:

                            try:
                                eligible_activities = sub_driver.find_element(By.XPATH,
                                                                              "//*[@id='kt-info-box_e0afb6-be']/a/div[2]/p")
                            except:

                                print("Eligible_activities :not found")
                                eligible_activities = "N/A"
                                pass
        element = sub_driver.find_element(By.XPATH, "//body")
        class_attribute = element.get_attribute("class")
        try:
            id_value = class_attribute.split("page-id-")[1].split(" ")[0]
        except:
            print("no-id value found")
            pass

        try:
            long_description = sub_driver.find_element(By.XPATH, "//*[@id='kt-layout-id_0992df-c3']/div/div/div/p")
            long_description = long_description.text
        except:
            try:
                long_description = sub_driver.find_element(By.XPATH,
                                                           f"//*[@id='post-{id_value}']/div/div/div[2]/div/div/div/p")
                long_description = long_description.text
            except:
                try:
                    long_description = sub_driver.find_element(By.XPATH,
                                                               f"//*[@id='kt-layout-id_e8c612-01']/div/div/div/p")
                    long_description = long_description.text
                except:

                    try:
                        long_description = sub_driver.find_element(By.XPATH,
                                                                   f"//*[@id='kt-layout-id_2854f0-3b']/div/div/div/p[1]")
                        long_description = long_description.text

                    except:
                        try:
                            long_description = sub_driver.find_element(By.XPATH,
                                                                       f"//*[@id='post-{id_value}']/div/div/div[2]/div/div/div/div/div/div[1]/div/p")
                            long_description = long_description.text
                        except:
                            try:
                                long_description = sub_driver.find_element(By.XPATH,
                                                                           "//*[@id='post-269555']/div/div/div[2]/div/div/div/p")
                                long_description = long_description.text
                            except:
                                try:
                                    long_description = sub_driver.find_element(By.XPATH,
                                                                               "//*[@id='post-7391']/div/div/div[2]/div/div/div/p")
                                    long_description = long_description.text
                                except:
                                    try:
                                        long_description = sub_driver.find_element(By.XPATH,
                                                                                   "//*[@id='post-268850']/div/div/div[2]/div/div/div/p")
                                        long_description = long_description.text
                                    except:
                                        print("Something went wrong")
                                        long_description = "N/A"
                                        pass
        writer.writerow([funding_program, link, region, short_description, eligible_applicants, eligible_activities,
                         long_description,
                         average_approval_rate, deadline, title])

print("CSV file generated successfully.")
