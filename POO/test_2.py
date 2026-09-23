class Etudiant:
    pass

guindo = Etudiant()
karim = Etudiant()
fanta = Etudiant()

etudiants = [guindo, karim, fanta]

for etudiant in etudiants:
    print(etudiant)
    print(f"Etudiant : {etudiant} est une instance ? {isinstance(etudiant, Etudiant)}")