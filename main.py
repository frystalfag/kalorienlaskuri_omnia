import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def mainmenu():
    while True:
        print("1. Lisää ruokaa")
        print("2. Katso ruokien lista")
        print("3. Etsi ruokaa")
        print("4. Muokkaa ruokaa")
        print("5. Poista ruoka")
        print("6. Katso kalorit yhteensä")
        print("0. Lopeta")

        try:
            a = int(input("Valitse toiminto: "))
        except ValueError:
            print("Anna numero!")
            continue

        if a == 1:
            add_food()

        elif a == 2:
            show_food()

        elif a == 3:
            search_food()

        elif a == 4:
            rename()

        elif a == 5:
            delete_food()

        elif a == 6:
            total_calories()

        elif a == 0:
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta!")

def add_food():
    data = load_data()

    print("\n Lisää ruoka")

    name = input("Mitä ruokaa olet syönyt? ")

    if name == "":
        print("Ruoan nimi ei voi olla tyhjä.")
        return

    try:
        calories = float(
            input("Kuinka paljon kaloreita ruoka sisälsi? ")
        )
    except ValueError:
        print("Anna kalorit numerona!")
        return

    if calories < 0:
        print("Kalorit eivät voi olla negatiivisia.")
        return

    food = {
        "name": name,
        "calories": calories
    }

    data.append(food)
    save_data(data)

    print("Lisätty tietokantaan!")

def show_food():
    data = load_data()

    print("\n RUOAT")

    if len(data) == 0:
        print("Ruokia ei ole vielä lisätty.")
        return

    for i, food in enumerate(data, start=1):
        print(
            f"{i}. {food['name']} - "
            f"{food['calories']} kcal"
        )

def search_food():
    data = load_data()

    print("\n Etsi ruokaa")

    search = input("Mitä ruokaa etsit? ").lower()

    found = False

    for food in data:
        if search in food["name"].lower():
            print(
                f"{food['name']} - "
                f"{food['calories']} kcal"
            )
            found = True

    if not found:
        print("Ruokaa ei löytynyt.")

def rename():
    data = load_data()

    print("\n Muokkaa ruokaa")

    if len(data) == 0:
        print("Ruokia ei ole vielä lisätty.")
        return

    show_food()

    try:
        number = int(input("Valitse ruoan numero: "))
    except ValueError:
        print("Anna numero!")
        return

    if number < 1 or number > len(data):
        print("Virheellinen numero.")
        return

    food = data[number - 1]

    print(f"Nykyinen nimi: {food['name']}")
    print(f"Nykyiset kalorit: {food['calories']} kcal")

    new_name = input(
        "Anna uusi nimi (Enter = pidä nykyinen): "
    )

    if new_name != "":
        food["name"] = new_name

    new_calories = input(
        "Anna uudet kalorit (Enter = pidä nykyiset): "
    )

    if new_calories != "":
        try:
            new_calories = float(new_calories)

            if new_calories < 0:
                print("Kalorit eivät voi olla negatiivisia.")
                return

            food["calories"] = new_calories

        except ValueError:
            print("Anna kalorit numerona.")
            return

    save_data(data)

    print("Ruoka päivitetty!")

def delete_food():
    data = load_data()

    print("\n Poista ruokaa")

    if len(data) == 0:
        print("Ruokia ei ole vielä lisätty.")
        return

    show_food()

    try:
        number = int(input("Valitse poistettavan ruoan numero: "))
    except ValueError:
        print("Anna numero!")
        return

    if number < 1 or number > len(data):
        print("Virheellinen numero.")
        return

    food = data[number - 1]

    print("\nPoistettava ruoka:")
    print(f"{food['name']} - {food['calories']} kcal")

    confirm = input("Haluatko varmasti poistaa? (k/e): ").lower()

    if confirm == "k":
        data.pop(number - 1)
        save_data(data)
        print("Ruoka poistettu!")
    else:
        print("Poistaminen peruutettu.")

def total_calories():
    data = load_data()

    if len(data) == 0:
        print("Ruokia ei ole vielä lisätty.")
        return

    total = 0

    for food in data:
        total += food["calories"]

    print("\n Kalorit yhteensä")
    print(f"Kalorit yhteensä: {total} kcal")

mainmenu()

