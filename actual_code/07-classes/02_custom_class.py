user1 = {
  "name":"Angharad",
  "location": "Salford",
  "role": "Delivery Manager"
}

user2 = {
  "name": "Gabriel",
  "locatin": "Salford",
  "role": "Degree Apprentice PM"
}

class User:
  # constructor, initializer, __init__
  def __init__(self, name, location, role):
    self.name = name
    self.location = location
    self.role = role
    self.manager = False

  # Human readable - what we see in logs
  def __str__(self):
    return f"User {self.name}, role is {self.role}, location is {self.location}"

  # Machine Readable - what we see when debugging
  def __repr__(self):
    return f"User(name='{self.name}', role='{self.role}', location='{self.location}')"

  def works_in(self, new_location):
    if new_location.lower() in ["belfast", "salford", "glasgow", "london", "cardiff"]:
      self.location = new_location
    else:
      print("Not a valid office.")
  
  def is_management(self):
    return "manager" in self.role.lower()



user3 = User(name="Kevin", location="Belfast", role="Developer Educator")
user4 = User("Claire", "Salford", "Tester Manager")


user3.works_in("Iceland")
print(user3.location)

print(user4.is_management())
# user5 = User(name= , location= , role=)

# print(user1["name"], user2["name"], user3.name, user4.name)
# print(user1["location"], user2["locatin"], user3.location, user4.location)
# print(user1["role"], user2["role"], user3.role, user4.role)

# print(user1)
# print(user4)
# print(user3)

# print([user3, user4])


