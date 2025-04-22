import os

CHEMIN = os.path.join(os.path.dirname(__file__), '..', 'fichiers')

# Fonctions Transport (S_lec, S_ecr)
def lire_S_lec():
    path = os.path.join(CHEMIN, 'S_lec.txt')
    with open(path, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

def ecrire_S_ecr(contenu):
    path = os.path.join(CHEMIN, 'S_ecr.txt')
    with open(path, 'a') as f:
        f.write(f"{contenu}\n")

# Fonctions Liaison (L_lec, L_ecr)
def lire_L_lec():
    path = os.path.join(CHEMIN, 'L_lec.txt')
    with open(path, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

def ecrire_L_ecr(contenu):
    path = os.path.join(CHEMIN, 'L_ecr.txt')
    with open(path, 'a') as f:
        f.write(f"{contenu}\n")

# Fonction pour vider les fichiers résultats (pratique pour tests)
def vider_fichiers():
    for fichier in ['S_ecr.txt', 'L_ecr.txt']:
        path = os.path.join(CHEMIN, fichier)
        open(path, 'w').close()
    
def ecrire_L_lec(contenu):
    path = os.path.join(CHEMIN, 'L_lec.txt')
    with open(path, 'a') as f:
        f.write(f"{contenu}\n")

def vider_L_lec():
    path = os.path.join(CHEMIN, 'L_lec.txt')
    open(path, 'w').close()
