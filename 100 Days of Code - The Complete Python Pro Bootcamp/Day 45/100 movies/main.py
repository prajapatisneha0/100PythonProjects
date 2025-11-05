import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}

response = requests.get(url=URL,headers=header)

soup = BeautifulSoup(response.text, features="html.parser")
# print(soup.prettify())

all_movies = soup.select("h2 strong")

# for movies in all_movies:
#     print(movies.getText())

movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]


with open("moves.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
