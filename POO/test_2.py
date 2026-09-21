class Etudiant:
    pass;
guindo= Etudiant()
Karim= Etudiant()
fanta= Etudiant()

etudiant= [guindo,Karim,fanta];

for i in etudiant:
    print(i)
    print(f"Etudiant No:{i} est une instances ? {isinstance(i,Etudiant)}")