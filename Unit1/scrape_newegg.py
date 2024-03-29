import requests
from bs4 import BeautifulSoup

# my_url = input("Url to scrape:")
my_url = "https://www.newegg.com/p/pl?d=playstation"
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
        
        title = item.find("a", attrs={"class":"item-title"}).text
        # print(title)
        
        price = item.find("li", attrs={"class":"price-current"})
        # print(price)
        price = float(price.find("strong").text.replace(',', '') + price.find("sup").text)
        
        rating = item.find("i", attrs={"class":"rating"})
        if rating is not None:
            rating = rating['class'][1].split('-')[1]
            # print(rating)
            
        ratingNum = item.find("span", attrs={"class":"item-rating-num"})
        if ratingNum is not None:
            ratingNum = ratingNum.text.lstrip('(').rstrip(')')
            print(ratingNum)
        
        print("Title: ", title, "\nPrice: ", price, "\nRating: ", rating, "\nRatingNum: ", ratingNum)
    

