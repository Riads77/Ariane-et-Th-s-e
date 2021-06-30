from upemtk import *
from copy import deepcopy
import sys








"""
_______________________________________________________________________________________________________________________________________________________________________________________

Phase 1 :
_______________________________________________________________________________________________________________________________________________________________________________________

"""

def analys_syntax(fichier):
    """
    Fonction qui ouvre et lit un fichier texte par lignes,
    avant d'en extraire chaque caractères dans une liste.
    """
    
    ouvrir = open(fichier,"r")
    
    lire = ouvrir.readlines()
    
    n = int(lire[0]) #Dimensions du jeu
    labyrinthe = []
    
    for i in range(1, 2*n+2):
        laby = []
        for j in range(1,2*n+2):
            laby.append(lire[i][j])
        labyrinthe.append(laby)
    return labyrinthe,n
        
    
        


"""
_______________________________________________________________________________________________________________________________________________________________________________________

Phase 2 :
_______________________________________________________________________________________________________________________________________________________________________________________

"""

def ecran_chargement():
    """
    charge le menu principal du jeu permettant la selection des niveaux.
    """


    rectangle(200,200,300,300,remplissage = 'grey')
    rectangle(200,500,300,600,remplissage = 'orange')
    rectangle(500,200,600,300,remplissage = 'red')
    rectangle(500,500,600,600,remplissage = 'blue')
    texte(400,50,"ARIANE", taille=45, couleur="red", ancrage = 'center')
    texte(250,250,"CLASSIQUE", taille=13, ancrage = 'center' )
    texte(250,550,"BIG", taille=13, ancrage = 'center' )
    texte(550,250,"DEFI", taille=13, ancrage = 'center' )
    texte(550,550,"SMALL", taille=13, ancrage = 'center' )





def classique():
    """charge la selection des niveaux de type classique.
    """
    rectangle(750,350,800,400,remplissage = 'grey')
    texte(775,375,"Menu", taille=10, ancrage = 'center' )

    rectangle(200,150,300,250,remplissage = 'grey')
    rectangle(200,350,300,450,remplissage = 'grey')
    rectangle(200,550,300,650,remplissage = 'grey')
    rectangle(500,150,600,250,remplissage = 'grey')
    rectangle(500,350,600,450,remplissage = 'grey')
    rectangle(500,550,600,650,remplissage = 'grey')
    
    texte(250,200,"Niveau 1", taille=13, ancrage = 'center' )
    texte(250,400,"Niveau 2", taille=13, ancrage = 'center' )
    texte(250,600,"Niveau 3", taille=13, ancrage = 'center' )
    texte(550,200,"Niveau 4", taille=13, ancrage = 'center' )
    texte(550,400,"Niveau 5", taille=13, ancrage = 'center' )
    texte(550,600,"Bac à sable", taille=13, ancrage = 'center' )

def big():
    """charge la selection des niveaux de type big
    """
    rectangle(750,350,800,400,remplissage = 'orange')
    texte(775,375,"Menu", taille=10, ancrage = 'center' )

    rectangle(200,350,300,450,remplissage = 'orange')
    rectangle(500,350,600,450,remplissage = 'orange')
    
    texte(250,400,"Niveau 1", taille=13, ancrage = 'center')
    texte(550,400,"Niveau 2", taille=13, ancrage = 'center' )

def defi():
    """charge la selection des niveaux de type defi
    """
    rectangle(750,350,800,400,remplissage = 'red')
    texte(775,375,"Menu", taille=10, ancrage = 'center' )

    rectangle(200,200,300,300,remplissage = 'red')
    rectangle(200,500,300,600,remplissage = 'red')
    rectangle(500,200,600,300,remplissage = 'red')
    rectangle(500,500,600,600,remplissage = 'red')

    texte(250,250,"Niveau 1", taille=13, ancrage = 'center' )
    texte(250,550,"Niveau 2", taille=13, ancrage = 'center' )
    texte(550,250,"Niveau 3", taille=13, ancrage = 'center' )
    texte(550,550,"Niveau 4", taille=13, ancrage = 'center' )

def small():
    """charge la selection des niveaux de type small
    """
    rectangle(750,350,800,400,remplissage = 'blue')
    texte(775,375,"Menu", taille=10, ancrage = 'center' )

    rectangle(200,200,300,300,remplissage = 'blue')
    rectangle(200,500,300,600,remplissage = 'blue')
    rectangle(500,200,600,300,remplissage = 'blue')
    rectangle(500,500,600,600,remplissage = 'blue')

    texte(250,250,"Niveau 1", taille=13, ancrage = 'center' )
    texte(250,550,"Niveau 2", taille=13, ancrage = 'center' )
    texte(550,250,"Niveau 3", taille=13, ancrage = 'center' )
    texte(550,550,"Niveau 4", taille=13, ancrage = 'center' )

