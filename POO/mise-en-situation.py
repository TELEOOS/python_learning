# POO EXERCICE DE MISE EN STUATION 1
#genre
#False :Femme
#True : Homme

class Persone:
    def __init__(self,nom:str,age:int,genre:bool):
        self.nom=nom;
        self.age=age;
        self.genre=genre;
        print(f"Contructeur  {self.nom}")
    def se_presenter(self)->None:
        if self.genre:
            print(f"Bonjour je m'appelle    {self.nom} j'ai {self.age} ")
            print(f"Genre : Masculin !")
            if self.est_majeur():
                print(f"Je suis majeur")
            else:
                print(f"Je suis mineur !");
            print()
        else:
             print(f"Bonjour je m'appelle    {self.nom} j'ai {self.age} ")
             print(f"Genre : Feminin !")
             if self.est_majeur():
                print(f"Je suis majeure")
             else:
                print(f"Je suis mineure !");
                print()

    def est_majeur(self)->bool:
        return self.age >=18;

persone1= Persone("Guindo",24,True)
persone2= Persone("Koulsoum",15,False)

persone1.se_presenter();
persone2.se_presenter();