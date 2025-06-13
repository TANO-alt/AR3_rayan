# Projet : Contrôle hybride d’un servomoteur à rotation continue (Arduino + Interface Python)

## Objectif

Ce projet a pour but de contrôler un **servomoteur à rotation continue** à l’aide :

- d’un **joystick physique** connecté à une carte **Arduino Uno**
- ou d’une **interface graphique Python interactive** (Tkinter)

L’utilisateur peut **basculer dynamiquement** entre les deux modes pour piloter le moteur en temps réel.

---

## Composants matériels

- Arduino Uno  
- Servomoteur à rotation continue (broche signal sur D9)  
- Joystick analogique :
  - VRx → A0 (X)
  - SW (bouton) → D4  
- PC Windows avec Python + interface graphique

---

## Fonctionnalités de l’interface Python

- **Contrôle manuel** du servomoteur :
  - Boutons `Gauche`, `Droite`, `Stop`
  - Curseur de **vitesse**
  - Curseur de **position (angle 0–180°)** type manivelle
- Boutons de **remise à zéro**
- **Sélecteur de mode** :
  - `Joystick` (pilotage physique)
  - `Python` (interface GUI)
- **Image de fond personnalisable** (`fond.jpg`)
- Comportement en temps réel via port série (pyserial)

---

## Fonctionnement côté Arduino

- Lecture du joystick (axe X analogique)
- Lecture du bouton SW pour éventuellement inverser la direction
- Lecture du port série pour recevoir des commandes depuis le PC
- Gestion du mode actif (`joystick` ou `Python`)

---

## Structure du projet

```
/projet-servo-hybride
├── interface_servo.py ← Interface graphique Python
├── arduino_servo.ino ← Code Arduino
├── fond.jpg ← Image de fond pour l’interface
├── README.md ← Ce fichier
```

---

## Lancer le projet

### 1. Matériel

- Connecter le joystick (VRx sur A0, SW sur D4)
- Brancher le servomoteur (signal sur D9)
- Brancher l’Arduino au PC via USB

### 2. Arduino

- Ouvrir `arduino_servo.ino` dans l’IDE Arduino
- Compiler et téléverser sur la carte

### 3. Python

Installer les bibliothèques nécessaires :

```bash
pip install pyserial pillow
```

Lancer l’interface :

```bash
python interface_servo.py
```

---

## Idées d'amélioration

- Ajout d’un **mode automatique** (rotation aléatoire)
- Affichage en temps réel de l’angle calculé
- Intégration de sons ou d’effets visuels
- Enregistrement de sessions de contrôle

---

## Aperçu

> *(Ajoutez ici une capture d’écran de l’interface une fois ouverte)*

---

## Licence

Projet open-source libre d’utilisation à des fins pédagogiques ou personnelles.
