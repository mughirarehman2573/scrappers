import re

# Replace this part of code with new API extracted from Hashtag insights url.
import requests

url = "https://ads.tiktok.com/creative_radar_api/v1/popular_trend/hashtag/list?page=1&limit=20&period=7&country_code=US&sort_by=popular"

payload = {}
headers = {
  'authority': 'ads.tiktok.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'anonymous-user-id': '21487677-8062-4660-9864-5738cd0ccc72',
  'cookie': '_ttp=2T4rlZ40IgcYBfzZtDI8TKyAPrc; _ga=GA1.1.620795730.1690313524; tta_attr_id=0.1690364005.7260058121794486273; tta_attr_id_mirror=0.1690364005.7260058121794486273; _ga_HV1FL86553=GS1.1.1690364010.1.1.1690364579.60.0.0; lang_type=en; s_v_web_id=verify_lkk2w7p3_PDVQ3THI_JUp3_4rbA_8Qi3_opxvs9UPhsfk; tt_csrf_token=4kFsgG0t-FeoQsb3RHqax6ozV5Bc5QuuwMjU; tt_chain_token=TrcQFBt6NHYvC88Hkp7SaQ==; _ga_QQM0HPKD40=GS1.1.1691004433.31.1.1691005132.44.0.0; ttwid=1%7C3stDw9BWIZ6oZf6uf6dy4uX0UEKrp0L0oQWQWHDpd6g%7C1691005137%7C1caac3532a08c4cfd88feae56e5f2332f6bfa36eb43c3ac2b4ec84d5f84f088e; msToken=m8Vtnb1P2Gr27Y0nDhuPrKlferTlBa2C3HaZQDpwMMpvCbLhhAGYgMygwZdLA5onR7kDLB0HYUfM41C-XP0Th7OnWD9dRDWWyHl5ZKpTPxstSja5-pPLsnTxZQDgxH8=; msToken=m8Vtnb1P2Gr27Y0nDhuPrKlferTlBa2C3HaZQDpwMMpvCbLhhAGYgMygwZdLA5onR7kDLB0HYUfM41C-XP0Th7OnWD9dRDWWyHl5ZKpTPxstSja5-pPLsnTxZQDgxH8=; msToken=_zb8HWJVQlJcbqVVFLHLTsFUn2zlrNoMrMnxuU8lnakTTyvQy6d09AuUMgFoCmvcxdDPB-Ggv3G7bkPGI9PgWqTVGOKdHcwI4JHrqYzKxIcjOYIkxRSaUVTctleUV0trFb9Bm6GwnXw=',
  'lang': 'en',
  'referer': 'https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'timestamp': '1691005162',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  'user-sign': 'dc2e5ea4b16449af',
  'web-id': '7259841200039396866'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



# End point to replace the code.

toq = open("hashtag-insights.csv", "a")
toq.write("Rank,hashtag_name, video_views, post, \n")
json_data = response.json()
hashtags = []
req_id = json_data.get("data").get("list")
for i in req_id:
    rank = i.get("rank")
    toq.write(f"{rank}")
    hashtag_name_raw = i.get("hashtag_name")
    hashtag_name = re.sub(r'[^a-zA-Z\s]', '', hashtag_name_raw)
    toq.write(f",{hashtag_name}")
    hashtags.append(hashtag_name)
    video_views = i.get("video_views")
    toq.write(f",{video_views}")
    post = i.get("publish_cnt")
    toq.write(f",{post}")
    toq.write("\n")
print("hashtags list :", hashtags)
