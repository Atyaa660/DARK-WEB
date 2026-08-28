#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from pathlib import Path

VERSION = "0.4"
SAVE_FILE = Path.home() / ".darkweb_save.json"

TEXT = {
    "ar": {
        "title": "دارك ويب",
        "new": "لعبة جديدة",
        "load": "تحميل اللعبة",
        "settings": "الإعدادات",
        "help": "المساعدة",
        "exit": "خروج",
        "choice": "اختيارك: ",
        "name": "اسم اللاعب: ",
        "world": "العالم",
        "player": "لوحة اللاعب",
        "missions": "المهام",
        "market": "السوق",
        "city": "المدينة",
        "save": "حفظ اللعبة",
        "back": "العودة",
        "money": "المال",
        "level": "المستوى",
        "rep": "السمعة",
        "location": "الموقع",
        "inventory": "المخزون",
        "none": "لا يوجد شيء هنا.",
        "press": "اضغط Enter للمتابعة...",
        "bad": "اختيار غير صحيح.",
        "saved": "تم حفظ اللعبة.",
        "loaded": "تم تحميل اللعبة.",
        "no_save": "لا توجد لعبة محفوظة.",
        "dock": "الميناء",
        "market_place": "السوق",
        "cafe": "المقهى",
        "warehouse": "المخزن القديم",
        "characters": "الشخصيات",
        "merchant": "التاجر",
        "worker": "العامل",
        "mysterious": "الرجل الغامض",
        "talk": "تحدث",
        "explore": "استكشف",
        "leave": "مغادرة",
        "buy": "شراء",
        "sell": "بيع",
        "items": "البضائع",
        "coffee": "قهوة",
        "map": "خريطة",
        "tool": "أداة",
        "price": "السعر",
        "bought": "تم الشراء.",
        "sold": "تم البيع.",
        "no_money": "المال غير كافٍ.",
        "no_item": "لا تملك هذا العنصر.",
        "task1": "استكشاف الميناء",
        "task2": "زيارة السوق",
        "task3": "التحدث مع الرجل الغامض",
        "completed": "تم إنجاز المهمة!",
        "already": "المهمة مكتملة بالفعل.",
        "reward": "المكافأة",
        "language": "اللغة",
        "arabic": "العربية",
        "english": "English",
        "help_text": "لعبة خيالية عن الاستكشاف والمهام والقرارات والسمعة والمال."
    },
    "en": {
        "title": "DARK WEB",
        "new": "New Game",
        "load": "Load Game",
        "settings": "Settings",
        "help": "Help",
        "exit": "Exit",
        "choice": "Choice: ",
        "name": "Player name: ",
        "world": "WORLD",
        "player": "Player",
        "missions": "Missions",
        "market": "Market",
        "city": "City",
        "save": "Save Game",
        "back": "Back",
        "money": "Money",
        "level": "Level",
        "rep": "Reputation",
        "location": "Location",
        "inventory": "Inventory",
        "none": "Nothing here.",
        "press": "Press Enter to continue...",
        "bad": "Invalid choice.",
        "saved": "Game saved.",
        "loaded": "Game loaded.",
        "no_save": "No saved game.",
        "dock": "Harbor",
        "market_place": "Market",
        "cafe": "Cafe",
        "warehouse": "Old Warehouse",
        "characters": "Characters",
        "merchant": "Merchant",
        "worker": "Worker",
        "mysterious": "Mysterious Man",
        "talk": "Talk",
        "explore": "Explore",
        "leave": "Leave",
        "buy": "Buy",
        "sell": "Sell",
        "items": "Items",
        "coffee": "Coffee",
        "map": "Map",
        "tool": "Tool",
        "price": "Price",
        "bought": "Purchased.",
        "sold": "Sold.",
        "no_money": "Not enough money.",
        "no_item": "You don't have this item.",
        "task1": "Explore the Harbor",
        "task2": "Visit the Market",
        "task3": "Talk to the Mysterious Man",
        "completed": "Mission completed!",
        "already": "Mission already completed.",
        "reward": "Reward",
        "language": "Language",
        "arabic": "العربية",
        "english": "English",
        "help_text": "A fictional game about exploration, missions, choices, reputation and money."
    }
}

LANG = "ar"


def T(key):
    return TEXT[LANG].get(key, key)


def clear():
    os.system("clear")


def pause():
    input("\n" + T("press"))


def header():
    print("=" * 62)
    print("                         DARK WEB")
    print(f"                         {T('title')}")
    print(f"                         Version {VERSION}")
    print("=" * 62)


