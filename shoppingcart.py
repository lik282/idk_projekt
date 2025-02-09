foods = []
prices = []
total = []

while True:
    food = input("Enter what food ud like to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        while True:
            price_input = input(f"Enter the price of a {food}: ")
            try:
                price = float(price_input)
                prices.append(price)
                break
            except ValueError:
                print("Please enter a valid number for the price.")

        foods.append(food)

total = sum(prices)
print("-----your cart-----")
for food in foods:
    print(food)

print(f"your total is: {total}")

