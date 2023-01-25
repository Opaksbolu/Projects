#returning values

def userName(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

player_name = userName('Sam', 'Spade')
print(player_name)

def newUser(first_name, last_name, middle_name = ''):
    if middle_name:
        new_name = f'{first_name} {last_name} {middle_name}'
    else:
        new_name = f'{first_name} {last_name}'
    return new_name.title()

print(newUser('Davy', 'Jones'))
print(newUser('James', 'T', 'Kirk'))
print(newUser('James', 'Kirk', 't'))

#Creating a dictionary with a function

def petShop(pet_id, pet_name):
    pet = {'Id': pet_id, 'Name': pet_name}
    return

newPet = petShop(244, 'peturnia')
newPet = petShop(64, 'Bubbles')
print(newPet)

#passing in a list 
def howdy(names):
    for name in names:
       msg = f'Howdy, {name.title}'
