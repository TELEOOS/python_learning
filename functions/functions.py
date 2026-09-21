#python functions learning 

def est_majeur(age):
   if age >= 18:
      return True;
   else: return False

def afficher_info_persone(nom="",age=0):
  if nom =="":
     print(f"Vous n'avez pas donne de nom l'age vaut {age}")
     return;
  if age ==0:
     print(f"La persone est {nom}")
  else:
     print(f"La persone est {nom} son age est {age} ")
  print(f"Le nom comporte {len(nom)} caracteres")


afficher_info_persone("Alice", 25)