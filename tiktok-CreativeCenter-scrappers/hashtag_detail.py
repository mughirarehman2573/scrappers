import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")

# Replace this hashtag_list from newly printed hashtag extracted from hashtag_scrapper.py
hashtag_list = ['anguscloud', 'euphoria', 'longervideos', 'august', 'mondaymotivation', 'peeweeherman', 'firsttimehomebuyer', 'outdoor', 'astroworld', 'renovation', 'homedepot', 'goodomens', 'julydump', 'fezco', 'omgpage', 'timburton', 'diyhomeprojects', 'firsthome', 'paulreubens', 'outdoorlife']
toq = open("hashtag_detail-insights.csv", "a")
toq.write("Ranking , Hashtag,Posts last 7 days , overall posts, Views last 7 days, overall views, date, \n")
ranking = 0
for tags in hashtag_list:
    ranking +=1

    toq.write(f"{ranking}")
    url = f"https://ads.tiktok.com/business/creativecenter/hashtag/{tags}/pc/en?countryCode=US&period=7"
    print(tags)
    toq.write(f",{tags}")
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('span')
    post_7_days = paragraphs[37].get_text()
    toq.write(f",{post_7_days}")
    overall_posts = paragraphs[39].get_text()
    toq.write(f",{overall_posts}")
    Views_last_7_days = paragraphs[42].get_text()
    toq.write(f",{Views_last_7_days}")
    overall_views = paragraphs[44].get_text()
    toq.write(f",{overall_views}")
    toq.write(f",{formatted_datetime}")
    toq.write("\n")
