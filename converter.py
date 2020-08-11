import json
import requests
from bs4 import BeautifulSoup


def get_hashed(id):
    url = "https://www.md5hashgenerator.com/"
    converted = requests.post(url, data={"stringy": id})

    soup = BeautifulSoup(converted.text, "html.parser")
    strongs = [strong.text for strong in soup.find_all("strong")]

    return strongs[1]


if __name__ == "__main__":
    with open("need_converted.json", "r") as file:
        unhashed = json.loads(file.read())
        
    hashes = []
    for raw in unhashed:
        # mini salt in the case someone is hellbent
        hashes.append(get_hashed(raw + "hrngh... soup"))
        
    with open("converted.json", "w") as file:
        file.write(json.dumps(students, indent=2))
