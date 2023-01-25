#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

def favourite_book(title):
    print(f'One of my favourite books is {title}')

favourite_book('Alice in Wonderland')
favourite_book('One Flew Over the Rainbow')
favourite_book('Dune')

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country="USA"):
    print(f'Visit {city} in this {country}')

describe_city("Austin")
describe_city("New Orleans")
describe_city("Berlin", "Germany")

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(art_name, album_title, tracks = 0):
    album = {'Artist':art_name, 'Title': album_title}
    if tracks:
        album['Tracks'] = tracks
    return album

current_album = make_album("Michael jackson", "Thriller")
print(current_album)
next_album = make_album("The Weekend", "Starwood")
print(next_album)
oldie_album = make_album("Beetles", "Abbeyroad", 10)
print(oldie_album)

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
def show_message(msg_lists):
    for msg in msg_lists:
        print(msg)

messages = ["Thank you it's Friday", "Happy Halloween", "Have a good day"]
show_message(messages)

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
def make_sandwich(*ingredients):
    print(f'Your sandwich has the following ingredients: ')
    for ingredient in ingredients:
        print(f'--{ingredient}')

make_sandwich('Ham', 'Tomatoes', 'Lettuce')
make_sandwich('Turkey', 'Mayo', 'Wheat bread', 'Swiss cheese')
make_sandwich('Peanut butter', 'Banana', 'White bread')