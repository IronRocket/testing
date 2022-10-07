equation = input("Enter equation:").strip(" ")
x,y = input("Enter x and y:").split(",")

operators = ("<",">","≥","≤","=")
for char in equation:
    if char in operators:
        operator = char
        axes,main = equation.split(char)
        axes = axes.strip(" ")
        main = main.strip(" ")
        main_equation = []
        for char in main:
            main_equation.append(char)
        break
counter = 0

if axes == "y":
    for char in main_equation:
        if char == "x":
            main_equation[counter] = "*"+x+")"
            for char in main_equation:
                count = counter
                counter -= 1
                if main_equation[counter] in operators:
                    main_equation[counter] = "("+main_equation[counter]
                    break
                if counter == 0:
                    main_equation[counter] = "("+main_equation[counter]
            counter = count
        counter += 1
else:
    for char in main_equation:
        if char == "y":
            main_equation[counter] = "*"+y+")"
            for char in main_equation:
                count = counter
                counter -= 1
                if main_equation[counter] in operators:
                    main_equation[counter] = "("+main_equation[counter]
                    break
                if counter == 0:
                    main_equation[counter] = "("+main_equation[counter]
            counter = count
        counter += 1

main = ""
for char in main_equation:
    main += char
original_main = main

exec(f"main = {main}")

y = int(y)
x = int(y)
if operator == "=":
    if y == main:
        print("Y is equal to",original_main)
    else:
        print("Y is not equal to",original_main)

print("Y is:",main)


input()