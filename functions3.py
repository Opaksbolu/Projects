#Arguement variations
def ingrdients(*items):
    print("These are the items we need: ")
    for item in items:
        print(f'{item}')

ingrdients('Apples', 'Caramel', 'Nuts')

def supper(time, *items):
    print(f"We are having supper {time} tonight, we are having: ")
    for item in items:
        print(f'-{item}')
supper('6:30', 'Spaghetti', 'Rolls', 'Meatballs', 'Salad', 'Apple pie')