def type_niveau(x,y):
    """
    verifie la coordonnée ou l'utilisateur a cliqué.
    Si cette coordonnée correspond à l'un des rectangles correspondant à un type de niveau,
    retourne une chaîne de caractère correspondant au type de niveau choisi.
    """
    if 200 <= x <= 300:
        if 200 <= y <= 300:
            return "CLASSIQUE"
        elif 500 <= y <= 600:
            return "BIG"
    elif 500 <= x <= 600:
        if 200 <= y <= 300:
            return "DEFI"
        elif 500 <= y <= 600:
            return "SMALL"
    return None

def choix_niveaux(x,y,niveau_type):
    """
    fonction similaire à type_niveau, mais pour des rectangles représentant plusieurs niveaux, 
    en fonction du type de niveau choisi.
    renvoie le fichier correspondant au niveau. 
    """

    if niveau_type == "CLASSIQUE":
        if 200 <= x <= 300:
            if 150 <= y <= 250:
                return "maps/labyrinthe1.txt"
            elif 350 <= y <= 450:
                return "maps/labyrinthe2.txt"
            elif 550 <= y <= 650:
                return "maps/labyrinthe3.txt"
        elif 500 <= x <= 600:
            if 150 <= y <= 250:
                return "maps/labyrinthe4.txt"
            elif 350 <= y <= 450:
                return "maps/labyrinthe5.txt"
            elif 550 <= y <= 650:
                return "maps/sandbox.txt"

   
    
    elif niveau_type == "BIG":
        if 350 <= y <= 450:
            if 200 <= x <= 300:
                return "maps/big/big1.txt"
            elif 500 <= x <= 600: 
                return "maps/big/big2.txt"
   
   
    elif niveau_type == "DEFI":
        if 200 <= x <= 300:
            if 200 <= y <= 300:
                return "maps/defi/defi0.txt"
            elif 500 <= y <= 600:
                return "maps/defi/defi1.txt"
        elif 500 <= x <= 600:
            if 200 <= y <= 300:
                return "maps/defi/defi2.txt"
            elif 500 <= y <= 600:
                return "maps/defi/defi3.txt"
   

    elif niveau_type == "SMALL":
        if 200 <= x <= 300:
            if 200 <= y <= 300:
                return "maps/small/small1.txt"
            elif 500 <= y <= 600:
                return "maps/small/small2.txt"
        elif 500 <= x <= 600:
            if 200 <= y <= 300:
                return "maps/small/small3.txt"
            elif 500 <= y <= 600:
                return "maps/small/small4.txt"

    return None

def affichage(z):

    """
    fonction d'affichage du labyrinthe. Elle  procède par balayage de la matrice labyrinthe, et en fonction du type de caractère,
    va afficher sur la fenêtre une ligne correspondant à un mur, ou une image représentant un personnage.
    Cette fonction renvoie les coordonnées d'Ariane, ainsi que celles des minotaures verticaux et horizontaux.
    """
    rectangle(700,450,800,500,remplissage = 'grey')
    texte(740,475,"Paramètres", taille=10, ancrage = 'center' )

    rectangle(750,350,800,400,remplissage = 'grey')
    texte(775,375,"Menu", taille=10, ancrage = 'center' )

    rectangle(750,250,800,300,remplissage = 'grey')
    texte(775,275,"Annuler", taille=10, ancrage = 'center' )

    x, y  = 25,5
    lignes, colonnes = 0, 0
    ariane = None
    mino_vertical = []
    mino_horizontal = []
    coordonnees = None
    for i in labyrinthe:
        colonnes = 0
        for j in i: 
            if j == '-' :
                ligne(x-z,y,x+z,y,couleur='black')      
            elif j == '|' :
                ligne(x,y-z,x,y+z,couleur='black')
            if j == 'P' or j == 'PV' or j == 'PH' or j == 'PA':
                image(x,y,'media/porte.png')    
            if j == 'H' or j == 'PH':
                image(x,y,'media/minoH.png')
                coordonnees = (lignes, colonnes)
                mino_horizontal.append(coordonnees)
            if j == 'V' or j == 'PV':
                image(x,y,'media/minoV.png')
                coordonnees = (lignes, colonnes)
                mino_vertical.append(coordonnees)
            elif j == 'T' and Thesee == False:
                image(x,y,'media/thesee.png')
            if j == 'A' or j == 'PA':
                image(x,y,'media/ariane.png')
                ariane = (lignes, colonnes)
                if Thesee == True:
                    image(x,y,'media/thesee.png')

            x += z
            colonnes += 1

        lignes += 1
        x = 25
        y += z
    return ariane, mino_vertical, mino_horizontal


def ecran_victoire():
    """
    Cette fonction renvoie l'écran de victoire, avec le mot "VICTOIRE", ainsi qu'un rectangle nous dirigeant au menu des niveaux.
    """
    texte(400,400, "VICTOIRE !",couleur='gold', taille = "60",ancrage='center')
    rectangle(300,550,500,600,remplissage = 'grey')
    texte(400,575,"niveaux",taille = "13",ancrage='center')

