import serial
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

PORT = 'COM6' # à adapter si besoin

try:
    arduino = serial.Serial(PORT, 9600, timeout=1)
except Exception as e:
    messagebox.showerror("Erreur port série", str(e))
    exit()

def envoyer_valeur(valeur):
    if mode_controle.get() == "python":
        arduino.write(f"V{valeur}\n".encode())

def update_position(val):
    envoyer_valeur(val)
    valeur_label.config(text=f"Servo: {val}")

def tourner_gauche():
    envoyer_valeur(90 - vitesse_scale.get())
    valeur_label.config(text="← Gauche")

def tourner_droite():
    envoyer_valeur(90 + vitesse_scale.get())
    valeur_label.config(text="→ Droite")

def stop():
    envoyer_valeur(90)
    valeur_label.config(text="Stop")

def reset_vitesse():
    vitesse_scale.set(0)

def reset_position():
    manivelle_scale.set(90)

def changer_mode():
    if mode_controle.get() == "joystick":
        arduino.write(b"MODE_JOY\n")
        valeur_label.config(text="Mode joystick actif")
    else:
        arduino.write(b"MODE_PY\n")
        envoyer_valeur(90)
        valeur_label.config(text="Mode Python actif")

# --- Interface graphique
fenetre = tk.Tk()
fenetre.title("Servo Interface + Joystick")
fenetre.geometry("639x785")

# --- Image de fond
image = Image.open("fond.jpg").resize((639, 785))
bg = ImageTk.PhotoImage(image)
fond_label = tk.Label(fenetre, image=bg)
fond_label.place(x=0, y=0, relwidth=1, relheight=1)

# --- Colonne latérale gauche (x = 20)
x_left = 20
y = 20
ligne = 40

valeur_label = tk.Label(fenetre, text="Servo: 90", font=("Arial", 12), bg="white")
valeur_label.place(x=x_left, y=y)
y += ligne

# Boutons directionnels
tk.Button(fenetre, text="← Gauche", width=12, command=tourner_gauche).place(x=x_left, y=y)
y += ligne
tk.Button(fenetre, text="→ Droite", width=12, command=tourner_droite).place(x=x_left, y=y)
y += ligne
tk.Button(fenetre, text="Stop", width=12, fg="red", command=stop).place(x=x_left, y=y)
y += ligne + 10

# Curseur de vitesse
tk.Label(fenetre, text="Vitesse", bg="white").place(x=x_left, y=y)
y += 20
vitesse_scale = tk.Scale(fenetre, from_=0, to=90, orient=tk.HORIZONTAL, length=160, bg="white")
vitesse_scale.set(30)
vitesse_scale.place(x=x_left, y=y)
y += 80

tk.Button(fenetre, text="Reset Vitesse", width=15, command=reset_vitesse).place(x=x_left, y=y)
y += ligne

# Curseur manivelle
tk.Label(fenetre, text="Manivelle (angle)", bg="white").place(x=x_left, y=y)
y += 20
manivelle_scale = tk.Scale(fenetre, from_=0, to=180, orient=tk.HORIZONTAL, length=160, command=update_position, bg="white")
manivelle_scale.set(90)
manivelle_scale.place(x=x_left, y=y)
y += 80

tk.Button(fenetre, text="Reset Position", width=15, command=reset_position).place(x=x_left, y=y)
y += ligne + 10

# Sélecteur de mode
tk.Label(fenetre, text="Mode de contrôle", bg="white").place(x=x_left, y=y)
y += 20
mode_controle = tk.StringVar(value="python")
tk.Radiobutton(fenetre, text="Python", variable=mode_controle, value="python", command=changer_mode, bg="white").place(x=x_left, y=y)
y += ligne
tk.Radiobutton(fenetre, text="Joystick", variable=mode_controle, value="joystick", command=changer_mode, bg="white").place(x=x_left, y=y)

# Fermeture propre
def quitter():
    arduino.write(b"MODE_PY\n")
    envoyer_valeur(90)
    arduino.close()
    fenetre.destroy()

fenetre.protocol("WM_DELETE_WINDOW", quitter)
fenetre.mainloop()
