principle = 0
time = 0
rate = 0

while True:
    principle = float(input('enter the principle amount '))
    if principle < 0:
        print("principle cant be less than zero")
    else:
        break

while True:
    rate = float(input('enter the interest rate amount '))
    if rate < 0:
        print("rate cant be less than zero")
    else:
        break
while True:
    time = float(input('enter the time in years '))
    if time < 0:
        print("time cant be less than zero")
    else:
        break

compound_interest = principle * pow((1 + rate / 100), time)







print(principle)
print(rate)
print(time)
print(f"your balance after {time} year/s is {compound_interest:.2f}")