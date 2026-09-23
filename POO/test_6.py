class Voiture:
    pass


class Etudiant:
    pass


def create_objects(classe, n):
    return [classe() for _ in range(n)]


# Test 1 : Voiture
voitures = create_objects(Voiture, 5)
print(voitures)

# Test 2 : Etudiant (preuve de généricité)
etudiants = create_objects(Etudiant, 2)
print(etudiants)