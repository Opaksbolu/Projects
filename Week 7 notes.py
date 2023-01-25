#basic function

def howdy(user):
    print(f'howdy {user}')


howdy('sally')
#Pay attention to the order of the arguements and make sure they match your program
def user(first_name, age):
    print(f'Users: {first_name} {age}')

user('Paul', 12)
user(24, 'Pam')

#using key pairs to get rid or order requirements
def oldUser(name, age):
    print(f'Our senoir user, {name} is {age} years old.')

oldUser(name = 'Bob', age = 90)
oldUser(age = 68, name = 'Joe')

#setting up defaults
def describeCar(model, make="Ford"):
    print(f"The vehicle is a {make} {model}.")

describeCar("Mustang")
describeCar("Altima", "Nissan")


