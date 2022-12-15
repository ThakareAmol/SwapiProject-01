"""The Star Wars API lists 82 main characters in the Star Wars saga. For the
first task, we would like you to use a random number generator that picks a
number between 1-82. Using these random numbers you will be pulling 15
characters from the API using Python."""

from utils.randgen import ProduceChars
from utils.fetch_data import fetch_data

home_url = "https://swapi.dev"  # swapi website url
relative_url = "/api/people/{0}"  # magic string
start = 1
stop = 83


def do_task_one() -> None:
    """
    Get details of 15 random characters in range [1,82]
    """
    for character in ProduceChars():  # generating random character numbers from
        # 'RandomCharacters' generator
        absolute_url = home_url + relative_url.format(character)  # creating url for
        # each character in RandomCharacters() generator
        print(fetch_data(absolute_url))  # printing details of randomly generated url
        print("#####" * 25)  # pretty print - seperator
