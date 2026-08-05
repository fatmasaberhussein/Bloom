import random

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

player_name = input("👤 Enter your name: ")
plant_name = input("🌱 Name your plant: ")

print()
print(f"❤️ Welcome {player_name}")
print(f"🌿 You are now taking care of {plant_name}")

# =====================================
#      Plant Statistics
# =====================================

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
#        Main Game Loop
# =====================================

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
    # Invalid Choice
    # =====================================

    else:

        print("❌ Invalid Choice!")