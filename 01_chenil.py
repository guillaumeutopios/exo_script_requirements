class Chien:
    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race


def input_chien():
    nom = input("Nom : ")
    age = int(input("Age : "))
    race = input("Race : ")
    chien = Chien(nom, age, race)
    return chien


def afficher_chien(chien: Chien):
    print(
        f"Le chien {chien.nom}, âgé de {chien.age} ans, est de race {chien.race}")


def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les chiens")
        print("2. Ajouter un chien")
        print("3. Retirer un chien")
        print("4. Ajouter un an aux chiens")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")


def handle_choice(choice: str, list_chiens: list):
    match choice:
        case "1":
            print('=== Liste des Chiens ===')
            for chien in list_chiens:
                print(list_chiens.index(chien)+1, end=': ')
                afficher_chien(chien)
        case "2":
            list_chiens.append(input_chien())
        case "3":
            list_chiens.pop(int(input("Numero du chien à retirer : "))-1)
        case "4":
            for chien in list_chiens:
                chien.age += 1  # pareil que "chien.age = chien.age + 1"
    return list_chiens


def main():
    # ça reste possible de mettre d'abord le chien dans une variable
    pepette = Chien("Pepette", 2, "Golden Retriever")
    list_chiens = [
        pepette,
        Chien("Eden", 10, "Bauçeron"),
        Chien("Rex", 6, "Chiwawa")
    ]
    while True:
        choice = main_menu()
        if choice == "0":
            break
        list_chiens = handle_choice(choice, list_chiens)


if __name__ == "__main__":
    main()
