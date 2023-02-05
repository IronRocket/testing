print("Comparision signs: ≤ ≥ =")
equation = input("Equation:")
x,y = input("Enter position in graph:").split(",")
x,y = x.strip(" "),y.strip(" ")

operators = (">","<","=","≤","≥")
comparison = ""
for char in equation:
  if char in operators:
    comparison = char
    axes,_ = equation.split(char)
    axes,_ = axes.strip(" "),_.strip(" ")
    main_equation = []*len(_)
    for char in _: main_equation.append(char)  
    break

counter = 0
for char in main_equation:
  if char == "x":
    main_equation[counter] = x+")"
    print(main_)
    count = -1
    for char in main_equation:
      if main_equation[count] in operators:
        main_equation[count+1] = "("+main_equation[count+1]
      count -= 1
  else:
    main_equation[counter] = y
  counter += 1
replaced_variables = ""
for char in main_equation:
  replaced_variables += char
print(replaced_variables)