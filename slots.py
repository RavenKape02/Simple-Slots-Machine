import sys
import random
import time
import pickle

username = input("Enter your username: ")

try:
    with open("money_storage", 'rb') as file:
        money_database = pickle.load(file)
        money_database = dict(sorted(money_database.items(), key= lambda item: item[1], reverse=True))
except:
    money_database = {}
    with open("money_storage", 'wb') as file:
        pickle.dump(money_database, file)


display_money = ""
if len(money_database) < 10:
    for keys, values in money_database.items():
        display_money = "→  " + str(keys) + ":" + str(values) + "\n"
else:
    c = 0
    for keys, values in money_database.items():
        c += 1
        if c > 5:
            break
        display_money += "→  " + str(keys) + ":" + str(values) + "\n"
print("Richest people:\n", display_money)

if username in money_database:
    current_money = money_database[username]
else:
    current_money = 5000

emojis_list = ['🍋','🍑','🍓','🐸','🎖','💰','👑']
emoji_values = {1:[3,1], 2:[5,1.2], 3:[10,1.5], 4:[15,2], 5:[20, 3], 6:[50,5], 7:[100, 10]}
def slots_machine(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        animation_first_emoji = random.randint(1,7)
        animation_second_emoji = random.randint(1,7)
        animation_third_emoji = random.randint(1,7)
        for i in range(4):
            sys.stdout.write('\r'+emojis_list[animation_first_emoji-1]+"|"+emojis_list[animation_second_emoji-1]+"|"+emojis_list[animation_third_emoji-1])
            time.sleep(0.1)

while True:
    if current_money == 0:
        print("Damn, you lost all your money? what a shame. Don't worry I got you this 5000. Bet it wisely")
        current_money = 5000
    print("Your current money:", current_money)
    response = input("Do you want to play? (type \"yes\" or \"no\"): ")
    if response.lower() == "yes":
        while True:      
            bet = float(input("Bet Amount:"))
            if bet <= current_money:
                break
            else:
                print("You can't apply for loans here, sorry")
        first_value = random.randint(1,7)
        second_value = random.randint(1,7)
        third_value = random.randint(1,7)
        slots_machine(3)
        sys.stdout.write('\r'+emojis_list[first_value-1]+"|"+emojis_list[second_value-1]+"|"+emojis_list[third_value-1]+"\n")
        if first_value == second_value == third_value:
            winnings = emoji_values[first_value][0]*bet
            print("Your bet:", bet)
            print("Winnings:", winnings)
        elif first_value == second_value or first_value == third_value:
            winnings = emoji_values[first_value][1]*bet
            print("Your bet:", bet)
            print("Winnings:", winnings)
        elif second_value == third_value:
            winnings = emoji_values[second_value][1]*bet
            print("Your bet:", bet)
            print("Winnings:", winnings)
        else:
            current_money -= bet
            winnings = 0
            print("How sad, you didn't won anything")
        current_money += winnings
    else:
        money_database[username] = current_money
        with open("money_storage", 'wb') as file:
            pickle.dump(money_database, file)
        break