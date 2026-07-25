x = 30000;
for i in range(0, 120):
    print (x*0.00417);
    x = (x * 0.00417) + x;
    print(f"Month {i + 1}: ${x:,.2f}");

print(f"Total after 10 years: ${x:,.2f}");
print(f"Total interest earned: ${x - 30000:,.2f}");
print(f"Total monthly payment after 10 years: ${x/120:,.2f}");
