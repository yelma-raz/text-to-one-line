# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:25:37 2024

@author: Razane
"""

import tkinter as tk
from tkinter import messagebox

# Fonction pour convertir le texte en une seule ligne
def convertir_texte():
    texte = entry.get("1.0", tk.END)  # Récupérer tout le texte
    texte_sur_une_ligne = texte.replace('\n', ' ').strip()  # Remplacer les sauts de ligne par des espaces
    result_entry.delete(0, tk.END)  # Effacer le champ précédent
    result_entry.insert(0, texte_sur_une_ligne)  # Insérer le texte converti

# Fonction pour copier le texte dans le presse-papier
def copier_texte():
    fenetre.clipboard_clear()  # Vider le presse-papier
    fenetre.clipboard_append(result_entry.get())  # Copier le texte converti
   # messagebox.showinfo("Copié", "Le texte a été copié dans le presse-papier")
   
# Fonction pour réinitialiser les zones de texte
def reinitialiser_texte():
    entry.delete("1.0", tk.END)  # Effacer le texte entré
    result_entry.delete(0, tk.END)  # Effacer le texte converti
    
# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertir en une seule ligne")

# Zone de texte pour entrer du texte
label = tk.Label(fenetre, text="Entrez votre texte:")
label.pack(padx=10, pady=10)

entry = tk.Text(fenetre, height=30, width=40)
entry.pack(padx=10, pady=10)

# Bouton pour convertir le texte
convert_button = tk.Button(fenetre, text="Convertir", command=convertir_texte)
convert_button.pack(pady=5)

# Bouton pour réinitialiser le texte
reset_button = tk.Button(fenetre, text="Réinitialiser", command=reinitialiser_texte)
reset_button.pack(pady=10)

# Zone d'affichage du résultat
result_label = tk.Label(fenetre, text="Texte sur une seule ligne :")
result_label.pack(padx=10, pady=5)

result_entry = tk.Entry(fenetre, width=50)
result_entry.pack(padx=10, pady=5)

# Bouton pour copier le texte
copy_button = tk.Button(fenetre, text="Copier", command=copier_texte)
copy_button.pack(pady=10)




# Lancer l'application
fenetre.mainloop()

