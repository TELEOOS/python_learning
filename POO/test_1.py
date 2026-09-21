class Livre:
    pass

livre1 = Livre()
livre2 = Livre()

print(f"Le type de livre1 est :{type(livre1)} et celui de livre2 est {type(livre2)}")
print(id(livre1))   # ex: 140234...
print(id(livre2))   # ex: 140235... → différent !
print(livre1 is livre2)  # False → confirme l'unicité