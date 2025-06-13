# Projet : Contrôle hybride d’un servomoteur à rotation continue (Arduino + Interface Python)

## Objectif

Ce projet permet de contrôler un **servomoteur à rotation continue** via deux modes d'interaction complémentaires :

- Un **joystick physique** connecté à une carte **Arduino Uno**
- Une **interface graphique Python** réalisée avec Tkinter

L’utilisateur peut passer dynamiquement d’un mode à l’autre et observer les effets en temps réel.

---

## Composants matériels

- Arduino Uno  
- Servomoteur à rotation continue (signal sur D9)  
- Joystick analogique :
  - VRx connecté à A0 (axe X)
  - SW connecté à D4 (bouton)
- Câblage de base (breadboard, fils Dupont)
- Ordinateur sous Windows avec Python installé

---

## Fonctionnalités de l’interface Python

- Contrôle du servomoteur :
  - Boutons `Gauche`, `Droite`, `Stop`
  - Curseur de **vitesse**
  - Curseur de **position** (angle 0 à 180°, style manivelle)
- Boutons de **remise à zéro** (vitesse et position)
- Sélecteur de **mode de contrôle** (`Python` ou `Joystick`)
- Image de fond personnalisable (`fond.jpg`)
- Animation visuelle lors du mode aléatoire (optionnel)
- Communication série en temps réel avec l’Arduino

---

## Fonctionnement côté Arduino

- Lit l’axe X du joystick via une entrée analogique (A0)
- Lit l’état du bouton (SW) pour inverser la direction
- Reçoit des instructions depuis le PC via le port série
- Gère dynamiquement le mode actif (`Joystick` ou `Python`)
- Envoie ou applique la vitesse de rotation du servomoteur

---

## Structure du projet

```
/projet-servo-hybride
├── arduino_servo/
│   └── arduino_servo.ino     ← Code Arduino
├── interface_servo.py        ← Interface graphique Python
├── fond.jpg                  ← Image de fond de l’interface
├── README.md                 ← Présentation du projet
```

---

## Mise en route

### 1. Côté Arduino

- Ouvrir `arduino_servo.ino` dans l’IDE Arduino
- Sélectionner la carte et le port
- Compiler et téléverser le code

### 2. Côté Python

- Installer les dépendances nécessaires :

```bash
pip install pyserial pillow
```

- Lancer l’interface :

```bash
python interface_servo.py
```

---

## Améliorations possibles

- Ajout d’un **mode aléatoire** (vitesse et direction aléatoires)
- Intégration d’un **affichage de retour visuel** (gauge, LED, etc.)
- Sauvegarde des sessions ou des configurations
- Contrôle via un gamepad ou d’autres entrées physiques

---

## Aperçu

> *(Ajouter ici une capture d’écran de l’interface)*

---

## Licence

Ce projet est open-source et libre d’utilisation pour des projets éducatifs ou personnels.