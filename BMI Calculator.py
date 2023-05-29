while True:
    print("Enter 1 to check BMI")
    print("Enter any other key to exit calculator")
    ch=input()
    if ch == '1':
        wt=float(input("Enter your weight in kgs"))
        ht=float(input("Enter your height in meters"))
        bmi=wt/(ht**2)
        print("Your BMI is ","%.2f"% bmi)
        if bmi <= 18.5:
            print("You are underweight")
            print("Try to eat more frequently , choose food with lots of nutrients and stay happy\n")
        elif bmi > 18.5 and bmi <=25:
            print("You are healthy")
            print("Maintain your health and stay happy\n")
        elif bmi > 25 and bmi <=30:
            print("You are overweight")
            print("Switch to a healthy diet , exercise regularly and stay happy\n")
        else:
            print("You are obese")
            print("Consider joining any weight loss program or \ntake any weight loss medicine with doctors prescription and stay happy\n")
    else:
        break
