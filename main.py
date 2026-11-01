import random
import json
import os

# =====================================
#       Plant Management
# =====================================

plants = []
active_plant = None

# =====================================
#          BLOOM GAME
# =====================================

print("=" * 40)
print("🌸 BLOOM")
print("Grow with Love")
print("=" * 40)

# =====================================
#      Player Information
# =====================================

def new_game():
    global player_name, plant_name
    global water, sunlight, health, happiness
    global energy, experience, growth_stage, day, coins

    player_name = input("👤 Enter your name: ")
    plant_name = input("🌱 Name your plant: ")

    print()
    print(f"❤️ Welcome {player_name}")
    print(f"🌿 You are now taking care of {plant_name}")

    water = 50
    sunlight = 50
    health = 40
    happiness = 30
    energy = 20
    experience = 0

    growth_stage = "🌱 Seed"
    day = 1
    coins = 0

# =====================================
#        Save Game
# =====================================

def save_game():

    if active_plant is not None:
        active_plant.update(create_plant_data())

    game_data = {
        "player_name": player_name,
        "coins": coins,
        "plants": plants
    }

    with open("bloom_save.json", "w", encoding="utf-8") as save_file:
        json.dump(game_data, save_file, indent=4)

# =====================================
#        Load Game
# =====================================

def load_game():
    global player_name, coins
    global plants, active_plant

    try:
        with open("bloom_save.json", "r", encoding="utf-8") as save_file:
            game_data = json.load(save_file)

        if not isinstance(game_data, dict):
            print("❌ Invalid save file format!")
            return False

        player_name = game_data["player_name"]
        coins = game_data["coins"]

        # Validate Player Data
        if not isinstance(player_name, str):
            print("❌ Invalid player name!")
            return False

        if not isinstance(coins, int):
            print("❌ Invalid coins data!")
            return False

        # New Save Format
        if "plants" in game_data:
            plants = game_data["plants"]

            if not isinstance(plants, list):
                print("❌ Invalid plants data!")
                return False

            for plant in plants:
                if not isinstance(plant, dict):
                    print("❌ Invalid plant data!")
                    return False

            required_keys = [
                "plant_name",
                "water",
                "sunlight",
                "health",
                "happiness",
                "energy",
                "experience",
                "growth_stage",
                "day"
            ]

            for plant in plants:
                for key in required_keys:
                    if key not in plant:
                        print(f"❌ Missing plant data: {key}")
                        return False

            expected_types = {
                "plant_name": str,
                "water": int,
                "sunlight": int,
                "health": int,
                "happiness": int,
                "energy": int,
                "experience": int,
                "growth_stage": str,
                "day": int
            }

            for plant in plants:
                for key, expected_type in expected_types.items():
                    if not isinstance(plant[key], expected_type):
                        print(f"❌ Invalid data type for: {key}")
                        return False

        # Old Save Format
        else:
            plant_data = {
                "plant_name": game_data["plant_name"],
                "water": game_data["water"],
                "sunlight": game_data["sunlight"],
                "health": game_data["health"],
                "happiness": game_data["happiness"],
                "energy": game_data["energy"],
                "experience": game_data["experience"],
                "growth_stage": game_data["growth_stage"],
                "day": game_data["day"]
            }

            plants = [plant_data]

        if plants:
            load_plant(plants[0])
        else:
            active_plant = None

    except FileNotFoundError:
        print("❌ Save file not found!")
        return False

    except json.JSONDecodeError:
        print("❌ Save file is corrupted!")
        return False

    except KeyError:
        print("❌ Save file is missing required data!")
        return False

    except TypeError:
        print("❌ Save file contains invalid data!")
        return False

    return True

# =====================================
#       Plant Data
# =====================================

def create_plant_data():
    plant_data = {
        "plant_name": plant_name,
        "water": water,
        "sunlight": sunlight,
        "health": health,
        "happiness": happiness,
        "energy": energy,
        "experience": experience,
        "growth_stage": growth_stage,
        "day": day
    }

    return plant_data

# =====================================
#        Load Plant Data
# =====================================

def load_plant(plant_data):
    global active_plant
    global plant_name, water, sunlight
    global health, happiness, energy, experience
    global growth_stage, day

    plant_name = plant_data["plant_name"]
    water = plant_data["water"]
    sunlight = plant_data["sunlight"]
    health = plant_data["health"]
    happiness = plant_data["happiness"]
    energy = plant_data["energy"]
    experience = plant_data["experience"]
    growth_stage = plant_data["growth_stage"]
    day = plant_data["day"]

    active_plant = plant_data

