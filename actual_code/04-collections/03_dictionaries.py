empty_dict = {}
print(empty_dict)
print(type(empty_dict))

user_dict = {
  "name": "Sarah",
  "location": "Manchester",
  "team": "Analytics"
}

# print(user_dict["name"])
print(user_dict.get("name", "Unknown"))

user_dict["languages"] = ["SQL", "R"]

print(user_dict)

print("name" in user_dict)
print("Sarah" in user_dict)

print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())