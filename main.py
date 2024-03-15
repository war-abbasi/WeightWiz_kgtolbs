print("Can't wait to see your converted WEIGHT? ;)")
weight = input("Weight: ")
unit = input("Weight is in Kg or Lbs? ")
if unit.lower() == "kg":
    converted_weight = float(weight) / 0.45
    print("Weight in Lbs: " + str(converted_weight))
else:
    converted_weight = float(weight) * 0.45
    print("Weight in Kgs: " + str(converted_weight))