def ecran_defaite():
    """
    fonction renvoyant l'écran de defaite, et affichant les trois possibilités au joueur qui sont de réessayer, de 
    changer de niveau ou de quitter.
    """

    texte(400,400, "DEFAITE !",couleur='purple1', taille = "60",ancrage='center')
    rectangle(300,475,500,525,remplissage = 'grey')
    rectangle(300,550,500,600,remplissage = 'grey')
    rectangle(300,625,500,675,remplissage = 'grey')
    texte(400,500,"Réessayer",taille = "13",ancrage='center')
    texte(400,575,"Niveaux",taille = "13",ancrage='center')
    texte(400,650,"Quitter",taille = "13",ancrage='center')

def ecran_parametre(dim):
    """
    Affichage paramètres : réessayer, niveaux, quitter, dimensions.
    """
    rectangle(300,275,500,325,remplissage = 'grey')
    rectangle(300,350,500,400,remplissage = 'grey')
    rectangle(300,425,500,475,remplissage = 'grey')

    rectangle(300,500,350,550,remplissage = 'grey')
    rectangle(450,500,500,550,remplissage = 'grey')

    rectangle(700,350,800,400,remplissage = 'grey')

    texte(400,300,"Recommencer",taille = "13",ancrage='center')
    texte(400,375,"Niveaux",taille = "13",ancrage='center')
    texte(400,450,"Dimensions",taille = "13",ancrage='center')

    texte(325,525,"<",taille = "13",ancrage='center')
    texte(475,525,">",taille = "13",ancrage='center')
    texte(400,525,dim,taille = "13",ancrage='center')

    texte(740,375,'Confirmer',taille = "13",ancrage='center')


def direction(type_touche):
    """
    Fonction qui en fonction du bouton où le joueur a appuyé, va renvoyer une liste de coordonnées, définissant la direction prise par Ariane.
    """
    x, y = 0, 0
    if type_touche == 'Left':
        y = -1
    elif type_touche == 'Right':
        y = 1
    elif type_touche == 'Up':
        x = -1
    elif type_touche == 'Down':
        x = 1
    return [x, y]


def moyenne(x, y):
    """
    renvoie la moyenne de deux entiers.
    """
    return (x+y)//2

def mur(x, y):
    """
    verifie une chaine de caractere précise dans le labyrinthe. Si celle-ci correspond à un obstacle,
    (mur ou minotaure), cette fonction renvoie False, et True dans le cas contraire. 
    Cette fonction a pour but d'éviter les déplacements non valides.
    """
    if labyrinthe[x][y] in ['|','-','H','V']:
        return False

    return True 


def minotaure_verticaux_deplacement(ariane, mino_verti):
    """
    Fonction utilisant minotaure_verticaux_detection et qui en cas de détection d'Ariane, va changer la coordonnée des minotaures en fonction des règles:
    si le minotaure est sur la même ligne, va se rapprocher d'Ariane jusqu'à avoir la même coordonnée, ou être stoppé par un obstacle, grâce à la fonction mur.
    Sinon, le minotaure, si la fonction mur lui permet, se place sur la même ligne sans changer de colonne.
    renvoie les coordonnées finales des minotaures.
    """
    mino_verti_nouveau = deepcopy(mino_verti)
    for i in range(len(mino_verti_nouveau)):
        if ariane[0] == mino_verti_nouveau[i][0]:
            while ariane != mino_verti_nouveau[i]:
                if mino_verti_nouveau[i][1] < ariane[1]:
                    avancee = mino_verti_nouveau[i][1]+2
                else:
                    avancee = mino_verti_nouveau[i][1]-2
                obstacle_eventuel = moyenne(mino_verti_nouveau[i][1],avancee)
                if mur(mino_verti_nouveau[i][0],obstacle_eventuel) is False or mur(mino_verti_nouveau[i][0],avancee) is False:
                    break
                mino_verti_nouveau[i] = (mino_verti_nouveau[i][0],avancee)
        else:
            if mino_verti_nouveau[i][0] < ariane[0]:
                if mur(mino_verti_nouveau[i][0]+1, mino_verti_nouveau[i][1]) is True and mur(mino_verti_nouveau[i][0]+2, mino_verti_nouveau[i][1]) is True :    
                    mino_verti_nouveau[i] = (mino_verti_nouveau[i][0]+2,mino_verti_nouveau[i][1])
            if mino_verti_nouveau[i][0] > ariane[0]:
                if mur(mino_verti_nouveau[i][0]-1, mino_verti_nouveau[i][1]) is True and mur(mino_verti_nouveau[i][0]-2, mino_verti_nouveau[i][1]) is True :    
                    mino_verti_nouveau[i] = (mino_verti_nouveau[i][0]-2,mino_verti_nouveau[i][1])
    return mino_verti_nouveau


