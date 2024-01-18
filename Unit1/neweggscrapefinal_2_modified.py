import requests
from bs4 import BeautifulSoup
import csv

# Scraping "R for Data Science"
my_url = "https://r4ds.had.co.nz/index.html"
# Create a sections csv file
csvfile = open('eggs_sections.csv','w', newline='')
# Create a writer to convert data into delimited strings
eggwriter = csv.writer(csvfile)

no_error = True

url = my_url
print("Grabbing...", url)
response = requests.get(url, allow_redirects=False)
print(response.url)
print("Status is", response.status_code)

html = response.text

soup = BeautifulSoup(html, "html.parser")

items_soup = soup.find_all('ul', attrs={'class':'book-toc list-unstyled'})
items = items_soup[0]
sections = items.find_all("li", attrs={"class":"book-part"})
chapters = items.find_all("li", attrs={"class":""})

eggwriter.writerow(["Sections"])
for i in range(len(sections)):
    section = sections[i].text
    eggwriter.writerow([section])

csvfile.close()

# Create a chapters csv file
csvfile = open('eggs_chapters.csv','w', newline='')
# Create a writer to write the chapters
chapters_eggwriter = csv.writer(csvfile)

# Header
chapters_eggwriter.writerow(["Chapters"])
for i in range(len(chapters)):
    chapter = chapters[i].text
    chapters_eggwriter.writerow([chapter])
