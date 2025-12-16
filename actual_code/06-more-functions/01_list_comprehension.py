locations = ["London", "Salford", "Accrington", "Belfast", "Brighton"]

upper_cased_locations = []
for place in locations:
    upper_cased_locations.append(place.upper())

print(locations)
print(upper_cased_locations)

# readable and maintainable??  Pythonic solution! Clever solution. Code golf.
upper_cased_locations_2 = [p.upper() for p in locations if p.startswith("B")]
print(upper_cased_locations_2)