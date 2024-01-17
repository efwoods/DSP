import requests
from bs4 import BeautifulSoup

my_url = input("Url to scrape:")
print("Grabbing...", my_url)

response = requests.get(my_url)
print("Status is",response.status_code)

if response.status_code != 200:
    print(f"You can't scrape this. {response.status_code}")
else:
    print(f"scraping...\n{response.text}")
    
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    body_ = soup.find("div", attrs={"class":"css-f52tr7 e17qa79g0"})
    print(body_.text)
    
    

