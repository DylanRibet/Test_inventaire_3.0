import csv

def est_nombre(valeur):
    try:
        # Essayer de convertir la valeur en entier
        int(valeur)
        return True
    except ValueError:
        # Retourner False si la conversion échoue
        return False

def modifier_csv(fichier_entree, fichier_sortie):
    # Réorganisation des colonnes : 'QTE' juste après 'CODE_BARRE'
    colonnes_utiles = ['CODE_BARRE', 'QTE', 'CONTRA', 'descript', 'MARQUE']
    
    with open(fichier_entree, mode='r', newline='', encoding='utf-8') as fichier_csv:
        lecteur = csv.DictReader(fichier_csv)
        
        # Créer une nouvelle liste pour les lignes filtrées
        lignes_filtrees = []
        
        for ligne in lecteur:
            # Vérifier si la colonne QTE existe, est un nombre et est supérieure à 0
            if est_nombre(ligne.get('QTE')) and int(ligne['QTE']) > 0:
                # Garder seulement les colonnes utiles
                ligne_filtre = {colonne: ligne[colonne] for colonne in colonnes_utiles}
                lignes_filtrees.append(ligne_filtre)
        
        # Écrire les données filtrées dans un nouveau fichier
        with open(fichier_sortie, mode='w', newline='', encoding='utf-8') as fichier_csv_modifie:
            auteur = csv.DictWriter(fichier_csv_modifie, fieldnames=colonnes_utiles)
            auteur.writeheader()
            auteur.writerows(lignes_filtrees)

# Exemple d'utilisation :
fichier_entree = '/Users/dylanrocaribet/Downloads/Inventaire/inventaire.csv'
fichier_sortie = '/Users/dylanrocaribet/Downloads/Inventaire/inventaire_modifie.csv'

modifier_csv(fichier_entree, fichier_sortie)