# =====================================
#          Add Plant
# =====================================

def add_plant():
    global active_plant

    plant_data = create_plant_data()

    plants.append(plant_data)

    active_plant = plant_data

# =====================================
#         Create New plant
# =====================================

def create_new_plant():
    global plant_name, water, sunlight
    global health, happiness, energy, experience
    global growth_stage, day
    if active_plant is not None:
        active_plant.update(create_plant_data())

    plant_name = input("🌱 Name your new plant: ")

    water = 50
    sunlight = 50
    health = 40
    happiness = 30
    energy = 20
    experience = 0

    growth_stage = "🌱 Seed"
    day = 1

    add_plant()

    print(f"🌿 New plant {plant_name} has been created!")

# =====================================
#          Choose plant
# =====================================

def choose_plant():
    global active_plant

    if not plants:
        print("❌ No plants available!")
        return False

    if active_plant is not None:
        active_plant.update(create_plant_data())

    while True:

        print("\n🌿 Your Plants:")

        for index, plant in enumerate(plants, start=1):
            print(f"{index}. {plant['plant_name']}")

        try:
            choice = int(input("Choose a plant number: "))

            if 1 <= choice <= len(plants):
                load_plant(plants[choice - 1])
                print(f"🌱 Now taking care of {plant_name}!")
                return True

            else:
                print("❌ Invalid choice! Try again.")

        except ValueError:
            print("❌ Please enter a valid number!")

# =====================================
#          Start Menu
# =====================================

def start_menu():

    if os.path.exists("bloom_save.json"):

        if not load_game():
            print("❌ Unable to start the game.")
            return False

        print(f"❤️ Welcome back {player_name}!")

        while True:

            print("\n1️⃣ Continue with an existing plant")
            print("2️⃣ Create a new plant")
            print("3️⃣ Exit")

            start_choice = input("\nChoose: ")

            if start_choice == "1":

                if choose_plant():
                    return True

            elif start_choice == "2":

                create_new_plant()
                return True

            elif start_choice == "3":

                print("👋 Goodbye!")
                return False

            else:

                print("❌ Invalid choice! Please try again.")

    else:

        new_game()
        add_plant()
        return True

# =====================================
#        Main Game Loop
# =====================================

