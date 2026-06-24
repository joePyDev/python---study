import json

data = """{
  "title": "Python for Everybody",
  "author": "Charles",
  "year": 2016
}"""

info = json.loads(data)
print(info["author"])


# ---------------------------------------------------
data_2 = """[
  {"name": "Alice", "score": 95, "level": 3},
  {"name": "Bob", "score": 88, "level": 2},
  {"name": "Cara", "score": 91, "level": 4}
]"""

records = json.loads(data_2)

print(len(records))
for entry in records:
    print(entry["name"], entry["score"])

# ---------------------------------------------------
