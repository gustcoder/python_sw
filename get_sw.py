import requests
import pandas as pd


def get_films():
    try:
        r = requests.get('https://swapi.dev/api/films')
        films = r.json()["results"]

        films_list = []
        for film in films:
            films_dict = {
                "episode_id": film["episode_id"],
                "tile": film["title"]
            }
            films_list.append(films_dict)

        return films_list
    except Exception as err:
        print("There was an error to get films. Please try again!", err)


def order_films(df, sort_column='episode_id'):
    return df.sort_values(by=[sort_column])


def transform_parquet(df, filename):
    try:
        df.to_parquet(filename)
        print(f"DataFrame saved as {filename}.parquet")
    except Exception as err:
        print(f"Error saving DataFrame as {filename}.parquet:", err)


def main():
    try:
        films = get_films()
        df = pd.DataFrame(films)
        ordered_films = order_films(df)
        transform_parquet(ordered_films, "star_wars_films")
    except Exception as err:
        print("There was an error with SWAPI. Please try again!", err)


main()
