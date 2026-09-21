#=========Ask usernames============

# noms=[]
# def demander_nom_utilisateur():
#     nom = " "
#     while nom != "":
#         nom = input(f"Entrer un nom !");
#         if nom == "":
#             noms.append(nom);



# demander_nom_utilisateur();
# print(f"La liste contient {len(noms)} {noms}")

#=======================================================
nom_chaffeur:list = ["Patrick","Paul","Marc","Jean","Pierre","Marie","Maxime"];
distance_chauffeur_km:list=[1.5,2.2,0.4,0.9,7.1,1.1,0.6]

index_min = 0;
distance_min = distance_chauffeur_km[0];

for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i];
    if distance < distance_min:
        distance_min= distance;
        index_min=i;




print(f"Distance minimum est : {distance_min} km !")
print(f"Index minimum est {index_min}")
print(f"Le chauffeur appele est {nom_chaffeur[index_min]}")


