# def afficher_info(nom,age):
#     print()
#     print("Votre nom est " + nom +" vous avez "+ str(age) + "ans")
#     print("L'ans prochain vous aurez "  +str(age + 1)+ " ans")
#     print()
#     if age>=18:
#         print(nom+"vous etes majeur")
#     elif age==17 :
#         print(nom + "vous etes presque majeur")
#     elif age ==18:
#         print(nom + "vous etes juste majeur felicitation ")
#     else:
#         print(nom + "vous etes mineur !")


# def demander_age():
#     age = 0
#     while age == 0:
#         age_str = input("Quel est votre age ? ");
#         try:
#             age = int(age_str);
#         except:
#             print("Erreur:: age doit etre un nombre")
#         return age

# def demander_nom():
#     nom = input("Quel est votre nom ? ");

#     while nom  =="":
#         nom = input("Quel est votre nom ? ");
#     return nom;

# # #persone1
# # nom1 = demander_nom()
# # age1 =demander_age()

# # #persone2
# # nom2 = demander_nom();
# # age2= demander_age()

# # #afficher info de persone
# # afficher_info(nom1,age1)
# # afficher_info(nom2,age2)

# for i in range(0,5):
#     print(i)

# def recuperer_et_afficher_ifos_persone(numbero_persone):
#     nom = input(f"Nom de la persone {numbero_persone} :")
#     age= input(f"Age de la persone {numbero_persone} :")
#     print(f"La persone {numbero_persone} est {nom} et a {age} ans ! ")



# recuperer_et_afficher_ifos_persone(1)
# recuperer_et_afficher_ifos_persone(2)
# recuperer_et_afficher_ifos_persone(3)


#=========================Exo-Table-de-multiplication--=====================//
def afficher_table_multiplication(n:int,min:int,max:int):
        if min >max:
            print(f"Error: min cannot be > than max")
            return;
        for i in range(min,max+1):
            print(f"{i}*{n} = {i*n}");

# afficher_table_multiplication(4,1,10)

#=========================Exo-QCM-.1.0--=========================//

# def knowlege_cheker(question:str,r1:str,r2:str,r3:str,r4:str,bonne_reponse:str)->None:
#      global score
#      print("QUESTIONS") 
#      print(f" {question}")
#      print(f" (a): {r1}")
#      print(f" (b): {r2}")
#      print(f" (c): {r3}")
#      print(f" (d): {r4}")
#      user_choice = input(f"Votre reponse !: ")
#      if user_choice != bonne_reponse:
#         print(f"Erreur: la bonne reponse est : {bonne_reponse}");
      
#      else:
#         print(f"Bonne reponse {user_choice} est la bonne reponse");
#         score+=1;
#      print(f"Votre score est : {score}")
# score:int = 0;

#=========================Exo-QCM-.1.0--=========================//
def demander_reponse_numeric_utilisateur(min:int,max:int):
    reponse_str= input(f"Votre reponse entre {str(min)} et {str(max)} :")
    try:
         reponse_int= int(reponse_str);
         if min<=reponse_int<=max:
              return reponse_int
         else:
              print(f"Un nombre entre {min} et {max} est requis !");
    except:
         print(f"Error: chosies un nombre entre {min} et {max}")
    return demander_reponse_numeric_utilisateur(min,max)
              
score=0;
def poser_question(question):
     global score;
     bonne_repone= question[2]
     titre:str= question[0];
     choix:list = question[1]

     print(titre)
     print() 
     for i in  range(len(choix)):
         print(f"{i+1}-->{choix[i]}")
     reponse_int = demander_reponse_numeric_utilisateur(1,len(choix))
     if choix[reponse_int-1].lower() == bonne_repone.lower():
          score=score+1;
          print(f"Bonne reponse {bonne_repone} est bien la capitale !")
          print(f"Votre score est : {score}")
     else:
          print(f"Mauvaise reponse la bonne reponse est : {bonne_repone}")
     


question1=("Quelle est la capitale de la France ?",("Nice","Bodeaux","Paris","Reine","Lille"),"Paris");
question2=("Quelle est la capitale du Mali ?",("Kayes","Gao","Sikasso","Bamako","Kangaba"),"Bamako");

poser_question(question1)
print()
poser_question(question2)