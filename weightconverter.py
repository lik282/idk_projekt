weight = float(input("What is your weight? (input a number)"))
chosen_unit = str(input("IN what unit was that? (kg or lbs)"))
if weight > 0:
    print(f"your weight is {weight} in {chosen_unit}")
elif weight < 0:
    print("Retard")
else:
    print("learn to type")





def lbs_to_kg(weight, chosen_unit):
    return weight / 2.20462262
def kg_to_lbs(weight, chosen_unit):
    return weight * 2.20462262


if chosen_unit == "kg":
    print(f"your weight in lbs is :{kg_to_lbs(weight, chosen_unit)}")
if chosen_unit == "lbs":
    print(f"your weight in kgs is :{lbs_to_kg(weight, chosen_unit)}")
else:
    print("invalid input")