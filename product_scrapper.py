from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
# Replace this part of code with latest APi from product insights url.
import requests

url = "https://ads.tiktok.com/creative_radar_api/v1/product/list?last=7&page=1&limit=20&country_code=PK&ecom_type=l3&period_type=last&order_by=post&order_type=desc"

payload = {}
headers = {
  'authority': 'ads.tiktok.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'anonymous-user-id': '21487677-8062-4660-9864-5738cd0ccc72',
  'cookie': '_ttp=2T4rlZ40IgcYBfzZtDI8TKyAPrc; _ga=GA1.1.620795730.1690313524; tta_attr_id=0.1690364005.7260058121794486273; tta_attr_id_mirror=0.1690364005.7260058121794486273; _ga_HV1FL86553=GS1.1.1690364010.1.1.1690364579.60.0.0; lang_type=en; s_v_web_id=verify_lkk2w7p3_PDVQ3THI_JUp3_4rbA_8Qi3_opxvs9UPhsfk; tt_csrf_token=4kFsgG0t-FeoQsb3RHqax6ozV5Bc5QuuwMjU; tt_chain_token=TrcQFBt6NHYvC88Hkp7SaQ==; ttwid=1%7C3stDw9BWIZ6oZf6uf6dy4uX0UEKrp0L0oQWQWHDpd6g%7C1691005669%7Cdfe3cdc755f7095d9fde36c811c026a62baf75c8e71e93e567ffc7bf38c155f5; msToken=edBGfw_6loUZOppv1638eXmZiF6K8sk_0Sl0zS701ddz6hX3VYOWjtYFr-ew_9nL1FAHhwrsOofGt4X6RE7RIdFwBOYhTWKVS86ZIiHnnogYxlNmD8yt5w==; msToken=LVHaFONBm8N7Cbp564vlrD-EsxOugRnqr_ieZx6CYw008ONPN7Bt4Lor6ps-QrkASCRUatbfnRCwYMWBOakG6gZvUkh0lCQABZ_FEhfmkFD14kHkcObI; _ga_QQM0HPKD40=GS1.1.1691004433.31.1.1691005912.58.0.0; msToken=_zb8HWJVQlJcbqVVFLHLTsFUn2zlrNoMrMnxuU8lnakTTyvQy6d09AuUMgFoCmvcxdDPB-Ggv3G7bkPGI9PgWqTVGOKdHcwI4JHrqYzKxIcjOYIkxRSaUVTctleUV0trFb9Bm6GwnXw=',
  'lang': 'en',
  'referer': 'https://ads.tiktok.com/business/creativecenter/top-products/pc/en',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'timestamp': '1691005914',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  'user-sign': 'b2ebde46ebd0dfa5',
  'web-id': '7259841200039396866'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# End point to replace the code.

json_data = response.json()
toq = open("product-insights-01-08.csv", "a")
toq.write("ranking, product, popularity, popularity change, ctr, cvr,  cpa, impression, comment, like, share,date, \n")
req_id = json_data.get("data").get("list")
ranking = 0
product_ids = []
for i in req_id:
    ranking += 1
    toq.write(f"{ranking}")
    id = i.get("third_ecom_category").get("id")
    product = i.get("third_ecom_category").get("value")
    toq.write(f",{product}")
    url_title = i.get("url_title")
    product_id = f'{url_title}-{id}'
    product_ids.append(product_id)
    post = i.get("post")
    toq.write(f",{post}")
    popularity_change = i.get("post_change")
    toq.write(f",{popularity_change}")
    ctr = i.get("ctr")
    toq.write(f",{ctr}")
    cvr = i.get("cvr")
    toq.write(f",{cvr}")
    cpa = i.get("cpa")
    toq.write(f",{cpa}")
    impression = i.get("impression")
    toq.write(f",{impression}")
    comment = i.get("comment")
    toq.write(f",{comment}")
    like = i.get("like")
    toq.write(f",{like}")
    share = i.get("share")
    toq.write(f",{share}")
    toq.write(f",{formatted_datetime}")
    toq.write("\n")
print("product_List : ", product_ids)
