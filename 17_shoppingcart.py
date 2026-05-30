
foods = []
prices = []
total = 0.0
while True:
    food = input("Enter food item (q to quit): ")
    if food.lower() == 'q':
        break
    price = float(input(f"Enter price for {food}: "))
    foods.append(food)
    prices.append(price)
    total += price


print("Shopping Cart:")
for food in foods:
    print(f"{food}: ${prices[foods.index(food)]:.2f}")
print(f"Total: ${total:.2f}")
