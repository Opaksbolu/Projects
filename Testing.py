def main():
 #making a empty list fav_food to store food item entered by the user 
 fav_food=[]
 #in�nite loop used to enter the favorite items until user types quit or Quit or QUIT
 while(True):
 #taking input from user 
    a=input("Please enter your favorite food item ")
 #if input is quit or QUIT or Quit exit 
    if a=="quit" or a=="Quit" or a=="QUIT":
        break
 #else we append the food item to the fav_food list 
 else:
    fav_food.append(a)
 #passing fav_food list to the function completeSentence to print the messages 
 print(fav_food)