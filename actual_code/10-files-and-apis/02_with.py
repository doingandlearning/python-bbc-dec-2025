file = open("test.txt")
print(file.read())
file.close()

# context handler - preferred "Pythonic" open files!
with open("test.txt") as file:
  print(file.read())

# here!