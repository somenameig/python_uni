#tp 3 ecriture formatee et structures conditionnelles/repetitives
#travail a faire 1:


#1.1- ecrire un commentaire suivant a la premiere ligne du code
#ecriture formatee et f strings
#1.2- affecter la valeur 300 a la variable quantite
quantite= 300
print(f"il vous faut {quantite} grammes de farine")
#1.3- afficher la phrase
print(f"si vous avez une quantite suffisante de farine, vous pouvez en utiliser jusqu'a {quantite+200} grammes")
#1.4- ignorer le code precedent en le mettant en commentaire
#1.5- ecrire le commentaire suivant: vvv
# structure conditionnelle et utilisation de la fonction input
#1.6- ecrire un programme qui demande l'age puis affiche un message selon les conditions donnees
age=input("veuillez saisit votre age: ")
if int(age)>=18 :
    print("vous etes majeur, vous pouvez passer le permis de conduite")
elif int(age)>=1 and int(age)<=17 :
    print("vous etes mineur, vous ne pouvez pas encore passer le permis")
else:
    print("age invalide, veuillez entrer un nombre positif")


#travail a faire 2:

#2.1- ecrire un programme qui affiche les consignes d'utilisaion d'une pompe en suivant les intructions:
tension=float(input("quelle est votre tension d'alimetation?: "))
temperature=float(input("quelle est la temperature de la paroi de votre pompe? :"))
if tension>230 and temperature>70 :
    print("il faut debrancher la pompe et verifier l'alimentation ainsi que le systeme de refroidissement.")
elif tension<=230 and temperature>70 :
    print("il faut verifier le systeme de refroidissement")
elif tension<=230 and temperature<=70 :
    print("tout fonctionne parfaitement!")

#2.2- ignorer le code en le mettant en commentaire (#)
# structure repetitves (for et while)

#2.3- ecrire une ligne de code permettant d'afficher chanque caractere du mot bonjour
message="bonjour"
for letter in message:
    print(letter)
#2.4- en utilisant for, ecrire une ligne qui permet 
for i in range(1,11):
    print(100+i)
#2.5- ecrire une boucle while qui permet d'incrementer la valeur de n avec un pas de 1
n=0
while n<5 :
    n=n+1
    print(n)
#2.6- ecrire un programme qui permet de parcourir les heures d'une journee et d'afficher le message
heure=float(input("quelle heure est-il?: "))
text="PHARMACIE"
for heure in range (1,25):
  if heure>=8 and heure<18:
    print(f"l'heure est {heure} h")
    for lettre in text :
        print(lettre)
    print("c'est ouvert")



