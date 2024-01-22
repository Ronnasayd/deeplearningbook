import json
from unidecode import unidecode

text = ""
summary = "# Sumário\n\n"
with open("data.json") as file:
    chapters = json.loads(file.read())
    for chapter in chapters:
        ID = unidecode(chapter["title"].replace(" ", "-").replace("(","").replace(")","").replace(":","").lower())
        summary += f"- [{chapter['title']}](#{ID})\n\n"
        text += f'<div id="{ID}"></div>\n\n'
        text += f"# {chapter['title']}\n\n"
        text += chapter["content"]
with open("README.md", "w") as file:
    file.write(summary + "\n\n")
    file.write(text)
