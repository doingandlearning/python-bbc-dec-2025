empty_list = []  
empty_list = list()

print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]

print(len(beatles))
print(beatles[1:])
print(beatles[-1])

print("John" in beatles)
print("Kevin" in beatles)

for beatle in beatles:
  print(beatle)

beatles.append("Reece")  # adds a single element!
print(beatles)

# iterable
beatles.extend(["Lalitha","Angharad","Claire", "John", "John"])  # add multiple elements
print(beatles)

beatles.insert(1, "Vishal") # more control <> more memory
print(beatles)

# beatles.insert(2, (1,2,3))
# print(beatles)

# beatles.sort()  # sort but changes the list
print(sorted(beatles))  # returns a sorted list but leaves the original unchanged
print(beatles)

deduplicated_beatles = list(set(beatles))
print(deduplicated_beatles)


# beatles.remove("John")  # removes the first instance that matches
# print(beatles)

# # while "John" in beatles:
while beatles.count("John") > 1:
  beatles.remove("John")
print(beatles)

beatles.reverse()
print(list(reversed(beatles)))
print(beatles)

freeze_list = tuple(beatles)
print(freeze_list)


for idx, value in enumerate(beatles):
  beatles[idx] = value + ".co.uk"

print(beatles)

person = ["Kevin", "Belfast"]

name, location = person

print(name, location)

print(len(beatles)) # len() -> human 1 indexed count
for i in range(len(beatles)):
  print(i)


bands = [
    ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
    ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
    ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    ["Jack White", "Meg White"]                                          # The White Stripes
]

print(bands[7][2])
print(bands[1][2])


