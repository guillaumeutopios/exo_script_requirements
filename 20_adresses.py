def input_address():
    address = {}
    address["N° Voie"] = input("N° voie : ")
    address["Complément"] = input("Complément : ")
    address["Intitulé"] = input("Intitulé : ")
    address["Commune"] = input("Commune : ")
    address["Code Postal"] = input("Code Postal : ")
    return address
    
def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Editer une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")

def handle_choice(choice: int, list_addresses: list): 
    match choice:
        case "1":
            print('=== Liste des Adresses ===')
            for dict_address in list_addresses:
                print(list_addresses.index(dict_address)+1, end=': ')
                for key, value in dict_address.items():
                    print(f"{key}: {value}", end=', ')
                print()
        case "2":
            list_addresses.append(input_address())
        case "3":
            nb = int(input("Numero de l'adresse à modifier : "))-1
            list_addresses.pop(nb)
            list_addresses.insert(nb, input_address())
        case "4":
            list_addresses.pop(int(input("Numero de l'adresse à supprimer : "))-1)
        case "0":
            # si on s'arrête, on ne renvoie pas la liste car c'est inutile
            return False, None
    # retourne la variable pour savoir si on continue 
    # ainsi que notre liste d'adresses'
    return True, list_addresses

def main():
    list_dict_addresses = [
        { # une adresse par défaut
            "N° Voie": "9Bis",
            "Complément": "Appartement 8",
            "Intitulé": "rue Mairesse",
            "Commune": "AMIENS",
            "Code Postal": "80000"
        }
    ]
    suivant = True
    while suivant:
        choice = main_menu()
        suivant, list_dict_addresses = handle_choice(choice, list_dict_addresses)


if __name__ == "__main__":
    main()


# dict_adresses = dict()
# user_input = ""
# i_adresse = 0

# def ajouter_adresse():
#     print("\n=== AJOUTER UNE ADRESSE ===")
#     global i_adresse

#     i_adresse += 1
#     dict_adresses[i_adresse] = dict()

#     dict_adresses[i_adresse]["Numero de Voie"] = int(input("Veuilliez entrer le numéro de voie SVP : "))
#     dict_adresses[i_adresse]["Complément d'adresse"] = input("Veuilliez entrer le complément d'adresse SVP : ")
#     dict_adresses[i_adresse]["Intitulé de voie"] = input("Veuilliez entrer l'intitulé de voie SVP : ")
#     dict_adresses[i_adresse]["Code Postal"] = int(input("Veuilliez entrer le code postal SVP : "))
#     dict_adresses[i_adresse]["Commune"] = input("Veuilliez entrer le nom de la commune SVP : ")


# def voir_adresses():
#     print("\n=== LISTE ADRESSES ===")
#     for k,v in dict_adresses.items():
#         if (v is not None):
#             print(f"Adresse n°{k} :")
#             for keys,vals in v.items():
#                 if (str(vals) != ""):
#                     print(f"\t{keys} : {vals}")

# def modifier_adresse():
#     print("\n=== EDITER UNE ADRESSE ===")
#     numero_edit = int(input("Quelle ID voulez-vous éditer ?"))
#     if dict_adresses[numero_edit] is not None:
#         dict_adresses[numero_edit]["Numero de Voie"] = int(input("Veuilliez entrer le numéro de voie SVP : "))
#         dict_adresses[numero_edit]["Complément d'adresse"] = input("Veuilliez entrer le complément d'adresse SVP : ")
#         dict_adresses[numero_edit]["Intitulé de voie"] = input("Veuilliez entrer l'intitulé de voie SVP : ")
#         dict_adresses[numero_edit]["Code Postal"] = int(input("Veuilliez entrer le code postal SVP : "))
#         dict_adresses[numero_edit]["Commune"] = input("Veuilliez entrer le nom de la commune SVP : ")
#     else :
#         print("Il n'y a pas de clé portant cette valeur !")

# def supprimer_adresse():
#     print("\n=== SUPPRIMER UNE ADRESSE ===")
#     numero_edit = int(input("Quelle ID voulez-vous supprimer ?"))
#     if dict_adresses[numero_edit] is not None:
#         dict_adresses[numero_edit] = None
#     else :
#         print("Il n'y a pas de clé portant cette valeur !")

# def menu_principal():
#     while True:
#         print("=== MENU PRINCIPAL ===")
#         print("1. Voir les adresses")
#         print("2. Ajouter une adresse")
#         print("3. Editer une adresse")
#         print("4. Supprimer une adresse")
#         print("0. Quitter le programme")

#         user_choice = int(input("Votre choix : "))
#         if user_choice == 0:
#             break
#         elif user_choice == 1:
#             voir_adresses()
#         elif user_choice == 2:
#             ajouter_adresse()
#         elif user_choice == 3:
#             modifier_adresse()
#         elif user_choice == 4:
#             supprimer_adresse()
#         else:
#             print("Ce choix n'est pas disponible !")

#         print("")

# menu_principal()
