from math import *

app = True

print("      =============    ===============    ==============")
print("     ===============   ===============  ==============  ")
print("    =====              ====            ====             ")
print("    ==============     ===========    ====              ")
print("     ==============    =========      ====              ")
print("                =====  ====           ====              ")
print("                =====  ====            ====             ")
print("    ================   ===              ==============  ")
print("   ==============      ===                ==============")
print("                                                     by pxello ")
print("                   ")
print("                   ")

while app == True:
    userShape = str(input("enter a shape (circle /rectangle /square /triangle): "))

    if userShape == "circle":
        print("shape: ",userShape)
        userShape = userShape
        print("type '/' to calculate the values from the features")
        shapeFeature = str(input("what feature you wanna calculate? (area /circumference): "))
        if shapeFeature == "area":
            print("shape: ",userShape)
            print("feature: area")
            shapeFeature = shapeFeature
            try:
                r = float(input("enter a value (number): "))
                result = r**2 * 3.14
                print(f"{r}² × π = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")

        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                r = float(input("enter a value (number): "))
                result = r * 3.14
                print(f"{r} × π = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")

        elif shapeFeature == '/':
            print("shape: ",userShape)
            userFeature = str(input("enter the feature (area /circumference): "))
            print("feature: ", userFeature)

            if userFeature == "area":
                try:
                    userFeatureValue = float(input("enter the area value: "))
                    result = sqrt(userFeatureValue / 3.14)
                    print(f"√({userFeatureValue} ÷ 3.14) = {result}")
                except:
                    print(" --error: Invalid value.. please enter an integer or a decimal")

            elif userFeature == "circumference":
                try:
                    userFeatureValue = float(input("enter the circumference value: "))
                    result = userFeatureValue / 3.14
                    print(f"{userFeatureValue} ÷ 3.14 = {result}")
                except:
                    print(" --error: Invalid value.. please enter an integer or a decimal")

            else:
                print(" --feature is Invalid :( ")

        else:
            print(" --feature is Invalid :( ")

    elif userShape == "rectangle":
        print("shape: ",userShape)
        userShape = userShape
        print("type '/' to calculate the values from the features")
        shapeFeature = str(input("what feature you wanna calculate? (area /circumference): "))

        if shapeFeature == "area":
            print("shape: ",userShape)
            print("feature: area")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                y = float(input("enter a value (number): "))
                result = (x*y) / 2
                print(f"({x} × {y}) ÷ 2 = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")
            
        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                y = float(input("enter a value (number): "))
                result = (x+y) * 2
                print(f"({x} + {y}) × 2 = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")

        elif shapeFeature == '/':
            print("shape: ",userShape)
            userFeature = str(input("enter the feature (area /circumference): "))
            print("feature: ", userFeature)

            if userFeature == "area":
                try:
                    userFeatureValue = float(input("enter the area value: "))
                    x = float(input("enter a value (number): "))
                    result = (userFeatureValue * 2) / x
                    print(f"({userFeatureValue} × 2) ÷ {x} = {result}")
                except:
                    print(" --error: Invalid x value or Invalid area value.. please enter an integer or a decimal")

            elif userFeature == "circumference":
                try:
                    userFeatureValue = float(input("enter the area value: "))
                    x = float(input("enter a value (number): "))
                    result = (userFeatureValue / 2) - x
                    print(f"({userFeatureValue} ÷ 2) - {x} = {result}")
                except:
                    print(" --error: Invalid x value or Invalid area value.. please enter an integer or a decimal")
        
        else:
            print(" --feature is Invalid :( ")

    elif userShape == "square":
        print("shape: ",userShape)
        userShape = userShape
        print("type '/' to calculate the values from the features")

        shapeFeature = str(input("what feature you wanna calculate? (area /circumference): "))
        if shapeFeature == "area":
            print("shape: ",userShape)
            print("feature: area")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                result = x**2
                print(f"{x} × {x} = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")
    
        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                result = x*4
                print(f"{x} × 4 = {result}") 
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")

        elif shapeFeature == '/':
            print("shape: ",userShape)
            userFeature = str(input("enter the feature (area /circumference): "))
            print("feature: ", userFeature)

            if userFeature == "area":
                try:
                    userFeatureValue = float(input("enter the area value: "))
                    result = sqrt(userFeatureValue)
                    print(f"√{userFeatureValue} = {result}")
                except:
                    print(" --error: Invalid area value.. please enter an integer or a decimal")
                
            elif userFeature == "circumference":
                try:
                    userFeatureValue = float(input("enter the circumference value: "))
                    result = userFeatureValue / 4
                    print(f"{userFeatureValue} ÷ 4 = {result}")
                except:
                    print(" --error: Invalid area value.. please enter an integer or a decimal")

        else:
            print(" --feature is Invalid :( ")

    elif userShape == "triangle":
        print("shape: ",userShape)
        userShape = userShape
        print("type '/' to calculate the values from the features")

        shapeFeature = str(input("what feature you wanna calculate? (area /circumference): "))
        if shapeFeature == "area":
            print("shape: ",userShape)
            print("feature: area")
            shapeFeature = shapeFeature
            try:
                h = float(input("enter a value (number): "))
                b = float(input("enter a value (number): "))
                result = (h*b) /2
                print(f"({h} × {b}) ÷ 2 = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")
            
    
        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                y = float(input("enter a value (number): "))
                z = float(input("enter a value (number): "))
                result = x+y+z
                print(f"{x} + {y} + {z} = {result}")
            except:
                print(" --error: Invalid value.. please enter an integer or a decimal")
        
        elif shapeFeature == '/':
            print("shape: ",userShape)
            userFeature = str(input("enter the feature (area /circumference): "))
            print("feature: ", userFeature)

            if userFeature == "area":
                try:
                    userFeatureValue = float(input("enter the area value: "))
                    userValue = str(input("what value do you wanna calculate (base /height): "))
                    if userValue == "base":
                        h_value = float(input("enter the height value: "))
                        result = (userFeatureValue / 2) / h_value
                        print(f"({userFeatureValue} ÷ 2) ÷ {h_value} = {result}")
                    
                    elif userValue == "height":
                        b_value = float(input("enter the height value: "))
                        result = (userFeatureValue / 2) / b_value
                        print(f"({userFeatureValue} ÷ 2) ÷ {b_value} = {result}")
                except:
                    print(" --error: Invalid value.. please enter an integer or a decimal")

            elif userFeature == "circumference":
                try:
                    userFeatureValue = float(input("enter the circumference value: "))
                    triangleType = str(input("is the triangle an equilateral triangle? (yes/no): "))
                    if triangleType == "yes":
                        result = userFeatureValue / 3
                        print(f"{userFeatureValue} ÷ 3 = {result}")
                    
                    elif triangleType == "no":
                        x = float(input("enter a value (number): "))
                        y = float(input("enter a value (number): "))
                        result = userFeatureValue - (x+y)
                        print(f"{userFeatureValue} - ({x} + {y}) = {result}")
                    
                    else:
                        print(" --error: Invalide answer.. please type 'yes' or 'no'")
                except:
                    print(" --error: Invalid value.. please enter an integer or a decimal")

        else:
            print(" --feature is Invalid :( ")

    else:
        print(" --shape is Invalid :(")