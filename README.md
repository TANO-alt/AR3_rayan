![Made with Arduino](https://img.shields.io/badge/Made%20with-Arduino-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
# Projet : Contrôle hybride d’un servomoteur à rotation continue (Arduino + Interface Python)

## Objectif

Ce projet permet de contrôler un **servomoteur à rotation continue** via deux modes d'interaction :

- Un **joystick physique** connecté à une carte **Arduino Uno**
- Une **interface graphique Python**

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
- Communication série en temps réel avec l’Arduino

---

## Fonctionnement côté Arduino

- Lecture de l’axe X du joystick via une entrée analogique (A0)
- Lecture l’état du bouton (SW) pour inverser la direction
- Réception des instructions depuis le PC via le port série
- Gestion dynamique du mode actif (`Joystick` ou `Python`)
- Définit et envoie la vitesse de rotation du servomoteur

Voici le schéma de branchement du projet :

  <img src="assets/Schéma_de_cablage.png" width="500">

- Le port de communication **COM6** dans le fichier **python/interface_servo.py** à la ligne **6**, est à **modifier** selon celui utilisé.

---

## Structure du projet

```
/projet-servo-hybride
├── arduino_servo/
│   └── arduino_servo.ino          ← Code Arduino
├── assets
│   └── Photo_du_montage_1.jpg     ← Photo du montage
│   └── Photo_du_montage_2.jpg     ← Photo du montage
│   └── Photo_du_montage_3.jpg     ← Photo du montage
│   └── Photo_du_montage_4.jpg     ← Photo du montage
│   └── Schéma_de_branchement.png  ← Schéma de branchement du projet
├── python
│   └── interface_servo.py         ← Interface graphique Python
│   └── fond.jpg                   ← Image de fond de l’interface
│   └── requirements.txt           ← Installation de pyserial et Pillow
├── README.md                      ← Présentation du projet
```

---

## Aperçu
Voici quelques photos du montage : 

<table>
  <tr>
    <td>
      <img src="assets/Photo_du_montage_1.jpg" width="480"><br>
      <img src="assets/Photo_du_montage_2.jpg" width="480">
    </td>
    <td>
      <img src="assets/Photo_du_montage_3.jpg" width="545">
    </td>
  </tr>
</table>