def minotaure_horizontaux_deplacement(ariane, mino_hori):
    """
    l'équivalent de minotaure_verticaux_deplacement pour les horizontaux, utilisant minotaure_horizontaux_detection, et applique les règles sur les lignes aux colonnes et inversement.
    """
    mino_hori_nouveau = deepcopy(mino_hori)
    for i in range(len(mino_hori_nouveau)):
        if ariane[1] == mino_hori_nouveau[i][1]:
            while ariane != mino_hori_nouveau[i]:
                if mino_hori_nouveau[i][0] < ariane[0]:
                    avancee = mino_hori_nouveau[i][0]+2
                else:
                    avancee = mino_hori_nouveau[i][0]-2
                obstacle_eventuel = moyenne(mino_hori_nouveau[i][0],avancee)
                if mur(obstacle_eventuel,mino_hori_nouveau[i][1]) is False or mur(avancee, mino_hori_nouveau[i][1]) is False:
                    break
                mino_hori_nouveau[i] = (avancee,mino_hori_nouveau[i][1])
        else:
            if mino_hori_nouveau[i][1] < ariane[1]:
                if mur(mino_hori_nouveau[i][0], mino_hori_nouveau[i][1]+1) is True and mur(mino_hori_nouveau[i][0], mino_hori_nouveau[i][1]+2) is True:    
                    mino_hori_nouveau[i] = (mino_hori_nouveau[i][0],mino_hori_nouveau[i][1]+2)
            if mino_hori_nouveau[i][1] > ariane[1]:
                if mur(mino_hori_nouveau[i][0], mino_hori_nouveau[i][1]-1) is True and mur(mino_hori_nouveau[i][0], mino_hori_nouveau[i][1]-2) is True:    
                    mino_hori_nouveau[i] = (mino_hori_nouveau[i][0],mino_hori_nouveau[i][1]-2)
    return mino_hori_nouveau



"""
_______________________________________________________________________________________________________________________________________________________________________________________

Phase 3 :
_______________________________________________________________________________________________________________________________________________________________________________________
"""


"""
def backtracking(laby_simulation, config_visitees,victoire,defaite,statut_jeu):

    if victoire == True:
        return 'Vrai'


    Thesee_is_dead = False
    mino_vertical = []
    mino_horizontal = []
    for i in range(len(laby_simulation)):
        if 'PTA' in laby_simulation[i]:
            return 'Vrai'
        colonne = 0
        for j in laby_simulation[i]:    
            if j == 'H' or j == 'PH':
                coordonnees = (i, colonne)    
                mino_horizontal.append(coordonnees)
            if j == 'V' or j == 'PV':
                coordonnees = (i, colonne)
                mino_vertical.append(coordonnees)
            if j == 'A' or j == 'PA' or j =='TA':
                ariane = (i, colonne)
            colonne += 1



    for i in range(len(mino_vertical)):
        verti_detect.append(False)

    for i in range(len(mino_horizontal)):
        hori_detect.append(False)

    vertical_detect = minotaure_verticaux_detection(ariane, mino_vertical, verti_detect)
    horizontal_detect = minotaure_horizontaux_detection(ariane, mino_horizontal, hori_detect)
    


    configuration = deepcopy(laby_simulation)
    config_visitees.append(deepcopy(configuration))
         
    obstacle_adjac = [(ariane[0],ariane[1]-1),(ariane[0],ariane[1]+1),(ariane[0]-1,ariane[1]),(ariane[0]+1,ariane[1])]
    case_adjac = [(ariane[0],ariane[1]-2),(ariane[0],ariane[1]+2),(ariane[0]-2,ariane[1]),(ariane[0]+2,ariane[1])]
    
    for case in case_adjac:
        i = case_adjac.index(case)
        if mur(obstacle_adjac[i][0],obstacle_adjac[i][1]) is True:
            if laby_simulation[case[0]][case[1]] in ['H','V']:
                return False
            if mur(case[0],case[1]) is True:
                if configuration[case[0]][case[1]] == 'T':
                    configuration[case[0]][case[1]] = 'TA'

                if configuration[case[0]][case[1]] == 'P':
                    if configuration[ariane[0]][ariane[1]] == 'TA':
                        configuration[case[0]][case[1]] = 'PTA'
                    else:
                        configuration[case[0]][case[1]] = 'PA'
                elif configuration[ariane[0]][ariane[1]] == 'TA':
                    configuration[case[0]][case[1]] = 'TA'
                else:
                    configuration[case[0]][case[1]] = 'A'

                if configuration[ariane[0]][ariane[1]] == 'PA':
                    configuration[ariane[0]][ariane[1]] = 'P'
                else:
                    configuration[ariane[0]][ariane[1]] = ' '

                  

                ariane = case

                vertical_detect = minotaure_verticaux_detection(ariane, mino_vertical, verti_detect)
                horizontal_detect = minotaure_horizontaux_detection(ariane, mino_horizontal, hori_detect)

                mino_vertical_nouveau = minotaure_verticaux_deplacement(ariane, mino_vertical, vertical_detect)
                for i in range(len(mino_vertical)):
                    
                    if configuration[mino_vertical[i][0]][mino_vertical[i][1]] == 'PV':
                        configuration[mino_vertical[i][0]][mino_vertical[i][1]] = 'P'
                    else:
                        configuration[mino_vertical[i][0]][mino_vertical[i][1]] = ' '
                    if configuration[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] == 'P':
                        configuration[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] = 'PV'
                    else:
                        configuration[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] = 'V'

                mino_vertical = mino_vertical_nouveau

                mino_horizontal_nouveau = minotaure_horizontaux_deplacement(ariane, mino_horizontal, horizontal_detect)

                for i in range(len(mino_horizontal)):
                    
                    if configuration[mino_horizontal[i][0]][mino_horizontal[i][1]] == 'PH':
                        configuration[mino_horizontal[i][0]][mino_horizontal[i][1]] = 'P'
                    else:
                        configuration[mino_horizontal[i][0]][mino_horizontal[i][1]] = ' '
                    if configuration[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] == 'P':
                        configuration[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] = 'PH'
                    else:
                        configuration[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] = 'H'
                        
                mino_horizontal = mino_horizontal_nouveau

                
                for i in range(len(configuration)):
                    if 'T' in configuration[i] or 'TA' in configuration[i] or  'PTA' in configuration[i] :
                        break
                    elif i == len(configuration)-1:
                        Thesee_is_dead = True
                
                        


                if ariane in mino_horizontal or ariane in mino_vertical or Thesee_is_dead == True:
                    defaite += 1
                    return 'Faux'




                
                if configuration not in config_visitees:
                    laby_simulation = deepcopy(configuration)

                    config_visitees.append(configuration)

                recurs = backtracking(laby_simulation,config_visitees, victoire, defaite,statut_jeu)
                defaite.append(recurs)
    if 'Vrai' not in defaite:
        return 'Faux'



"""




