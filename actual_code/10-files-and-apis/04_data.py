import csv
import json

with open("movies.csv") as file:
  # reader = csv.reader(file)  # each row is a list
  reader = csv.DictReader(file, 
  # fieldnames=["name", "release", "director", "genre"] # provide if you want ot override the headerrow
  ) # each row is a dict

  
  # next(reader)  # this allows me to skip rows
  movies = []
  for row in reader:
    movies.append(row)

with open("movies.json", "w") as file:
  file.write(json.dumps(movies, indent=1))
  
with open("movies.json") as file:
  print(json.loads(file.read()))