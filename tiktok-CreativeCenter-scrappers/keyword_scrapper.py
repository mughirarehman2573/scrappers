import requests
from datetime import datetime

now = datetime.now()

# This part is to be replaced with latest API


import requests

url = "https://ads.tiktok.com/creative_radar_api/v1/script/keyword/list?page=1&limit=20&period=7&country_code=US&industry=14000000000&order_by=post&order_type=desc"

payload = {}
headers = {
    'authority': 'ads.tiktok.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'anonymous-user-id': '21487677-8062-4660-9864-5738cd0ccc72',
    'cookie': '_ttp=2T4rlZ40IgcYBfzZtDI8TKyAPrc; _ga=GA1.1.620795730.1690313524; tta_attr_id=0.1690364005.7260058121794486273; tta_attr_id_mirror=0.1690364005.7260058121794486273; _ga_HV1FL86553=GS1.1.1690364010.1.1.1690364579.60.0.0; lang_type=en; s_v_web_id=verify_lkk2w7p3_PDVQ3THI_JUp3_4rbA_8Qi3_opxvs9UPhsfk; tt_csrf_token=4kFsgG0t-FeoQsb3RHqax6ozV5Bc5QuuwMjU; tt_chain_token=TrcQFBt6NHYvC88Hkp7SaQ==; _ga_QQM0HPKD40=GS1.1.1691004433.31.0.1691004433.60.0.0; ttwid=1%7C3stDw9BWIZ6oZf6uf6dy4uX0UEKrp0L0oQWQWHDpd6g%7C1691004436%7C202661423b1a2ef6803e4eab8235e037fc9c9e032619a7a91163bb0308b3a4d7; msToken=kS8wiLQpp9NR71phEnEw-puSayfUQltAaiSfDPsqQf0re-w36xq4lV08Togo6oHiGBF6oP5ed-rB6KCp983nqUzGychC0bpNDaXsNeHu2tvavhTMUvGCGg==; msToken=kS8wiLQpp9NR71phEnEw-puSayfUQltAaiSfDPsqQf0re-w36xq4lV08Togo6oHiGBF6oP5ed-rB6KCp983nqUzGychC0bpNDaXsNeHu2tvavhTMUvGCGg==; msToken=LoK66Y3ekWHnM-HXvDoVdJUi4Qq_9CPxG3yo1QezR521h8DBOYkKK8yCoSPvCwdQcgWGdUr_cdWV8rBjy5aydF6qYxhRsHMInG0MS2Z5oMruyaqUh0PVRHDeuIy3dNkLbw==',
    'lang': 'en',
    'referer': 'https://ads.tiktok.com/business/creativecenter/keyword-insights/pc/en',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'timestamp': '1691004476',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'user-sign': 'bf29063b4c371e2f',
    'web-id': '7259841200039396866'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# End point to replace code with lates API

keyword_list = []
json_data = response.json()
toq = open("Keyword-insights-01-08.csv", "a")
toq.write("Ranking, keyword, popularity, popularity change, ctr, cpa,  cvr, impression, comment, like, share, date, \n")
req_id = json_data.get("data").get("keyword_list")
ranking = 0
for i in req_id:
    ranking += 1
    toq.write(f"{ranking}")
    keyword = i.get("keyword")
    toq.write(f",{keyword}")
    keyword_list.append(keyword)
    comments = i.get("comment")
    toq.write(f",{comments}")
    cpa = i.get("cpa")
    toq.write(f",{cpa}")
    ctr = i.get("ctr")
    toq.write(f",{ctr}")
    cvr = i.get("cvr")
    toq.write(f",{cvr}")
    impression = i.get("impression")
    toq.write(f",{impression}")
    like = i.get("like")
    toq.write(f",{like}")
    post = i.get("post")
    toq.write(f",{post}")
    post_change = i.get("post_change")
    toq.write(f",{post_change}")
    share = i.get("share")
    toq.write(f",{share}")
    formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
    toq.write(f",{formatted_datetime}")
    toq.write("\n")
print("Key word List : ", keyword_list)
