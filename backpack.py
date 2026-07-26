backpack = ["pizza slice", "button", "pizza slice", "fishing pole ", "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"];
print(backpack);


for index in range(len(backpack) // 2):
   backpack[index], backpack[-index-1] = backpack[-index-1], backpack[index];
print(backpack);


# Reverse the list using slicing without creating a new list.
backpack[:] = backpack[::-1];

print(backpack);

# Reverse the list using slicing and creating a new list.
backpack2 = backpack[::-1];  
print(backpack2);

#reverse the list using the built-in reverse() method.
backpack.reverse();
print(backpack);

#reversing  a list using the built-in reversed() function.
backpack3 = list(reversed(backpack));
print(backpack3);

#Reverse the list using a for loop.
backpack4 = [];
for i in range(len(backpack) - 1, -1, -1):
    backpack4.append(backpack[i]);
print(backpack4);