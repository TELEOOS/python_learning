class Voiture:
    pass

n = 5
voitures = []

for _ in range(n):
    voitures.append(Voiture())

print(f"La liste des voitures contient : {voitures}")


voitures = [Voiture() for _ in range(n)]

for voiture in voitures :
    print(f"Voiture : {voiture}")