def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi =weight/(height*height)
    print("BMI = "+ str(bmi))
    underweight = 18.5
    overweight = 25.0
    if bmi<underweight:
        print("You are Under Weight")
        return -1
    elif bmi>overweight:
        print("You are Over Weight")
        return 0
    else:
        print("You are Normal Weight")
        return 1

calculate_bmi(weight=57, height=1.73)

