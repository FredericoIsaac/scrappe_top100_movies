import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()
response_data = response.text

soup = BeautifulSoup(response_data, "html.parser")

articles = soup.find(name="div", class_="jsx-3821216435 block-item listicle-container")

img_tag = articles.find_all(name="img")

movies = []
count = 100
for img in img_tag:
    alt = img.get("alt")
    movies.append(f"{count}) {alt}")
    count -= 1


movies_string = "\n".join(movies[::-1])

with open("movies.txt", "w") as file:
    file.write(movies_string)
