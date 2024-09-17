import requests
from bs4 import BeautifulSoup

response = requests.get("https://eviden.com/careers/")
soup = BeautifulSoup(response.content, 'html.parser')
