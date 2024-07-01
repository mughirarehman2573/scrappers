from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from datetime import datetime


# username_list = ["@esteelauder", "@bathandbodyworks", "@brilliantearth", "@costco", "@victoriassecret", "@walmart", "@clinique", "@maccosmetics", "@jomalonelondon", "@elfcostmetics", "@macys", "@ultabeauty", "@sephora", "@target", "@lawless", "@glossier", "@charlottetilbury"]
username_list = ["@esteelauder", "@bathandbodyworks"]
url = "https://www.tiktok.com/"
toq = open(f"{datetime.now().date()}-testing.csv", "a")
highest_view = open(f"{datetime.now().date()}-testing2.csv", "a")
toq.write("DateTime, User_Name, Following, Followers, Likes, Video_Views, Video_Links, Video_Text, \n")
highest_view.write("User_Name, Following, Followers, Likes, Video_Views, Video_Links, Video_Text, \n")

for i in username_list:
    link_list = []
    link_list.clear()
    text_list = []
    text_list.clear()
    ls = []
    ls.clear()
    video_views = []
    video_views.clear()
    new_csv_list = []
    new_csv_list.clear()
    try:
        toq.write(f"{datetime.now()}")
        response = requests.get(url + i)
        text = response.text.split('s222">')

        for j in text:
            if '<h2 data-e2e="user-subtitle"' in j:
                user_name = j.split("</h2><style data-emotion")[0].split('class="tiktok-1d3qdok')[1].split('">')[1].strip()
                toq.write(f",{user_name}")
                # highest_view.write(f"{user_name}")

            if "</div></div></a></div></div></div>" in j:
                views = j.split("</strong")[0]
                video_views.append(views)
                if 'href="" class="tiktok' in j:
                    text_data = j.split('<a title="')[1].split('" href')[0]
                    final_text = text_data.replace(",", ".").replace('&nbsp', " ")
                    text_list.append(final_text)
        time.sleep(4)
        driver = webdriver.Chrome()
        driver.get(url+i)
        time.sleep(5)
        quotes = driver.find_elements(By.XPATH, "//*[@id='main-content-others_homepage']/div/div[1]/h3/div")
        time.sleep(5)
        for quote in quotes:
            following = quote.find_element(By.XPATH, ".//strong").text
            following_text = quote.find_element(By.XPATH, ".//span").text
            final_following_text = following + " " + following_text
            print("FINAL : ", final_following_text)
            toq.write(f",{final_following_text}")
            # highest_view.write(f",{final_following_text}")
            ls.append(final_following_text)
        toq.write(f", \n")
        # highest_view.write(", \n")

        link_data = driver.find_elements(By.XPATH, "//*[@id='main-content-others_homepage']/div/div[2]/div[3]/div/div")
        time.sleep(2)

        for view, link, texts in zip(video_views, link_data, text_list):
            links = link.find_element(By.XPATH, ".//div[2]/a").get_attribute("href")
            link_list.append(links)

            toq.write(f",,,,,{view}, {links}, {texts} \n")

            if "K" in view:
                view = view.replace("K", "000").replace(".", "")
                new_csv_list.append([f"{view}", f"{links}", f"{texts}"])
            elif "M" in view:
                view = view.replace("M", "00000").replace(".", "")
                new_csv_list.append([f"{view}", f"{links}", f"{texts}"])
            else:
                new_csv_list.append([f"{view}", f"{links}", f"{texts}"])
        higher_view = sorted(new_csv_list, key=lambda x: int(x[0]), reverse=False)
        if higher_view[-1]:
            highest_view.write(f"{i}")
            for fol in ls:
                highest_view.write(f", {fol}")
        for top_view in higher_view[-1]:
            highest_view.write(f",{top_view}")
        highest_view.write("\n")

        driver.close()
    except Exception as e:
        print("THERE IS ISSUE : ", e)
