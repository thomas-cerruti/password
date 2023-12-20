import re
import hashlib
import json
import random
import string

def verifmdpexigence(mdp):
    return (
        len(mdp) >= 8 and
        any(char.isupper() for char in mdp) and
        any(char.islower() for char in mdp) and
        any(char.isdigit() for char in mdp) and
        any(char in "!@#$%^&*.-_/\|():;" for char in mdp)
    )

def mdputilisateur():
    affexigencemdp()  
    while True:
        mdp = input("Choisissez un mot de passe : ")
        if verifmdpexigence(mdp):
            return mdp
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

def hashmdp(mdp):
    hashed_password = hashlib.sha256(mdp.encode()).hexdigest()
    return hashed_password

def mdpsauvegarde(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def chargemdp():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def affexigencemdp():
    print("Exigences de sécurité du mot de passe :")
    print("1. Il doit contenir au moins huit caractères.")
    print("2. Il doit contenir au moins une lettre majuscule.")
    print("3. Il doit contenir au moins une lettre minuscule.")
    print("4. Il doit contenir au moins un chiffre.")
    print("5. Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *, ., -, _, /, \, |, (, ), :, ;, ).")

def main():
    passwords = chargemdp()

    while True:
        print("\nMenu :")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe enregistrés")
        print("0. Quitter")

        menuchoix = input("Veuillez entrer votre choix : ")

        if menuchoix == '1':
            user_password = mdputilisateur()
            hashed_password = hashmdp(user_password)

            if hashed_password not in passwords:
                passwords.append(hashed_password)
                mdpsauvegarde(passwords)
                print("Mot de passe enregistré avec succès !")
            else:
                print("Ce mot de passe existe déjà dans la base de données. Veuillez en choisir un nouveau.")
        elif menuchoix == '2':
            print("Mots de passe enregistrés :")
            for hashed_pass in passwords:
                print(hashed_pass)
        elif menuchoix == '0':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()