def new_player(name):
    return {
        "name": name,
        "level": 1,
        "money": 100,
        "reputation": 0,
        "location": T("dock"),
        "inventory": {},
        "missions": {
            "harbor": False,
            "market": False,
            "mystery": False
        }
    }


def save_game(player):
    data = {"language": LANG, "player": player}
    SAVE_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def load_game():
    if not SAVE_FILE.exists():
        return None

    try:
        data = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
        global LANG
        LANG = data.get("language", "ar")
        return data.get("player")
    except Exception:
        return None


def show_player(player):
    print("\n--- " + T("player") + " ---")
    print(f"{T('name').rstrip(': ')}: {player['name']}")
    print(f"{T('level')}: {player['level']}")
    print(f"{T('money')}: {player['money']}")
    print(f"{T('rep')}: {player['reputation']}")
    print(f"{T('location')}: {player['location']}")

    print("\n--- " + T("inventory") + " ---")

    if not player["inventory"]:
        print(T("none"))
    else:
        for item, amount in player["inventory"].items():
            print(f"- {item}: {amount}")


def missions(player):
    while True:
        clear()
        header()

        print("\n--- " + T("missions") + " ---\n")

        print(
            "1 - " + T("task1") +
            (" ✓" if player["missions"]["harbor"] else "")
        )
        print(
            "2 - " + T("task2") +
            (" ✓" if player["missions"]["market"] else "")
        )
        print(
            "3 - " + T("task3") +
            (" ✓" if player["missions"]["mystery"] else "")
        )
        print("4 - " + T("back"))

        choice = input("\n" + T("choice")).strip()

        if choice == "1":
            if player["missions"]["harbor"]:
                print("\n" + T("already"))
            else:
                player["missions"]["harbor"] = True
                player["reputation"] += 5
                player["money"] += 50
                print("\n✓ " + T("completed"))
                print("+50 " + T("money"))
                print("+5 " + T("rep"))
                save_game(player)
            pause()

        elif choice == "2":
            if player["missions"]["market"]:
                print("\n" + T("already"))
            else:
                print("\n" + T("task2"))
                print(T("market_place"))
                player["missions"]["market"] = True
                player["reputation"] += 3
                player["money"] += 25
                print("\n✓ " + T("completed"))
                print("+25 " + T("money"))
                print("+3 " + T("rep"))
                save_game(player)
            pause()

        elif choice == "3":
            if player["missions"]["mystery"]:
                print("\n" + T("already"))
            else:
                print("\n" + T("task3"))
                player["missions"]["mystery"] = True
                player["reputation"] += 10
                player["money"] += 75
                print("\n✓ " + T("completed"))
                print("+75 " + T("money"))
                print("+10 " + T("rep"))
                save_game(player)
            pause()

        elif choice == "4":
            return

        else:
            print(T("bad"))
            pause()


def market(player):
    items = [
        ("1", T("coffee"), 10),
        ("2", T("map"), 30),
        ("3", T("tool"), 50)
    ]

    while True:
        clear()
        header()

        print("\n--- " + T("market") + " ---")
        print(f"\n{T('money')}: {player['money']}\n")

        for key, name, price in items:
            print(f"{key} - {name} | {T('price')}: {price}")

        print("4 - " + T("back"))

        choice = input("\n" + T("choice")).strip()

        if choice == "4":
            return

        selected = None

        for key, name, price in items:
            if choice == key:
                selected = (name, price)
                break

        if selected is None:
            print(T("bad"))
            pause()
            continue

        name, price = selected

        if player["money"] < price:
            print(T("no_money"))
        else:
            player["money"] -= price
            player["inventory"][name] = player["inventory"].get(name, 0) + 1
            print(f"\n✓ {T('bought')} {name}")
            save_game(player)

        pause()


def character_menu(player, character):
    clear()
    header()

    print("\n--- " + character + " ---\n")

    if character == T("merchant"):
        print(T("market_place"))
        print("\n1 - " + T("talk"))
        print("2 - " + T("back"))

    elif character == T("worker"):
        print(T("dock"))
        print("\n1 - " + T("talk"))
        print("2 - " + T("back"))

    else:
        print("...")
        print("\n1 - " + T("talk"))
        print("2 - " + T("back"))

    choice = input("\n" + T("choice")).strip()

    if choice == "1":
        print()

        if character == T("merchant"):
            print(
                "التاجر: " +
                ("أهلاً بك في السوق." if LANG == "ar"
                 else "Welcome to the market.")
            )

        elif character == T("worker"):
            print(
                "العامل: " +
                ("الميناء مليء بالأسرار." if LANG == "ar"
                 else "The harbor is full of secrets.")
            )

        else:
            print(
                "الرجل الغامض: " +
                ("ربما سنلتقي مرة أخرى." if LANG == "ar"
                 else "Perhaps we will meet again.")
            )

        pause()


