backpack = ["pizza slice", "button", "pizza slice", "fishing pole ", "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"];
print(backpack);


for index in range(len(backpack) // 2):
   backpack[index], backpack[-index-1] = backpack[-index-1], backpack[index];
print(backpack);