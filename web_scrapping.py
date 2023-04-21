import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# The URL of the website
url = 'https://mydramalist.com'
# The URL of the page to scrape
scraping_url = 'https://mydramalist.com/shows/top_korean_dramas?'
links = []
titles = []

#There are 5 pages in total to scrape
for index in range(1,6):

    req=requests.get(scraping_url + 'page=' + str(index))

    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find(id='content')

    
    urls = results.find_all("a",class_='block')
    title = results.find_all('h6','title')
    for i in urls:
        links.append(i.get('href'))
    
    for j in title:
        titles.append(j)



Title = []
Genres = []
Score = []
Other = []

# For each URL of a kdrama
for link in links:
    drama_link = url + link
    page = requests.get(drama_link)
    soup = BeautifulSoup(page.content,"html.parser")
    results = soup.find(id='content')
    elements = results.find_all("div", class_='container-fluid title-container')

    # Get the Title, Genre and Other relevant information for each kdrama
    for element in elements:

        genres_element = element.find('li',class_='list-item p-a-0 show-genres')
        title_element = element.find('h1',class_='film-title')
        other_elements = element.find('div',class_ ='show-detailsxss')
        Title.append(title_element.text)
        Genres.append(genres_element.text)
        Other.append(other_elements.text)

# Extract the rating for each drama from the Other list using regular expressions
for i in Other:
    score = re.search(r'[0-9][.][0-9]',i)
    if score:
        Score.append(score.group())

for index,j in enumerate(Genres):
    Genres[index] = j.replace("Genres:","")


dict = {'Title' : Title, 'Genre' : Genres, 'Rating': Score}
df = pd.DataFrame(dict)



        
        




