import json
read_json = open("hobbie.json", "r")
data = json.load(read_json)
read_json.close()
name = data["firstName"]
hobbies = data["hobbies"]
hobbies = ", ".join(hobbies)
print(name, "has hobbies as", hobbies)
