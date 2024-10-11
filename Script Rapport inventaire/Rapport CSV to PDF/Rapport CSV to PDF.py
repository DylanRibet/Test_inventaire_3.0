import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def csv_to_pdf(fichier_csv, fichier_pdf):
    # Lire le fichier CSV
    df = pd.read_csv(fichier_csv)

    # Créer un PDF
    c = canvas.Canvas(fichier_pdf, pagesize=letter)
    largeur, hauteur = letter

    # Ajouter un titre
    c.drawString(100, hauteur - 40, "Rapport CSV")

    # Ajuster la position de départ
    y_position = hauteur - 80
    x_positions = [100, 200, 300, 400]  # Positions des colonnes

    # Écrire les en-têtes de colonne
    for idx, col in enumerate(df.columns):
        c.drawString(x_positions[idx], y_position, col)
    
    y_position -= 20  # Espacement après les en-têtes

    # Écrire les lignes du DataFrame
    for index, row in df.iterrows():
        for idx, value in enumerate(row):
            c.drawString(x_positions[idx], y_position, str(value))
        y_position -= 20  # Espacement entre les lignes

        # Si la position dépasse la hauteur de la page, créer une nouvelle page
        if y_position < 50:
            c.showPage()
            y_position = hauteur - 80  # Réinitialiser la position

    c.save()  # Sauvegarder le PDF

# Exemple d'utilisation
fichier_csv = '/Users/dylanrocaribet/Downloads/Inventaire/inventaire.csv'
fichier_pdf = '/Users/dylanrocaribet/Downloads/Inventaire/inventaire.pdf'

csv_to_pdf(fichier_csv, fichier_pdf)