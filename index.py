from bs4 import BeautifulSoup
import json
file_path = "./test.json"

with open("sb.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

with open(file=file_path, mode='r') as read_file:
    object = json.load(read_file)
    pretty = json.dumps(object, indent=2)
    print(pretty)

tag = soup.find(id="pz-game-root")
game = tag.find_next("script")

# print(game.string)


