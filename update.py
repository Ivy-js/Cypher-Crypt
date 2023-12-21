import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def crypter_rot13(decalage):
    texte_a_crypter = input_text.get("1.0", "end-1c")
    texte_crypte = string_rot13(texte_a_crypter, decalage)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", texte_crypte)

def lettre_rot13(lettre, decalage):
    resultat = ""
    if len(lettre) <= 1:
        for char in lettre:
            if 'a' <= char <= 'z':
                shift = decalage
                if char >= "n":
                    shift = -decalage
                new = chr(ord(char) + shift)
                resultat += new
            else:
                resultat += char
    return resultat

def string_rot13(mot, decalage):
    resultat = ""
    for i in range(len(mot)):
        resultat += lettre_rot13(mot[i], decalage)
    return resultat


decalage_entry = tk.Entry(app, width=10)
decalage_entry.pack(pady=10, padx=5)
decalage_entry.insert(0, "13")  

crypter_button = tk.Button(app, text="Crypter/Décrypter", command=lambda: crypter_rot13(int(decalage_entry.get())))
crypter_button.pack()

crypter_fichier_button = tk.Button(app, text="Crypter/Décrypter un fichier", command=crypter_fichier)
crypter_fichier_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()