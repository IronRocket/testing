def combination(objects,maxlength):
    num = str(len(objects)**int(maxlength))
    counter = 0
    conversion = []
    for char in num[::-1]:
        counter += 1
        if counter == 3:
            counter = 0
            conversion.append(","+char)
        else:
            conversion.append(char)
    num = ""
    for item in conversion[::-1]:
        num += item
    complete_list = []
    for current in range(4):
        a = [i for i in objects]
        for y in range(current):
            a = [x+i for i in objects for x in a]
        complete_list = complete_list+a
    print("Number of combinations:",num)
    input("")
    print(complete_list)