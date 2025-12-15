empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

name_1 = "Marcus"
name_2 = "Lalitha"
name_3 = "Sana"

#           0          1         2
names = ("Marcus", "Lalitha", "Sana", "Claire", "Sarah")

print(len(names))
print(names[2])
# print(names[4])  - be careful not to go out of range!

print(names[0:2])
print(names[-1])
print(names[1:])
print(names[0:4])
print(names[0:4:3])

print("Hello my name is Kevin"[0:10:3])

more_names = (names, ("Gabriel", "Reece", "Angharad"), ("Tanveer", "Simon", "Vishal"))
print(more_names)

print(more_names[1][1])  # print reece


# if "Marcus" in names:
#   print("Hi Marcus!")

# if "Kevin" in names:
#   print("Hi Kevin!")

# for person in names:
#   print(f"Hi {person} - how are you?")

print(names.count("Kevin"))

print(names.index("Sarah"))

target_name = "Sana"

if target_name in names:
  print(names.index(target_name))