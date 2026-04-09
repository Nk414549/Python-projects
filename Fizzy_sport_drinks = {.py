Fizzy_sport_drinks = {
    "Monster":210,
    "Gatorade":140,
    "Redbull":110,
    "powerade":130,
}
print("These are the available drinks ")
for drink in Fizzy_sport_drinks.keys():
    print(drink)

print("These are the calories for each drink")
for calories in Fizzy_sport_drinks.values():
    print(calories)
print("drinks and calories")
for drink, calories in Fizzy_sport_drinks.items():
    print(f"{drink}:{calories}calories")

drink_name = input("Enter the name of the drink: ")
if drink_name in Fizzy_sport_drinks:
    print(f"{drink_name} contains {Fizzy_sport_drinks[drink_name]} calories")
else :
    print (f"Sorry, {drink_name} is not in the list")