print ("Sup nerd tell u your favourite vegitable");
print ("hit enter after each food. Enter q to quit");

favs = [];

while True:
    food = input("Enter a food: ");
    if food == "q":
        break;
    favs.append(food);

for food in favs:
     print("Your favourite vegetables are:", food);
print(favs);
print("Thanks for sharing your favourite vegetables with me!");