"""
_______________________________________________________________________________________________________________________________________________________________________________________

Programme Principal :
_______________________________________________________________________________________________________________________________________________________________________________________
"""


cree_fenetre(800, 800)

stay_true = False

"""
niveau_type correspond dans le menu à une chaîne de caractère définissant le type de niveau choisi par l'utilisateur
niveau_choisi correspond aussi à un string, mais dans la selection de niveau. Il sera le string du niveau choisi...
"""
niveau_type = None 
niveau_choisi = None

"""
statut_jeu évolue en fonction du menu où veut aller l'utilisateur.
Si sa valeur est 'menu', alors le jeu chargera l'écran du menu tant que cette valeur sera inchangée. 
Même principe pour tout les écrans possibles
"""

statut_jeu = None
dim = 30 #dimensions initiales du jeu.

"""
La boucle while True ne fait pas seulement durer le jeu ici, mais tout le programme, permettat de recommencer une partie, et revenir dans le menu.
"""
while True:
    ariane = None



    """
    Les conditions boléennes et fin : -victory devient True, si Ariane atteint la porte avec Thésée. Alors statut_jeu change et passe du jeu à l'écran de victoire.
    -Thesee devient True si Ariane se met au niveau de sa coordonnée. Il ne peut redevenir False que si la position est annulée et qu'Ariane ne l'a pas encore récupéré.
    Cette condition est nécessaire pour la victoire.
    Thesee_est_mort est vrai seulement si Thesee est False, mais que sa représentation 'T' est absente du labyrinthe. Comme Ariane ne l'a pas pris, alors un minotaure l'a mangé.
    Cette condition conduit à la défaite.
    fin prend la valeur de 'Victory' ou de 'Loose' si la partie se finit, et adapte la valeur de statut_jeu en fonction de la sienne. 
    """
    victory = False
    Thesee = False
    Thesee_est_mort = False
    fin = None
    


    """
    statut_jeu est par défaut conduit au menu.
    Si l'utilisateur veut quitter, et que statut_jeu == 'Exit', la boucle se brise et le jeu prend fin.
    """
    if statut_jeu == None:
        statut_jeu = 'menu'
    elif statut_jeu == 'Exit':
        break


    """
    quand le statut du jeu est le menu principal, l'écran du menu principal est affiché.
    Le joueur peut uniquement cliquer sur le menu ou le quitter. Dans le deuxième cas, statut_jeu devient exit et cette boucle se finit. Comm statut_jeu est 'Exit', cela ferme le programme.
    Si le joueur clique sur le menu, s'il clique sur des coordonnées correspondant aux rectangles de hoix de niveau, le statut de jeu changera en selection de niveau, et niveau_type aura le nom de
    l'un des types de niveau. Si on clique n'importe où, rien ne se passe.
    """
    while statut_jeu == 'menu':
        efface_tout()
        ecran_chargement()

        ev = donne_evenement()
        ty = type_evenement(ev)

        if ty == 'ClicGauche':
            niveau_type = type_niveau(clic_x(ev),clic_y(ev))
            if niveau_type != None:
                statut_jeu = 'selection_niveau'

        if ty == 'Quitte':
            statut_jeu = 'Exit'  

        mise_a_jour()

    """
    Boucle similaire à la précédente, celle-ci va observer la valeur de niveau_type et charger une grille de niveau en fonction.
    même principe que pour le menu principal, mais si on clique sur l'un des rectangles, c'est la valeur de niveau_choisi qui change prenant le nom de l'un des fichiers txte maps,
    l'un des niveaux donc. le statut du jeu est dirigé vers le jeu. 

    """

    while statut_jeu == 'selection_niveau' :
        efface_tout()
        if niveau_type == "CLASSIQUE":
            classique()
        elif niveau_type == "BIG":
            big()
        elif niveau_type == "DEFI":
            defi()
        elif niveau_type == "SMALL":
            small()

        ev = donne_evenement()
        ty = type_evenement(ev)

        if ty == 'ClicGauche':

            if 750 <= clic_x(ev) <= 800 and 350 <= clic_y(ev) <= 400:
                statut_jeu = 'menu'
                break

            niveau_choisi = choix_niveaux(clic_x(ev),clic_y(ev),niveau_type)
            if niveau_choisi != None:
                statut_jeu = 'préjeu'
        if ty == 'Quitte':
            statut_jeu = 'Exit'

        mise_a_jour()

    """
    statut juste avant le jeu où le fichier texte est converti en matrice grâce à l'analyseur syntaxique.
    Permet la réinitialisation d'un niveau à la fin d'une partie. Evite l'apparition perpétuelle d'écrans de victoire ou de défaite.
    """
    if statut_jeu == 'préjeu':
        labyrinthe = analys_syntax(niveau_choisi)[0]
        n = analys_syntax(niveau_choisi)[1]
        
        historique = [deepcopy(labyrinthe)] #liste des configurations du labyrinthe à chaque coup joué. 
        statut_jeu = 'jeu'


    """
    Boucle principale du jeu. Tant que le joueur ne quitte pas la partie et ferme le programme où ne termine pas une partie (par l'une des deux issues possibles.),
    le jeu tournera. 
    """
    while statut_jeu == 'jeu':

        efface_tout()

        """
        Afin de ne pas laisser les paramètres changer le statut de Thésée.
        """
        if stay_true == True:
            Thesee = True

        #solveur = backtracking(laby_simulation, config_visitees, victoire, defaite, statut_jeu)
        """
        le jeu s'affiche tout en actualisant les données des personnages mouvants.
        """
        ariane = affichage(dim)[0]
        mino_vertical = affichage(dim)[1]
        mino_horizontal = affichage(dim)[2]
        

        """
        Vérification des conditions de victoire, mettant fin à une partie en changeant juste la valeur de statut_jeu.
        """ 
        for i in range(len(labyrinthe)):
            if 'PA' in labyrinthe[i] and Thesee == True:
                victory = True
                break
        if victory is True:
            fin = 'Victory'
            statut_jeu = 'fin'
            break

        

        
        ev = donne_evenement()
        ty = type_evenement(ev)
        

        """
        Si l'utilisateur clique, en principe, rien ne se passe, sauf s'il appuie sur le bouton menu, qui le renvoie au menu,
        ou sur le bouton annuler, qui va affecter l'avant-dernière valeur de l'historique au labyrinthe et supprimer la dernière, 
        revenant donc au coup d'avant.
        """
        if ty == 'ClicGauche':
            if 750 <= clic_x(ev) <= 800 and 350 <= clic_y(ev) <= 400:
                statut_jeu = 'menu'

            if 700 <= clic_x(ev) <= 800 and 450 <= clic_y(ev) <= 500:
                statut_jeu = 'Paramètres'

            if 750 <= clic_x(ev) <= 800 and 250 <= clic_y(ev) <= 300:
                if not len(historique) == 1:
                    labyrinthe = historique[len(historique)-2]
                    historique.pop(len(historique)-1)
                    for i in range(len(labyrinthe)):
                        if 'T' in labyrinthe[i]:
                            Thesee = False
                            stay_true = False
                            break

        """
        Provoque la fin de la boucle puis du programme si ty == Quitte.
        
        En principe, si l'évènement est une touche, rien ne se passe, sauf pour les touches directionnelles.
        En fonction de la touche directionnelle, la fonction direction va renvoyer un couple d'entier rerésentant le déplacement d'Ariane. Si possible, ses coordonnées 
        vont changer et toutes les conséquences de son déplacement vont suivre.
        
        """
        if ty == 'Quitte':
            statut_jeu = 'Exit'

        
        elif ty == 'Touche':
            type_touche = touche(ev)
            action = direction(type_touche)
            if action[0] != 0 or action[1] != 0:
                lign, colonne = ariane[0], ariane[1]
                lign += action[0]
                colonne += action[1]
                if mur(lign, colonne) == True: #Vérification de l'absence de mur... sinon Ariane ne peut passer et l'évènement s'annule.
                    lign += action[0]
                    colonne += action[1]
                    if labyrinthe[lign][colonne] == 'V' or labyrinthe[lign][colonne] == 'H':
                        fin = 'Loose'
                        statut_jeu = 'fin'
                        break
                    if mur(lign, colonne) == True: #Deuxième vérification évitant à Ariane d'arriver sur un minotaure (en principe cas impossible), mais surtout de traverser le labyrinthe et d'arriver de l'autre côté.
                        adjac = [None,None,None,None]
                        obstacle_thesee = [None,None,None,None]
                        if not lign-2<0:
                            adjac[0] = (labyrinthe[lign-2][colonne])
                            coord = (lign-1,colonne)
                            obstacle_thesee[0] = (coord)
                        if not lign+2>len(labyrinthe)-1:
                            adjac[1] = (labyrinthe[lign+2][colonne])
                            coord = (lign+1,colonne)
                            obstacle_thesee[1] = (coord)
                        if not colonne-2<0:
                            adjac[2] = (labyrinthe[lign][colonne-2])
                            coord = (lign,colonne-1)
                            obstacle_thesee[2] = (coord)
                        if not colonne+2>len(labyrinthe)-1:
                            adjac[3] = (labyrinthe[lign][colonne+2])
                            coord = (lign,colonne+1)
                            obstacle_thesee[3] = (coord)
                        for i in range(len(adjac)):
                            if 'T' == adjac[i]:
                                if mur(obstacle_thesee[i][0], obstacle_thesee[i][1]) == True:
                                    Thesee = True #Ariane arrive sur le 'T' de Thésée, donc la condition Thésée est verifiée.
                        if labyrinthe[ariane[0]][ariane[1]] == 'PA': #Si Ariane était sur la porte, on remet la lettre correpondant à la porte sans Ariane.
                            labyrinthe[ariane[0]][ariane[1]] = 'P'
                        else:
                            labyrinthe[ariane[0]][ariane[1]] = ' ' #La case d'ou vient Ariane devient un string vide. La fonction affichage de la prendra plus en compte.
                        if labyrinthe[lign][colonne] == 'P':
                            labyrinthe[lign][colonne] = 'PA' #Si Ariane arrive sur la porte, et que Thesee est faux, le jeu continue. Dans le cas de 'PA', l'image d'Ariane se superpose à celle de la porte dans affichage()
                        else:
                            labyrinthe[lign][colonne] = 'A' #Ariane arrive sur une case. La lettre qui lui est afiliée doit y être présente, pour que la fonction affichage y mette son image.
                        ariane = (lign, colonne) #Ajustement des coordonnées d'Ariane, utile pour le déplacement des minotaures.
                        
                    
                    

                        """
                        Déplacement des minotaures. Comme pour Ariane, leur ancienne coordonnée affiche le caractère '' et le nouveau 'H' ou 'V'.
                        Dans le cas où ils traversent la porte, comme pour Ariane, leur image se superpose à elle en créant 'PV' ou 'PH'
                        """

                        mino_vertical_nouveau = minotaure_verticaux_deplacement(ariane, mino_vertical)
                        
                        
                        for i in range(len(mino_vertical)):
                            if labyrinthe[mino_vertical[i][0]][mino_vertical[i][1]] == 'PV':
                                labyrinthe[mino_vertical[i][0]][mino_vertical[i][1]] = 'P'
                            else:
                                labyrinthe[mino_vertical[i][0]][mino_vertical[i][1]] = ' '
                            if labyrinthe[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] == 'P':
                                labyrinthe[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] = 'PV'
                            else:
                                labyrinthe[mino_vertical_nouveau[i][0]][mino_vertical_nouveau[i][1]] = 'V'

                        mino_vertical = mino_vertical_nouveau

                        mino_horizontal_nouveau = minotaure_horizontaux_deplacement(ariane, mino_horizontal)

                        for i in range(len(mino_horizontal)):
                            
                            if labyrinthe[mino_horizontal[i][0]][mino_horizontal[i][1]] == 'PH':
                                labyrinthe[mino_horizontal[i][0]][mino_horizontal[i][1]] = 'P'
                            else:
                                labyrinthe[mino_horizontal[i][0]][mino_horizontal[i][1]] = ' '
                            if labyrinthe[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] == 'P':
                                labyrinthe[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] = 'PH'
                            else:
                                labyrinthe[mino_horizontal_nouveau[i][0]][mino_horizontal_nouveau[i][1]] = 'H'
                        
                        mino_horizontal = mino_horizontal_nouveau
                        

                        """
                        Tant que Thesee est False, celui-ci est censé être présent dans le labyrinthe sous la forme 'T'.
                        Dans le cas contraire, on en déduit sa mort à cause d'un minotaure.
                        """
                        if Thesee == False:
                            for i in range(len(labyrinthe)):
                                if 'T' in labyrinthe[i]:
                                    break
                                elif i == len(labyrinthe)-1:
                                    Thesee_est_mort = True


                        """
                        Si avec la condition précédente, Thesee_est_mort, ou si ariane a la même cordonnée que l'un des minotaures, alors on affecte 'Loose' à fin et 
                        statut_jeu change, ce qui termine la boucle de cette partie. Sinon le jeu continue et la nouvelle configuration du jeu est ajoutée à l'historique.
                        """
                        if ariane in mino_horizontal or ariane in mino_vertical or Thesee_est_mort == True:
                            
                            fin = 'Loose'
                            statut_jeu = 'fin'
                            break

                        historique.append(deepcopy(labyrinthe))
                        

        mise_a_jour()
    """
    Ce statut est provisoire est observe juste s'il y a victoire ou défaite en fonction de fin. statut_jeu changera en fonction de fin.
    """
    if statut_jeu == 'fin':
        stay_true = False
        if fin == 'Victory':
            statut_jeu = 'Victoire'
        if fin == 'Loose':
            statut_jeu = 'Défaite'

    """
    fin = 'Victory'
    Vous avez gagné.
    Le jeu affiche un écran de victoire. 
    Vous pouvez juste quitter le jeu ou appuyer sur le bouton niveaux et revenir à la sélection de niveaux.
    """
    while statut_jeu == 'Victoire':
        efface_tout()
        ecran_victoire()

        ev = donne_evenement()
        ty = type_evenement(ev)

        if ty == 'Touche':
            type_touche = touche(ev)
            if type_touche == 'Return':
                statut_jeu = 'préjeu'

        if ty == 'ClicGauche':
            if 300 <= clic_x(ev) <= 500 and 550 <= clic_y(ev) <= 600:
                statut_jeu = 'selection_niveau'

        if ty == 'Quitte':
            statut_jeu = 'Exit'

        mise_a_jour()

    """
    fin = 'Loose'
    Vous avez perdu.
    Le jeu affiche un écran de défaite. 
    Vous pouvez juste quitter le jeu ou appuyer sur l'un des boutons.
    Le premier, réessayer transforme statut_jeu en préjeu et réinitialise le niveau, puis relance une partie.
    Le deuxième, niveaux, transforme statut_jeu en choix niveaux et renvoie à la sélection de niveaux.
    Le troisième, quitter, termine le programme avec statut_jeu == 'Exit'

    """
    while statut_jeu == 'Défaite':  



        efface_tout()
        ecran_defaite()

        ev = donne_evenement()
        ty = type_evenement(ev)

        if ty == 'Touche':
            type_touche = touche(ev)
            if type_touche == 'Return':
                
                statut_jeu = 'préjeu'

        if ty == 'ClicGauche':
            if 300 <= clic_x(ev) <= 500 and 475 <= clic_y(ev) <= 525:
                statut_jeu = 'préjeu'
            if 300 <= clic_x(ev) <= 500 and 550 <= clic_y(ev) <= 600:
                statut_jeu = 'selection_niveau'
            if 300 <= clic_x(ev) <= 500 and 625 <= clic_y(ev) <= 675:
                statut_jeu = 'Exit'
        if ty == 'Quitte':
            statut_jeu = 'Exit'

        mise_a_jour()

    while statut_jeu =='Paramètres':
        stay_true = False
        
        
        efface_tout()
        ecran_parametre(dim)

        ev = donne_evenement()
        ty = type_evenement(ev)

        if ty == 'Quitte':
            statut_jeu = 'Exit'

        if ty == 'ClicGauche':
            if 300 <= clic_x(ev) <= 500 and 275 <= clic_y(ev) <= 325:
                statut_jeu = 'préjeu'
            if 300 <= clic_x(ev) <= 500 and 350 <= clic_y(ev) <= 400:
                statut_jeu = 'selection_niveau'
            if 500 <= clic_y(ev) <= 550:
                if 300 <= clic_x(ev) <= 350:
                    if dim > 14:
                        dim -= 2
                if 450 <= clic_x(ev) <= 500:
                    if dim < 42:
                        dim += 2

            if 700 <= clic_x(ev) <= 800 and 350 <= clic_y(ev) <= 400: 
                if Thesee == True:
                    stay_true = True
                statut_jeu = 'jeu'

            
        mise_a_jour()

ferme_fenetre()
  