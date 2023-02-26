# Creating a list and replace and select them.
cars = ['Ford', 'Chevy', 'Porsche', 'Ferrari', 'Toyota', 'Lexus', 'Toyota']
print(cars)
print(cars[3])
print(f"I own a {cars[0]} but would like a {cars[5]}.")
cars[4] = 'Tesla'
print(cars)

#Adding to the cars list
cars.append('mazda')
print(cars)

#New list - creating a new list 
supplies = []
supplies.append('Paper')
supplies.append('Pencils')
supplies.append('Stapler')
print(supplies)

#Use insert
supplies.insert(2, 'Eraser')
supplies.insert(0, 'Printer')
print(supplies)

#Removing things from the list
#Using del
del supplies[1]
print(supplies)

#Removing the last item but allows you to still work with it.
#Using pop
my_car = cars.pop(0)
print(my_car)
print(cars)

#Removing using remove
supplies.remove('Printer')
print(supplies)


#Sorting permanently
#Using sort
print(cars)
cars.sort()
print(cars)

scores = [1, 21, 2, 56, 3, 9, 45, 11]
scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

#Sort temp
print('Here is the original')
print(cars)
print('This is temp')
print(sorted(cars))
print('This is back to original')
print(cars)
cars.reverse()
print(cars)

#Finding out the total numbers of words in the list
print(len(cars))

#cars has 7 items
#cars has indexes from 0 to 6
print(cars[-1])
