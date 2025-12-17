user = {
    "name": "Alex",
    "roles": ["viewer", "producer"]
}

def can_publish(user):
    return "editor" in user["roles"] or "producer" in user["roles"]

class User:
    def __init__(self, name, roles, manager=False):
        self.name = name
        self.roles = roles
        self.manager = manager

    def can_publish(self):
        return "editor" in self.roles or "producer" in self.roles

lalitha = User("Lalitha", [ "tester"], True) # Dynamically typed
print(type(lalitha))

if lalitha.can_publish():
  print("Publish")
else:
  print("you are not authorised")

