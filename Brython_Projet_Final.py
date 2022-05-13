# coding: utf8


'''
Mini-projet "Projet Final"
Objectif : Création d'une page web de 4 mini-jeux
Auteurs : - Eliott CHUPIN 1ère 6
          - Nolann DECUREY 1ère 6
          - Maxime BIGEY--ROUX 1ère 6
          - Samuel HURTADO 1ère 6
Version n°3.14
Dernière révision le 07/05/2022
'''


from browser import document, html
import csv
from random import*


def ouverture_fichier(nom_fichier):

    """
    Crée une fonction nommée ouverture_fichier qui permet d'ouvrir un fichier csv
    Entrée : - nom_fichier qui est le nom du fichier à ouvrir
    Sortie : - table de dictionnaires qui contient tout le fichier
    """

    table = []
    with open(nom_fichier, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for _ in reader:
            table.append(_)
    return table

vies = 5
erreurs = 0
table_jeu_capitales = ouverture_fichier('Jeu_capitales.csv')
table_jeu_culture = ouverture_fichier('Jeu_culture.csv')
table_jeu_drapeaux = ouverture_fichier('Jeu_drapeaux.csv')
table_jeu_sutom = ouverture_fichier("Jeu_sutom.csv")
question_nombre = [i for i in range(27)]
question = 0
reponse = []
comptage = -1


def page_accueil():

    """
    Crée une fonction nommée page_accueil qui permet d'afficher la page
    d'accueil de notre page web
    Entrée : - aucune
    Sortie : - aucune
    """

    document['vies_utilisateur'].bind('mousemove', vies_utilisateur)
    document <= html.BR()
    document <= html.P(html.BUTTON(f"Jeu des capitales européennes", Class='bouton', value=1, id='Jeu 1'))
    document <= html.P(html.BUTTON(f"Test de culture générale", Class='bouton', value=2, id='Jeu 2'))
    document <= html.P(html.BUTTON(f"Jeu des drapeaux européens", Class='bouton', value=3, id='Jeu 3'))
    document <= html.P(html.BUTTON(f"Jeu sutom", Class='bouton', value=4, id='Jeu 4'))
    document <= html.P("Created by Eliott, Nolann, Maxime, Samuel", Class='creat')
    document <= html.IMG(Class="image_licence", src='https://www.ffamhe.fr/wp-content/uploads/2017/05/by-nc-sa.eu_.png',  width="88", height="33")
    document <= html.A('Licence', href="https://creativecommons.org/licenses/by-nc-sa/3.0/fr/", Class='lien_licence')
    for i in range(1, 5):
        document[f'Jeu {i}'].bind('click', attribution)



def vies_utilisateur(évènement):

    """
    Crée une fonction nommée vies_utilisateur qui permet de conter les vies de
    l'utilisateur qu'il choisit dans le slider
    Entrée : - évènement qui est l'évènement du bind de page_accueil
    Sortie : - aucune
    """

    global vies
    document['vies'].textContent = document['vies_utilisateur'].value
    vies = int(document['vies_utilisateur'].value)


def attribution(évènement):

    """
    Crée une fonction nommée attribution qui permet d'attribuer le jeu choisi
    par l'utilisateur
    Entrée : - évènement qui est l'évènement du bind de page_accueil
    Sortie : - aucune
    """

    global table_du_jeu
    if évènement.target.value == '1':
        table_du_jeu = table_jeu_capitales
        points(évènement)
    if évènement.target.value == '2':
        table_du_jeu = table_jeu_culture
        points(évènement)
    if évènement.target.value == '3':
        table_du_jeu = table_jeu_drapeaux
        points(évènement)
    if évènement.target.value == '4':
        table_du_jeu = table_jeu_sutom
        points(évènement)


def points(évènement):

    """
    Crée une fonction nommée points qui permet de conter les points de
    l'utilisateur et de savoir si il a gagné, perdu ou si il peut continuer
    Entrée : - évènement qui est l'évènement du bind de traitement_capitales_culture
    ou de traitement_drapeaux
    Sortie : - aucune
    """

    global comptage
    comptage += 1
    if comptage == len(table_du_jeu) and vies >= 1:
        victoire()
    elif vies >= 1:
        aleatoire()
    else:
        defaite()


def aleatoire():

    """
    Crée une fonction nommée aleatoire qui permet de choisir aléatoirement
    l'indice de la question
    à afficher à l'utilisateur
    Entrée : - aucune
    Sortie : - aucune
    """

    global table_du_jeu
    global question
    global question_nombre
    question = randint(0, len(table_du_jeu) - 1)
    if question_nombre[question] == 'used':
        aleatoire()
    if table_du_jeu == table_jeu_drapeaux:
        lancement_drapeaux()
    if table_du_jeu == table_jeu_sutom:
        lancement_sutom()
    if table_du_jeu == table_jeu_capitales or table_du_jeu == table_jeu_culture:
        lancement_capitales_culture()
    question_nombre[question] = 'used'


def lancement_capitales_culture():

    """
    Crée une fonction nommée lancement_capitales_culture qui permet d'afficher
    la question et les réponses du jeu des capitales ou celui de culture
    générale en fonction du choix de l'utilisateur
    Entrée : - aucune
    Sortie : - aucune
    """

    document['corps'].textContent = ''
    document <= html.H3(table_du_jeu[question]['Question :'])
    document <= html.H2(f"{comptage + 1}/{len(table_du_jeu)}")
    for _ in range(vies):
        document <= html.IMG('', id="img", src="https://fr.seaicons.com/wp-content/uploads/2015/08/heart-icon.png", width="50", height="50")
    for _ in range(3):
        document <= html.BR()
    for i in range(1, 5):
        document <= html.P(html.BUTTON(table_du_jeu[question][f'Réponse {i}'], Class='bouton', value=i, id=f'Réponse{i}'))
        document[f'Réponse{i}'].bind('click', traitement_capitales_culture)


def traitement_capitales_culture(évènement):

    """
    Crée une fonction nommée traitement_capitales_culture qui permet de traiter
    la réponse de l'utilisateur
    Entrée : - évènement qui est l'évènement du bind de
    lancement_capitales_culture
    Sortie : - aucune
    """

    global vies
    global erreurs
    reponse.append(table_du_jeu[question]['Vérification'])
    if reponse[comptage] != f'Réponse {évènement.target.value}':
        bonne_reponse = table_du_jeu[question]['Vérification']
        document['corps'].textContent = ''
        document <= html.H3("Dommage, tu t'es trompé")
        document <= html.H3(f"La bonne réponse était : {table_du_jeu[question][bonne_reponse]}")
        if table_du_jeu == table_jeu_culture:
            document <= html.H5(f"Explication : {table_du_jeu[question]['Explication']}")
        for _ in range(3):
            document <= html.BR()
        document <= html.BUTTON("Ok", id="btn_valide", Class='bouton')
        document["btn_valide"].bind('click', points)
        vies -= 1
        erreurs += 1
    else:
        points(évènement)



def lancement_drapeaux():

    """
    Crée une fonction nommée lancement_drapeaux qui permet d'afficher le
    drapeau ainsi que le bouton de réponse de l'utilisateur
    Entrée : - aucune
    Sortie : - aucune
    """

    def entree(évènement):
        if évènement.key == 'Enter':
            traitement_drapeaux(évènement)
    document['corps'].textContent = ''
    document <= html.H3("Quel est le nom de ce pays ?")
    document <= html.H2(f"{comptage + 1}/{len(table_du_jeu)}")
    for _ in range(vies):
        document <= html.IMG(src="https://fr.seaicons.com/wp-content/uploads/2015/08/heart-icon.png", width="50", height="50")
    for _ in range(4):
        document <= html.BR()
    document <= html.IMG(src=f"{table_du_jeu[question]['Drapeau']}", width="400", height="250", id="drapeau")
    for _ in range(2):
        document <= html.BR()
    document <= html.INPUT(id="pays", Class='saisie')
    document <= html.BUTTON("Ok", id="btn_valide", Class='bouton')
    document['btn_valide'].bind('click', traitement_drapeaux)
    document['pays'].bind("keypress", entree)


def traitement_drapeaux(évènement):

    """
    Crée une fonction nommée traitement_drapeaux qui permet de traiter la
    réponse de l'utilisateur
    Entrée : - évènement qui est l'évènement du bind de lancement_drapeaux
    Sortie : - aucune
    """

    global vies
    global erreurs
    reponse.append(table_du_jeu[question]['Réponse :'])
    if reponse[comptage].upper() != document['pays'].value.upper():
        document['corps'].textContent = ''
        document <= html.H3("Dommage, tu t'es trompé")
        document <= html.H3(f"La bonne réponse était : {reponse[comptage]}")
        for _ in range(3):
            document <= html.BR()
        document <= html.BUTTON("Ok", id="btn_valide", Class='bouton')
        document["btn_valide"].bind('click', points)
        vies -= 1
        erreurs += 1
    else:
        points(évènement)


def lancement_sutom():

    """
    Crée une fonction nommée lancement_sutom qui permet d'afficher un indice
    pour le mot à chercher ainsi que le bouton de réponse de l'utilisateur
    Entrée : - aucune
    Sortie : - aucune
    """
    
    def entree(évènement):
        if évènement.key == 'Enter':
            traitement_sutom(évènement)
    document['corps'].textContent = ''
    document <= html.H3("Essaye de deviner le mot !")
    document <= html.H2(f"Indice : Le mot cherché fait {len(table_du_jeu[question]['Mot :'])} lettres et  \n"
                        f"sa première lettre est {table_du_jeu[question]['Mot :'][0].upper()}\n")
    document <= html.H2(f'Bonne chance, tu as {vies} vies !')
    document <= html.H3("🟩 : La lettre est bonne et bien placée", Class='code_couleur_bon')
    document <= html.H3("🟨 : La lettre est bonne mais mal placée", Class='code_couleur_moyen')
    document <= html.H3("🟥 : La lettre n'est pas dans le mot", Class='code_couleur_faux')
    print(f"{table_du_jeu[question]['Mot :']}")
    document <= html.INPUT(id="sutom", Class='saisie')
    document <= html.BUTTON("Ok", id="btn_valide", Class='bouton', value=-1)
    document['btn_valide'].bind('click', traitement_sutom)
    document['sutom'].bind("keypress", entree)


def traitement_sutom(évènement):

    """
    Crée une fonction nommée traitement_sutom qui permet de traiter le mot
    choisi par l'utilisateur et de savoir quelles lettres sont bien placées,
    mal placées ou non comprises dans le mot à chercher
    Entrée : - évènement qui est l'évènement du bind de lancement_sutom
    Sortie : - aucune
    """

    global vies
    global erreurs
    case = ''
    lettre = ''
    liste_user = []
    liste_mot_a_trouver = []
    mot_cherche = table_du_jeu[question]['Mot :'].upper()
    mot_user = document['sutom'].value.upper()
    mot_a_print = mot_cherche.lower()
    test = html.DIV(Class='div')
    if len(mot_user) < len(mot_cherche) or len(mot_user) > len(mot_cherche):
        document <= html.H2("Le nombre de lettres de votre mot doit être égal à celui inscrit", Class="lettre_mauvaise")
        if erreurs == vies - 1:
            defaite()
            document <= html.H4(f'Le bon mot était "{mot_a_print}"')
    elif mot_user != mot_cherche:
        if erreurs == vies - 1:
            defaite()
            document <= html.H4(f'Le bon mot était "{mot_a_print}"')
        else:

            for i in range(len(mot_user)):
                liste_user.append(mot_user[i])
                liste_mot_a_trouver.append(mot_cherche[i])
            for j in range(len(mot_cherche)):
                lettre += mot_user[j]

                if liste_user[j] == liste_mot_a_trouver[j]:
                    liste_mot_a_trouver[j] = 1   
                    case += '🟩'
                    
                elif liste_user[j] in liste_mot_a_trouver and liste_user[j] != liste_mot_a_trouver[j]:
                    liste_mot_a_trouver[liste_mot_a_trouver.index(mot_user[j])] = 2          
                    case += '🟨'    
                    
                elif liste_user[j] not in liste_mot_a_trouver:
                    case += '🟥'

            test <= html.DIV(html.H6(case), Class='case')
            test <= html.DIV(html.H6(lettre), Class='lettre')
            document <= test
    else:
        victoire()
    erreurs += 1


def victoire():

    """
    Crée une fonction nommée victoire qui permet d'afficher la page de
    victoire à l'utilisateur et son nombre d'erreurs ainsi que le bouton de
    rafraichissement
    Entrée : - aucune
    Sortie : - aucune
    """

    document['corps'].textContent = ''
    document <= html.H3("Bien joué, tu as gagné !! ")
    if erreurs == 1:
        document <= html.H3(f"Tu n'as fais qu'une erreur !")
    elif erreurs > 1:
        document <= html.H3(f"Tu as fais {erreurs} erreurs")
    else:
        document <= html.H3(f"Tu n'as pas fais d'erreurs ")
    document <= html.IMG(id="fin", src="https://p2.piqsels.com/preview/432/118/526/black-wallpaper-black-and-white-boxer-boxing.jpg", width="600", height="350")
    for _ in range(2):
        document <= html.BR()
    document <= html.BUTTON(" Rejoue !", Class='bouton', id='Rejouer')
    document['Rejouer'].bind('click', rafraichissement)


def defaite():

    """
    Crée une fonction nommée defaite qui permet d'afficher la page de
    defaite à l'utilisateur ainsi que le bouton de rafraichissement
    Entrée : - aucune
    Sortie : - aucune
    """

    document['corps'].textContent = ''
    document <= html.H3("Dommage, tu as perdu !! ")
    document <= html.IMG(id="fin", src="https://p2.piqsels.com/preview/582/204/910/guy-man-people-dark.jpg", width="600", height="370")
    for _ in range(3):
        document <= html.BR()
    document <= html.BUTTON(" Rejoue !", Class='bouton', id='Rejouer')
    document['Rejouer'].bind('click', rafraichissement)


def rafraichissement(évènement):

    """
    Crée une fonction nommée rafraichissement qui permet de rafraichir la page
    web
    Entrée : - évènement qui est l'évènement du bind de victoire ou de
    defaite
    Sortie : - aucune
    """

    document['Rejouer'] <= html.META(http_equiv="Refresh", content="0")

page_accueil()
