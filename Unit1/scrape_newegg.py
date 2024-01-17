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
    
    items_ = soup.find_all("div", attrs={"class":"item-cell"})
    for i in range(len(items_)):
        item = items_[i]
        print(item.text)
    