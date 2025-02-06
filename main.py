from bs4 import BeautifulSoup
import requests
import func

headers = {'User-Agent': 'Chrome/92.0.4515.159 Safari/537.36'}

for i in range(1,7):
    html_link = f"https://www.metacritic.com/browse/movie/all/all/current-year/new/?page={i}"

    req = requests.get(html_link, headers=headers).text

    soup = BeautifulSoup(req, "lxml")

    movie_titles = soup.find_all("h3", class_ = 'c-finderProductCard_titleHeading')
    movie_date = soup.find_all("span", class_ = "u-text-uppercase")
    movie_description = soup.find_all("div", class_="c-finderProductCard_description")

    data = func.dataSet(movie_titles,movie_date,movie_description)
    func.exportToCSV(data)
    del data, movie_titles, movie_description, movie_date
    print(i)









