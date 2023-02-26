#3-1 creating names list
names = ['Tega', 'Tumise', 'Daniella', 'Atiat', 'Jessica', 'Ise', 'Nifemi']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

#3-4 creating a guest list with a message
guests = ['Taiwo', 'Eniola', 'Ifeoluwa', 'Olanrewaju']
for guest in guests:
    print(f"Hello {guest} You have been invited to my birthday party that is happening on the 25th of December at the Folas house.")
#3-5 changing the guest list
guests [3] = 'Tega'
for guest in guests:
    print(f"Hello {guest} You have been invited to my birthday party that is happening on the 25th of December at the Folas house.")
#3-6 more guests
guests.insert(0, 'Olatunji')
guests.insert(2, 'Kenny')
guests.append('Olanrewaju')
for guest in guests:
    print(f"Hello {guest} You have been invited to my birthday party that is happening on the 25th of December at a new venue at Madison Square Garden.")
#3-7 shrinking guest list
for guest in guests:
    print(f"Hello {guest} I can only invite two people to Madison Square Garden.")
guests.pop(0)
guests.pop(1)
guests.pop(1)
guests.pop(2)
guests.pop(2)
for guest in guests:
    print(f"Hello {guest} you have been invited to Madison Square Garden to celebrate my birthday.")
#3-8 seeing the world
addresses = ['Popeyes', 'Panda Express', 'Red Lobsters', 'Mc Dolnalds', 'Wendy', 'Taco Bells', 'Chick Fila', 'Arbys']
print(addresses)
addresses.sort()
print(addresses)
addresses = ['Popeyes', 'Panda Express', 'Red Lobsters', 'Mc Dolnalds', 'Wendy', 'Taco Bells', 'Chick Fila', 'Arbys']
addresses.sort(reverse=True)
print(addresses)
addresses = ['Popeyes', 'Panda Express', 'Red Lobsters', 'Mc Dolnalds', 'Wendy', 'Taco Bells', 'Chick Fila', 'Arbys']
addresses.sort()
print(addresses)
addresses = ['Popeyes', 'Panda Express', 'Red Lobsters', 'Mc Dolnalds', 'Wendy', 'Taco Bells', 'Chick Fila', 'Arbys']
addresses.sort(reverse=True)
print(addresses)
addresses.sort()
print(addresses)
addresses.sort(reverse=True)
print(addresses)

#4-1 Pizzas
pizzas = ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Hawaiian', 'Buffalo', 'Meat', 'Veggie']
for pizza in pizzas:
    print(f'I love {pizza} pizza.')
fpizzas = ['Hawaiian', 'Buffalo', 'BBQ and Pineapple']
for fpizza in fpizzas:
    print(f'My favourite type of pizza is {fpizza} pizza.')
print('I really love pizza!!!')

#4-2 Animals
animals = ['Dogs', 'Cats', 'Elephant', 'Horse', 'Cows']
for animal in animals:
    print(f'{animal}:')
    print(f'A {animal} could make a great pet if tamed well.')
    print(f'A {animal} is an example of a 4 legged animal.')
#4-3 Counting to 20
for value in range(1, 21):
    print(value)
#4-7 Threes
for value in range(3, 33, 3):
    print(value)
#4-11 My Pizzas, Your Pizzas
pizzas.append('Olive')
friend_pizzas = ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Hawaiian', 'Buffalo', 'Meat', 'Veggie']
for pizza in pizzas:
    print(f'My favorite pizzas are: {pizza}.')
for friend_pizza in friend_pizzas:
    print(f'My friends favorite pizzas are: {friend_pizza}.')
#4-13 Buffet
sfood = ('Rice and Chicken', 'Pasta and Sauce', 'Pizza and Ice Cream', 'Burgers and Slushies', 'Cookies and Milk')
for simple_food in sfood:
    print(f'In our restuarant, our main food is {simple_food}.')
sfood [0] = 'Bread and Jam'
sfood = ('Cake and Popsicles', 'Bread and Jam', 'Pizza and Ice Cream', 'Burgers and Slushies', 'Cookies and Milk')
for simple_food in sfood:
    print(f'In our restuarant, our main food is {simple_food}.')