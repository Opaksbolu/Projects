colors = ['Red', 'Purple', 'Blue', 'Green', 'Fuschia', 'Yellow']
for bob in colors:
    print(f"This is one of the color's in our house {bob}.")

print("Do we need any more colors?")

#numbers
for value in range(1, 12, 2):
    print(value)

number = list(range(2, 25, 3))
print(number)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

#Slices
print(colors)
print(colors[1:3])
print(colors[:4])
fav_colors = colors[:3]
print(fav_colors)
colors.append("orange")
fav_colors.append("cyan")
print(fav_colors)
print(colors)

#Lists use []
#Tuples use ()

animals = ('Lion', 'Tiger')
print(animals)

for animal in animals:
    print(animal)

animals = ("dog", "coyote")
print(animals)