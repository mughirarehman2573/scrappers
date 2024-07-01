import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://stats-api.sportsnet.ca/ticker?league=mlb&day=2024-06-17"

payload = {}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.sportsnet.ca',
    'priority': 'u=1, i',
    'referer': 'https://www.sportsnet.ca/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = (response.json())
link_ids = [game['id'] for game in json_data['data']['games']]
for ids in link_ids:
    link = f"https://www.sportsnet.ca/baseball/mlb/games/{ids}/"
    print(link)

    driver = webdriver.Chrome()
    driver.get(link)
    print("Game link ", link)
    first_team_name = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[1]/div/div').text
    print("First team", first_team_name)
    second_team_name = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[1]/div/div').text
    print("Second team", second_team_name)
    tm_1 = [driver.find_element(By.XPATH, f'//section/div[1]/div/div[2]/div[2]/div[{i}]').text for i in range(1, 10)]
    tm_2 = [driver.find_element(By.XPATH, f'//section/div[1]/div/div[3]/div[2]/div[{i}]').text for i in range(1, 10)]

    for i in range(9):
        print(f"tm_1_{i + 1}", tm_1[i])
        print(f"tm_2_{i + 1}", tm_2[i])
    # tm_1_1= driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[1]').text
    # print("TM 1 1", tm_1_1)
    # tm_1_2= driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[2]').text
    # print("TM 1 2", tm_1_2)
    # tm_1_3= driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[3]').text
    # print("TM 1 3", tm_1_3)
    # tm_1_4= driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[4]').text
    # print("tm_1 4", tm_1_4)
    # tm_1_5 = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[5]').text
    # print("tm_1 5", tm_1_5)
    # tm_1_6 = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[6]').text
    # print("tm_1 6", tm_1_6)
    # tm_1_7 = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[7]').text
    # print("tm_1 7", tm_1_7)
    # tm_1_8 = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[8]').text
    # print("tm_1 8", tm_1_8)
    # tm_1_9 = driver.find_element(By.XPATH, '//section/div[1]/div/div[2]/div[2]/div[9]').text
    # print("tm_1 9", tm_1_9)
    # tm_2_1 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[1]').text
    # print("tm_2_1", tm_2_1)
    # tm_2_2 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[2]').text
    # print("tm_2_2", tm_2_2)
    # tm_2_3 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[3]').text
    # print("tm_2_3", tm_2_3)
    # tm_2_4 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[4]').text
    # print("tm_2_4", tm_2_4)
    # tm_2_5 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[5]').text
    # print("tm_2_5", tm_2_5)
    # tm_2_6 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[6]').text
    # print("tm_2_6", tm_2_6)
    # tm_2_7 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[7]').text
    # print("tm_2_7", tm_2_7)
    # tm_2_8 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[8]').text
    # print("tm_2_8", tm_2_8)
    # tm_2_9 = driver.find_element(By.XPATH, '//section/div[1]/div/div[3]/div[2]/div[9]').text
    # print("tm_2_9", tm_2_9)

    try:
        # Wait for the element to be clickable (if necessary)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class, "Tabs-module_tab__LYqhc") and contains(text(), "Boxscore")]'))
        )

        # Click on the element
        element.click()

    first_pitcher_name = driver.find_element(By.XPATH, '//div/div[4]/div[2]/div[4]/div[2]/div/div[10]/div/div[1]/div[2]')
        print("test")

    except Exception as e:
        print(e)