def play_game():
    global water, sunlight, health, happiness
    global energy, experience, growth_stage, day, coins

    while True:

        print("\n" + "=" * 40)
        print(f"📅 Day        : {day}")
        print(f"🌱 Plant      : {plant_name}")
        print(f"🌸 Stage      : {growth_stage}")
        print(f"💰 Coins      : {coins}")
        print("=" * 40)

        print("1️⃣ Water Plant 💧")
        print("2️⃣ Give Sunlight ☀")
        print("3️⃣ Check Status 📊")
        print("4️⃣ Shop 🛒")
        print("5️⃣ End Day 🌙")
        print("6️⃣ Exit 👋")
        print("7️⃣ Save Game 💾")
        print("8️⃣ Load Game 📂")

        choice = input("\nChoose: ")

    # =====================================
    #          Water Plant
    # =====================================

        if choice == "1":

            water += 10
            experience += 2

            if water > 100:
                water = 100

            print("\n💧 You watered your plant!")

    # =====================================
    #        Give Sunlight
    # =====================================

        elif choice == "2":

            sunlight += 10
            experience += 2

            if sunlight > 100:
                sunlight = 100

            print("\n☀ Your plant enjoyed the sunlight!")

    # =====================================
    #         Check Status
    # =====================================

        elif choice == "3":

            print("\n========== STATUS ==========")
            print(f"🌱 Stage       : {growth_stage}")
            print(f"💧 Water       : {water}")
            print(f"☀ Sunlight    : {sunlight}")
            print(f"❤️ Health      : {health}")
            print(f"😊 Happiness   : {happiness}")
            print(f"⚡ Energy      : {energy}")
            print(f"⭐ Experience  : {experience}")
            print(f"💰 Coins       : {coins}")
            print("============================")

    # =====================================
    #               Shop
    # =====================================

        elif choice == "4":

            print("\n========== SHOP ==========")
            print("1️⃣ Water Bottle 💧  (10 Coins)")
            print("2️⃣ Fertilizer 🌿    (20 Coins)")
            print("3️⃣ Toy 🎁           (30 Coins)")
            print("4️⃣ Exit Shop")
            print("==========================")

            shop_choice = input("Choose Item: ")

        # -----------------------------
        # Water Bottle
        # -----------------------------

            if shop_choice == "1":

                if coins >= 10:

                    coins -= 10
                    water += 20
                    experience += 5

                    if water > 100:
                        water = 100

                    print("🌿 You bought Water Bottle!")

                else:
                    print("❌ You don't have enough coins!")

        # -----------------------------
        # Fertilizer
        # -----------------------------

            elif shop_choice == "2":

                if coins >= 20:

                    coins -= 20
                    health += 15
                    experience += 5

                    if health > 100:
                        health = 100

                    print("🌿 You bought Fertilizer!")

                else:
                    print("❌ You don't have enough coins!")

        # -----------------------------
        # Toy
        # -----------------------------

            elif shop_choice == "3":

                if coins >= 30:

                    coins -= 30
                    happiness += 20
                    experience += 5

                    if happiness > 100:
                        happiness = 100

                    print("🌿 You bought Toy!")

                else:
                    print("❌ You don't have enough coins!")

        # -----------------------------
        # Exit Shop
        # -----------------------------

            elif shop_choice == "4":

                print("🚪 Leaving Shop...")

            else:

                print("❌ Invalid Choice!")


    # =====================================
    #              End Day
    # =====================================

        elif choice == "5":

            day += 1

            water -= 5
            sunlight -= 3
            energy -= 2
            happiness -= 1

            experience += 5

            coins += 5
            print("💰 You earned 5 coins today!")

        # -----------------------------
        # Prevent negative values
        # -----------------------------

            if water < 0:
                water = 0

            if sunlight < 0:
                sunlight = 0

            if energy < 0:
                energy = 0

            if happiness < 0:
                happiness = 0

            if health < 0:
                health = 0

        # -----------------------------
        # Random Event
        # -----------------------------

            event = random.randint(1, 5)

            if event == 1:

                print("🌧 It rained!")
                water += 10

                if water > 100:
                    water = 100

            elif event == 2:

                print("🔥 Very Hot Day!")
                water -= 10
                sunlight -= 5

            elif event == 3:

                print("🐛 Bugs attacked!")
                health -= 10

            elif event == 4:

                print("🌈 Beautiful Weather!")
                happiness += 5

                if happiness > 100:
                    happiness = 100

            elif event == 5:

                print("🎁 You found 10 coins!")
                coins += 10

        # -----------------------------
        # Prevent negative values again
        # -----------------------------

            if water < 0:
                water = 0

            if sunlight < 0:
                sunlight = 0

            if energy < 0:
                energy = 0

            if happiness < 0:
                happiness = 0

            if health < 0:
                health = 0

        # -----------------------------
        # Growth System
        # -----------------------------

            if experience >= 90:
                growth_stage = "🌸 Bloom"

            elif experience >= 50:
                growth_stage = "🌳 Adult Plant"

            elif experience >= 20:
                growth_stage = "🌿 Small Plant"

            else:
                growth_stage = "🌱 Seed"

        # -----------------------------
        # Game Over
        # -----------------------------

            if water == 0 or sunlight == 0 or health == 0:

                print("\n💀 GAME OVER!")
                print(f"{plant_name} couldn't survive.")

                break

        # -----------------------------
        # Win
        # -----------------------------

            if growth_stage == "🌸 Bloom":

                print("\n🎉 CONGRATULATIONS!")
                print(f"{plant_name} is now a beautiful flower!")
                print("🏆 YOU WIN!")

                break

            print("\n🌙 A new day has started!")

    # =====================================
    # Exit Game
    # =====================================

        elif choice == "6":

            print("\n👋 Thanks for playing BLOOM!")
            break

    # =====================================
    # Save Game
    # =====================================

        elif choice == "7":

            save_game()
            print("💾 Game saved successfully!")

    # =====================================
    # Load Game
    # =====================================

        elif choice == "8":

            if active_plant is not None:
                active_plant.update(create_plant_data())

            save_game()

            if load_game():
                print("📂 Game loaded successfully!")
                choose_plant()
            else:
                print("❌ Unable to load the game.")

    # =====================================
    # Invalid Choice
    # =====================================

        else:

            print("❌ Invalid Choice!")

    if active_plant is not None:
        active_plant.update(create_plant_data())
    save_game()

# =====================================
#          Start BLOOM
# =====================================

while True:

    if not start_menu():
        break

    play_game()