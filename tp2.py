#tp2 variable, types de donees et operations
#travail a faire 1:
#1.1- utuliser la fonction type
print(type(78.4))
print(type("true"))
print(type(20))
print(type([4,1,9]))
print(type(-10))
print(type(False))
#1.2- afficher les donnees aux variables
age= 21
message= 'bonjour'
reponse= True
differences_de_temperature = -3.72
true = 4
#1.3- le python n'accepte pas les variables True et difference de temperature car True est une fonction reserve au boolean et il ne faut laisser des espaces
#1.4- la solution a l'erreur est d'utuliser true (sans maj), ne pas laisser d'espace en les remplacant par - ou _, et '' pour des messages
#1.5- ligne de commande qui permet d'afficher les variables
print(age)
print(message)
print(reponse)
print(differences_de_temperature)
print(true)
#1.6- effectuer une affectation multiple de ces variables et afficher uniquement la variable reponse
print(reponse)
#1,7- ecrire des lignes de commandes qui permet d'afficher les types
print(type(str(21)))
print(type(int("10")))
print(type(float("5.5")))
#1.8- les fonctions str,int et float sert a nous donner leur version des variables donnees
#1.9- predicions:
# str(3)*int("2") => 33
# str(3)+str(4) => 34
# int("2")+float("2.5") => 4.5
# int("3")*float("1.5") => 4.5
print(str(3)*int("2"))
print(str(3)+str(4)) 
print(int("2")+float("2.5"))
print(int("3")*float("1.5"))


#travail a faire 2:
#2.1- predire le resultat, puis le verifier dans l'interpreteur
#"jour"+str(3) => jour3
#"bonjour"*(2) => bonjourbonjour
#"py"+"thon"+str(3) => python3
#int("4")*float("1.5") => 6.0
print("jour"+str(3))
print("bonjour"*(2))
print("py"+"thon"+str(3))
print(int("4")*float("1.5"))
#2.2 affecter les donnes aux variables
nom = "said"
prenom= "djamel"
fonction = "etudiant"
#2.3- ecrire un programe qui affiche la phrase "je mappelle said djamel ,je suis etudiant"
print('je mappelle',nom,prenom,',je suis',fonction)
#2.4- on ajoute la variable age (elle est deja declaree dans la question 1.2 )
print('je mappelle',nom,prenom,',je suis',fonction,'et jai',age,'ans')
#2.5- en utulisant age, ecrire un programme qui affiche la phrase "dans cinq ans, jaurai 26 ans"
print('dans cinq ans, jaurai', age+5, 'ans')