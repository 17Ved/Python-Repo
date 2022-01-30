farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# if we want a set containing all the animals, we can create the union of the two sets.
# sets have the union method that does just that

all_animals = farm_animals.union(wild_animals)
print(all_animals)

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

all_animals_3 = wild_animals | farm_animals     # another method to write union
print(all_animals_3)








