hero_health = 10
hero_power = 6
goblin_health = 8
goblin_power = 4
has_potion = False
has_magic_sword = False

def shop():
    still_shopping = True
    global has_potion
    global has_magic_sword

    while still_shopping:
        print("You have entered the shop.")
        print("What do you want to buy?.")
        print("1. Health Potion")
        print("2. Magic Sword")
        print("3. leave the shop")
        print("4. Flex your muscles")
        print(">")

        user_input = input()

        if user_input == "1":
            has_potion = True
        elif user_input == "2":
            has_magic_sword = True
        elif user_input == "3":
            still_shopping = False
        elif user_input == "4":
            print("The shopkeeper is disgusted by your arrogance and throws you out.")
            still_shopping = False
        else:
            print("The shopkeeper grumbles at your nonsense")


hero_name = input("What is your name brave adventurer? ")
hero_name = hero_name.capitalize()

shop()

print(f"{hero_name} have encountered a terrifying goblin.")
while hero_health > 0 and goblin_health > 0:
    print(f"{hero_name} have {hero_health} health and {hero_power} power")
    print(f"The goblin has {goblin_health} health and {goblin_power} power")
    print("What action will ou take?")
    print("1. Attack the goblin")
    print("2. Stand there. And get hit.")
    print("3. Run like a coward")
    if has_potion:
        print("4. Use potion")
    print(">")
    user_input = input()

    if user_input == "1":
        print(f"{hero_name} makes a daring attack!")

        if has_magic_sword:
            print(f"The goblin takes {hero_power} damage and another 5 from the magic sword!")
        else:
            print(f"The goblin take {hero_power} damage!")
        if has_magic_sword:
            goblin_health -= hero_power + 5
        else:
            goblin_health -= hero_power
    elif user_input == "2":
        print(f"{hero_name} stands like a fool looking for an early grave.")
    elif user_input == "3":
        print(f"{hero_name} has run away like a fledgling coward. At least you will live.")
        break
    elif user_input == "4" and has_potion:
        print("You use the health potion and gain 20 health!")
        hero_health += 20
        has_potion = False
    else:
        print(f"Invalid input {user_input}")

    if goblin_health > 0:
        print(f"The goblin snarls and lashses out at {hero_name}")
        print(f"The goblin does {goblin_power} damage")
        hero_health -= goblin_power

    if hero_health <= 0:
        print("you have been defeated by the pathetic goblin.")
    elif goblin_health <= 0:
        print("you have defeated the terrible goblin.")
