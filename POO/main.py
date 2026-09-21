#=======================Programmation imperative/proceduralle ============================/
"""def afficher_informations_persone(nom,age)->None:
    print(f"La persone s'appelle {nom} et son age est {age}")

def demander_persone()->str:
    nom = input(f"Quel est votre nom ?")
    return nom


nom1:str="Jean";
age1:int =30; 

nom2:str="Paul";
age2:int=24

afficher_informations_persone(nom1,age1);
afficher_informations_persone(nom2,age2);

nom3:str=demander_persone();
age3=18

afficher_informations_persone(nom3,age3)"""""

#====================la programmation orientee objet===============/
class Persone:
    def __init__(self,nom:str="",age:int=0):
       self.nom=nom;
       self.age=age;
    
    def se_presenter(self):
        if self.age ==0:
            print(f"Bonjour je m'appelle toto !")
        else:
            if self.est_majeur():
                print(f"Je suis majeur !")
            else:
                print(f"Je suis mineur !")

        if (self.nom==""):
            return self.demander_nom();
                
        print(f"Bonjour je m'appelle {self.nom} et j'ai {self.age} ! ")
       
    def est_majeur(self)-> bool:
        return self.age >= 18
    
    def demander_nom(self):
        self.nom= input("Quel est votre nom ?")
        return self.nom;


persone1= Persone("",0)
# persone2= Persone("Koulssoum",10)
persone1.se_presenter()
# persone2.se_presenter()

# print(f"La persone {persone1.nom} est { persone1.est_majeur()}")
# print(f"La persone {persone2.nom} est { persone2.est_majeur()}")

