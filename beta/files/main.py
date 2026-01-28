app = True

print("          sfc      ")
print("            Pxello /_")
print("                  /___ ")
print("                 /_____ ")
print("                /_______ ")
print("               /_________ ")
print("                   ")
print("                   ")

while app == True:
    userShape = str(input("enter a shape (circle /rectangle /square /triangle...): "))

    if userShape == "circle":
        print("shape: ",userShape)
        userShape = userShape
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
                print("error: Invalid value.. please enter an integer or a decimal")
    
        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                r = float(input("enter a value (number): "))
                result = r * 3.14
                print(f"{r} × π = {result}")
            except:
                print("error: Invalid value.. please enter an integer or a decimal")

        else:
            print("feature is Invalid ☹️ ")

    elif userShape == "rectangle":
        print("shape: ",userShape)
        userShape = userShape
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
                print("error: Invalid value.. please enter an integer or a decimal")
            
    
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
                print("error: Invalid value.. please enter an integer or a decimal")

        else:
            print("feature is Invalid ☹️ ")

    elif userShape == "square":
        print("shape: ",userShape)
        userShape = userShape
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
                print("error: Invalid value.. please enter an integer or a decimal")
    
        elif shapeFeature == "circumference":
            print("shape: ",userShape)
            print("feature: circumference")
            shapeFeature = shapeFeature
            try:
                x = float(input("enter a value (number): "))
                result = x*4
                print(f"{x} × 4 = {result}") 
            except:
                print("error: Invalid value.. please enter an integer or a decimal") 

        else:
            print("feature is Invalid ☹️ ")

    elif userShape == "triangle":
        print("shape: ",userShape)
        userShape = userShape
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
                print("error: Invalid value.. please enter an integer or a decimal")
            
    
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
                print("error: Invalid value.. please enter an integer or a decimal")

        else:
            print("feature is Invalid ☹️ ")

    else:
        print("shape is Invalid ☹️")