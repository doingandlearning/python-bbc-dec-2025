# Anonymous functions

beatles = ["Jethrio", "John", "Paul", "Bob", "George", "Ringo"]

def count_vowels(name):
  name = name.lower()
  count = name.count("a") + name.count("e") + name.count("i") + name.count("o") + name.count("u")
  return count

print(sorted(beatles, key=count_vowels))

data = [1, 3, 5, 2, 7, 4, 10]
print([item + 2 for item in data])

def add_one(item):
  return item + 1

add_one = lambda item: item + 1
print(add_one(4))

def add_two(item):
  return item + 2

# single steps, simple functions, throw away
print(list(map(lambda n:n+10, data)))

def double(n):
  return n * 2

double = lambda n: n * 2