# Willkommen zu eurem ersten Python Programm

# Als erstes müsst ir oben rechts einen Kernel auswählen. Dieser Kernel ist für die Ausführung des Codes zuständig.
# Wählt den Kernel aus, der mit "Python 3" gekennzeichnet ist.
# Viel Spass beim Schere, Stein, Papier - Mal sehen wer die Nase vorne hat, du oder der Laptop
# Gib deine Auswahl ein, um den Spielstand zu sehen
# Die Auswahl gibst du oben im Feld ein. Die Ausgabe erfolgt unten im Terminal


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    spieler_auswahl = int(input('Was wählst du? Für Stein 0, Für Schere 1, Für Papier 2: '))
    computer_auswahl = random.randint(0, 2)

    if spieler_auswahl == 0:
        print("Du hast Stein gewählt:")
        print(rock)
    elif spieler_auswahl == 1:
        print("Du hast Schere gewählt:")
        print(scissors)
    elif spieler_auswahl == 2:
        print("Du hast Papier gewählt:")
        print(paper)
    else:
        print("Ungültige Auswahl. Bitte wähle 0, 1 oder 2.")
        continue
    print("Der Computer hat gewählt:")
    if computer_auswahl == 0:
        print(rock)
    elif computer_auswahl == 1:
        print(scissors)
    else:
        print(paper)

    if spieler_auswahl == computer_auswahl:
        print("Es ist ein Unentschieden!")
    elif (spieler_auswahl == 0 and computer_auswahl == 1) or \
        (spieler_auswahl == 1 and computer_auswahl == 2) or \
        (spieler_auswahl == 2 and computer_auswahl == 0):
        print("Herzlichen Glückwunsch! Du hast gewonnen!")
    else:
        print("Entschuldigung, du hast verloren.")
