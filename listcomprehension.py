#A list.
backpack = ["sword", "shield", "potion", "map", "torch", "sword","rubber duck", "slice of pizza", "parachute"];

#A set.
backpack2 = {"sword", "shield", "potion", "map", "torch","sword","rubber duck", "rubber duck", "slice of pizza", "parachute"};
print(len(backpack));
print(backpack);
print(len(backpack2));
print(*backpack2);

mynewlist = [item for item in backpack2 if item != "sword"];
print(mynewlist);


anotherlist = [];
anotherlist[:] = [item for item in backpack if item != "sword"];
print(anotherlist);