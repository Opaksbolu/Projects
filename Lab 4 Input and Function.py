# function definition
def favorite_foods(fav_foods):
# loop to iterate items in the list
    for fav_foods in fav_foods:
# printing message for your item in the list
        print("one of your food items is: ",fav_foods)

# declaration of empty list
fav_foods = []

while True:
        print("\nplease type your favorite foods", end=" ")
        fav_foods_item = input("(please type quit when your done):")
# if item = 'quit' then break the loop
        if fav_foods_item =="quit" or fav_foods_item =="Quit" or fav_foods_item =="QUIT":
                break
# add items in the list
        else:
                fav_foods.append(fav_foods_item)

print()
print()
# function call
favorite_foods(fav_foods)   