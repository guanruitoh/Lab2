def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi =weight/(height*height)
    print("BMI = "+ str(bmi))
    underweight = 18.5
    overweight = 25.0
    if bmi<underweight:
        print("You are Under Weight")
    elif bmi>overweight:
        print("You are Over Weight")
    else:
        print("You are Normal Weight")


calculate_bmi(weight=57, height=1.73)

