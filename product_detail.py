import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")

# Replace the list_of_products with new generated list of products from product_scrapper.py

list_of_products = ['Perfume-601583', 'Serums-Essences-601619', 'Shampoo-Conditioner-601469',
                    'Hair-Scalp-Treatments-981512', 'Body-Wash-Soap-601493', 'Lipstick-Lip-Gloss-601534',
                    'Deodorants-Antiperspirants-601498', 'Makeup-Tools-601537', 'Manicure-Pedicure-Tools-700790',
                    'Facial-Sunscreen-Sun-Care-601602', 'Teeth-Whitening-601690', 'Body-Beauty-Devices-601664',
                    'Nail-Art-Nail-Polish-601591', 'Moisturisers-Mists-601615', 'Concealer-Foundation-601554',
                    'Eye-Treatments-601646', 'Hair-Care-601681', 'Body-Makeup-601582', 'Acne-Treatments-873480',
                    'Facial-Cleansers-601609']
toq = open("product-detail-insights.csv", "a")
toq.write("product , Popularity, CTR, CVR, CPA, Cost, Impressions,  6s View Rate, Likes, Shares, Comments, \n")

for product in list_of_products:
    url = f"https://ads.tiktok.com/business/creativecenter/product-category/{product}/pc/en?index=0&level=l3&period=7&type=last&region=US&c=l1-601450"

    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    test_loop = 0
    paragraphs = soup.find_all('strong')
    toq.write(f"{product}")
    Popularity = paragraphs[0].get_text()
    toq.write(f",{Popularity}")
    CTR = paragraphs[1].get_text()
    toq.write(f",{CTR}")
    CVR = paragraphs[2].get_text()
    toq.write(f",{CVR}")
    CPA = paragraphs[3].get_text()
    toq.write(f",{CPA}")
    Cost = paragraphs[4].get_text()
    toq.write(f",{Cost}")
    Impressions = paragraphs[5].get_text()
    toq.write(f",{Impressions}")
    View_Rate = paragraphs[6].get_text()
    toq.write(f",{View_Rate}")
    Likes = paragraphs[7].get_text()
    toq.write(f",{Likes}")
    Shares = paragraphs[8].get_text()
    toq.write(f",{Shares}")
    Comments = paragraphs[9].get_text()
    toq.write(f",{Comments}")
    toq.write("\n")
