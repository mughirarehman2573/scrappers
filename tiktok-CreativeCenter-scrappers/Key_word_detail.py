import re

from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")

# Replace this keyword list with new generated key word list from key_scrapper.py

keyword_list = ['free shipping', 'you guys', '50% off', 'get yours', 'right now', 'shop now',
                'try it', 'get yours today', 'all day', 'wig', 'use it', 'buy 1 get 1 free', 'love it',
                'try this', 'get yours now', 'longsheng rice shampoo bars', 'soap', 'know what', 'summer',
                'put it']

toq = open("Keyword-deatil-insights.csv", "a")
toq.write("keyword,ctr, cvr, keyword phrase,date, \n")

for key in keyword_list:
    toq.write(f"{key}")
    sep = key.split(" ")
    if "%" in sep[0]:
        key = sep[0]
        word = sep[1]
        url = f"https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword={key}25+{word}&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"
    if len(sep) == 1:
        url = f"https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword={key}&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"
    if len(sep) == 2:
        key = sep[0]
        word = sep[1]
        url = f"https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword={key}+{word}&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"

    if len(sep) == 3:
        key = sep[0]
        word = sep[1]
        word2 = sep[2]
        url = f"https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword={key}+{word}+{word2}&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"

    if len(sep) == 4:
        key = sep[0]
        word = sep[1]
        word2 = sep[2]
        word3 = sep[3]
        url = f"https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword={key}+{word}+{word2}+{word3}&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"
    # Replace this code from lates API of keyword detail website
    import requests

    url = "https://ads.tiktok.com/creative_radar_api/v1/script/sentence/list?page=1&limit=50&period=7&keyword=free+shipping&country_code=US&industry=14000000000&order_by=ctr&order_type=desc"

    payload = {}
    headers = {
        'authority': 'ads.tiktok.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'anonymous-user-id': '21487677-8062-4660-9864-5738cd0ccc72',
        'cookie': '_ttp=2T4rlZ40IgcYBfzZtDI8TKyAPrc; _ga=GA1.1.620795730.1690313524; tta_attr_id=0.1690364005.7260058121794486273; tta_attr_id_mirror=0.1690364005.7260058121794486273; _ga_HV1FL86553=GS1.1.1690364010.1.1.1690364579.60.0.0; lang_type=en; s_v_web_id=verify_lkk2w7p3_PDVQ3THI_JUp3_4rbA_8Qi3_opxvs9UPhsfk; tt_csrf_token=4kFsgG0t-FeoQsb3RHqax6ozV5Bc5QuuwMjU; tt_chain_token=TrcQFBt6NHYvC88Hkp7SaQ==; ttwid=1%7C3stDw9BWIZ6oZf6uf6dy4uX0UEKrp0L0oQWQWHDpd6g%7C1691004898%7Cfa75fd5197c6d7ebd93461570a8f94f2f319cd2c026d181120f9bf81ee7cd266; msToken=V3VBJ7cDaa1ci93ajEaKj5mHyxdO9S0udzfveqfcHCH0Tb2ijLq30ttbmgaHr6lJ6oQ9qZ_2TvMQK_qHBK1Y32y9duLb9b4c0FaoGbZDRO5UImKbtUiwZdZ29RqcM8E=; _ga_QQM0HPKD40=GS1.1.1691004433.31.1.1691004911.23.0.0; msToken=Jf0Jur7HcBca1pS5nkNjr714qgjuj_J1OgH8MTBlywZsj1R5VIWSDcnr-Bvl34PS_dO-Rx7mPi3TB8k80eLLHnHItiPXfcsJGcB1A7mEBoQCntPyIpxa; msToken=LoK66Y3ekWHnM-HXvDoVdJUi4Qq_9CPxG3yo1QezR521h8DBOYkKK8yCoSPvCwdQcgWGdUr_cdWV8rBjy5aydF6qYxhRsHMInG0MS2Z5oMruyaqUh0PVRHDeuIy3dNkLbw==',
        'lang': 'en',
        'referer': 'https://ads.tiktok.com/business/creativecenter/tiktok-keyword/free%20shipping/pc/en?industry=14000000000&countryCode=US&orderBy=1&orderType=2&period=7&page=1',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'timestamp': '1691004913',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'user-sign': '81bedafab9a150cd',
        'web-id': '7259841200039396866'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # End point to replace the code.

    json_data = response.json()
    req_id = json_data.get("data").get("sentence_list")

    for i in req_id:
        ctr = i.get("ctr")
        toq.write(f",{ctr}")
        cvr = i.get("cvr")
        toq.write(f",{cvr}")
        sentence_raw = i.get("sentence")
        sentence = re.sub(r'[^a-zA-Z\s]', '', sentence_raw)
        toq.write(f",{sentence}")
        toq.write(f",{formatted_datetime}")
        toq.write("\n")
