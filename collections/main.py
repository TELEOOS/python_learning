#Les collections sont l'ensemble de Tableaux,Tuples,Listes ...
#=================Diffenrences-entre-Listes-et-les-Tuples---------------------
#------Tuples:Sont immutable---Listes:Sont mutables-------------------
# persones= ("Melanie","Jean","Martin","Alice");

# print(persones[0]);
# print(len(persones));
# for i in range(0,len(persones)):
#     print(f"Persone No:{i+1} est  {persones[i]}")
# for i in persones:
#     print(f"La premiere lettre de {i} est {i[0]}")
#     print(f"{len(i)}")

# ===========Les Listes==================
"""persones:str= ["Melanie","Jean","Martin","Alice"];

nouvel_persone:str= "David";
print(persones)
persones.append(nouvel_persone);
print(persones)
del persones[2]
print(persones)"""



#==============Tuples et Fontions=================//
 #Fonction qui retourne un Tuples
def obtenir_informations():
    return "Melanie",25,1.65;
def afficher_informations(nom,age,taille):
    print(f"Cette persone s'appele {nom} elle a {age} ans et sa taille est {taille}");

"""
#====On peut faire ça 
infos = obtenir_informations();
# print(f"Cette persone s'appele {infos[0]} elle a {infos[1]} ans et sa taille est {infos[2]}")
#=========Ou on peut faire ça 
nom,age,taille = obtenir_informations();
afficher_informations(nom,age,taille)
#Qui veut dire exactement la meme chose que :
afficher_informations(*infos)#On dit qu'on UNPACT le Tuple"""

#===========SLICES=================[start:stop] ou [start:stop:step(le saut )]

persones= ("Melanie","Jean","Martin","Alice","Pierre","Paul")

#Le premier bloc designe  : le debut :le second :la fin et le troisieme le pas qu'on doit faire 
# for i in persones[::2]
#     print(i)

