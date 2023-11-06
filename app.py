import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def crypter_rot13():
    texte_a_crypter = input_text.get("1.0", "end-1c")
    texte_crypte = string_rot13(texte_a_crypter)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", texte_crypte)

def crypter_fichier():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        texte_crypte = string_rot13(content)
        with open(file_path, 'w') as file:
            file.write(texte_crypte)
        status_label.config(text=f'Fichier "{os.path.basename(file_path)}" crypté/décrypté avec succès.')
        subprocess.Popen(["open", file_path])

def lettre_rot13(lettre):
    resultat = ""
    if len(lettre) <= 1:
        for char in lettre:
            if 'a' <= char <= 'z':
                decalage = 13
                if char >= "n":
                    decalage = -13
                new = chr(ord(char) + decalage)
                resultat += new
            else:
                resultat += char
    return resultat

def string_rot13(mot):
    resultat = ""
    for i in range(len(mot)):
        resultat += lettre_rot13(mot[i])
    return resultat

app = tk.Tk()
app.title("CypherCrypt / Crypter NSI")
app.iconbitmap("avion.ico")

input_text = tk.Text(app, height=10, width=40)
input_text.pack(pady=10)
output_text = tk.Text(app, height=10, width=40)
output_text.pack(pady=10)

crypter_button = tk.Button(app, text="Crypter/Décrypter", command=crypter_rot13)
crypter_button.pack()
crypter_fichier_button = tk.Button(app, text="Crypter/Décrypter un fichier", command=crypter_fichier)
crypter_fichier_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
