animals = ["hund", "katt", "fisk", "fugler", "hest"]
for animal in animals:
    print(animals)

names = ["Alex", "Tommy", "Hedda", "Stian", "Gøril"]
for i in range(len(animals)):
    print(names[i], "er", animals[i])


animals = ["hund", "katt", "fisk", "fugler", "hest"]
print(animals[0]) # Første ord i rekken
print(animals[-1]) # Siste ord i rekken


print(animals) # Dyrelisten
animals(sort) # Sortert i alfabetisk rekkefølge
animals.reverse() # Sortert i alfabetisk bakvendt rekkefølge
print(animals)