def city(player):
    places = {
        "1": T("dock"),
        "2": T("market_place"),
        "3": T("cafe"),
        "4": T("warehouse")
    }

    while True:
        clear()
        header()

        print("\n--- " + T("city") + " ---\n")

        for key, place in places.items():
            print(f"{key} - {place}")

        print("5 - " + T("back"))

        choice = input("\n" + T("choice")).strip()

        if choice == "5":
            return

        if choice not in places:
            print(T("bad"))
            pause()
            continue

        place = places[choice]
        player["location"] = place

        clear()
        header()

        print(f"\n--- {place} ---\n")

        if choice == "1":
            print(
                "ميناء المدينة مزدحم بالسفن والعمال."
                if LANG == "ar"
                else "The city harbor is crowded with ships and workers."
            )
            print("\n1 - " + T("explore"))
            print("2 - " + T("characters"))
            print("3 - " + T("back"))

            c = input("\n" + T("choice")).strip()

            if c == "1":
                player["missions"]["harbor"] = True
                player["reputation"] += 5
                player["money"] += 50
                print("\n✓ " + T("completed"))
                print("+50 " + T("money"))
                print("+5 " + T("rep"))
                save_game(player)
                pause()

            elif c == "2":
                character_menu(player, T("worker"))

        elif choice == "2":
            market(player)

        elif choice == "3":
            print(
                "مقهى هادئ يجتمع فيه سكان المدينة."
                if LANG == "ar"
                else "A quiet cafe where city residents gather."
            )
            print("\n1 - " + T("talk"))
            print("2 - " + T("back"))

            c = input("\n" + T("choice")).strip()

            if c == "1":
                character_menu(player, T("mysterious"))

        elif choice == "4":
            print(
                "مخزن قديم في طرف الميناء."
                if LANG == "ar"
                else "An old warehouse at the edge of the harbor."
            )
            pause()


def settings():
    global LANG

    clear()
    header()

    print("\n--- " + T("settings") + " ---\n")
    print("1 - " + T("arabic"))
    print("2 - " + T("english"))
    print("3 - " + T("back"))

    choice = input("\n" + T("choice")).strip()

    if choice == "1":
        LANG = "ar"
    elif choice == "2":
        LANG = "en"

    pause()


def help_menu():
    clear()
    header()
    print("\n--- " + T("help") + " ---\n")
    print(T("help_text"))
    pause()


def world(player):
    while True:
        clear()
        header()

        show_player(player)

        print("\n--- " + T("world") + " ---\n")
        print("1 - " + T("player"))
        print("2 - " + T("missions"))
        print("3 - " + T("market"))
        print("4 - " + T("city"))
        print("5 - " + T("save"))
        print("6 - " + T("back"))

        choice = input("\n" + T("choice")).strip()

        if choice == "1":
            clear()
            header()
            show_player(player)
            pause()

        elif choice == "2":
            missions(player)

        elif choice == "3":
            market(player)

        elif choice == "4":
            city(player)

        elif choice == "5":
            save_game(player)
            print("\n✓ " + T("saved"))
            pause()

        elif choice == "6":
            return

        else:
            print(T("bad"))
            pause()


def main():
    global LANG
    LANG = "ar"

    while True:
        clear()
        header()

        print("\n1 - " + T("new"))
        print("2 - " + T("load"))
        print("3 - " + T("settings"))
        print("4 - " + T("help"))
        print("5 - " + T("exit"))

        choice = input("\n" + T("choice")).strip()

        if choice == "1":
            clear()
            header()

            name = input("\n" + T("name")).strip()

            if not name:
                name = "Player"

            player = new_player(name)
            save_game(player)

            print(f"\n✓ {T('created')}: {name}")
            pause()

            world(player)

        elif choice == "2":
            player = load_game()

            if player is None:
                print("\n[!] " + T("no_save"))
                pause()
            else:
                print("\n✓ " + T("loaded"))
                pause()
                world(player)

        elif choice == "3":
            settings()

        elif choice == "4":
            help_menu()

        elif choice == "5":
            clear()
            print("DARK WEB")
            print(T("exit"))
            break

        else:
            print(T("bad"))
            pause()


if __name__ == "__main__":
    main()
