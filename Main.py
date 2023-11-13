height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height**2)
BMI=round(bmi, 1)

if bmi < 18.5:
    print(f"Your BMI is {BMI}, You are Underweight!")
elif bmi < 25:
    print(f"Your BMI is {BMI}, You have a normal Weight!")
elif bmi < 30:
    print(f"Your BMI is {BMI}, You are slightly Overweight!")
elif bmi < 35:
    print(f"Your BMI is {BMI}, You are Obese!")
elif bmi >= 35:
    print(f"Your BMI is {BMI}, You are clinically Obese!")