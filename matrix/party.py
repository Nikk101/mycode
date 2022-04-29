#!/usr/bin/env python3
import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()

    for x in movies["Search"]:
        if x["Type"] == 'movie':
            print(f"{x['Title']} was released in {x['Year']}")


if __name__ == "__main__":
    main()
