def mysplit(strng):
    newString = strng.strip()
    stringArray = []
    if(newString == ""): return stringArray
    
    currentString = ""
    for char in newString:
        if(not char.isalnum() or char == " "):
            if (currentString != ""):
                stringArray.append(currentString)
            currentString = "";
        else:
            currentString += char
    stringArray.append(currentString)
    return stringArray

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))



def numToSevenDisplay(displayNum):
    displayMatrix = [
    # 0
        ['###',
         '# #',
         '# #',
         '# #',
         '###'],
    # 1     
        [' # ',
         ' # ',
         ' # ',
         ' # ',
         ' # '],
    # 2    
        ['###',
         '  #',
         '###',
         '#  ',
         '###'],
    # 3     
        ['###',
         '  #',
         '###',
         '  #',
         '###'],
    # 4
        ['# #',
         '# #',
         '###',
         '  #',
         '  #'],
    # 5    
        ['###',
         '#  ',
         '###',
         '  #',
         '###'],
    # 6    
        ['###',
         '#  ',
         '###',
         '# #',
         '###'],
    # 7   
        ['###',
         '  #',
         '  #',
         '  #',
         '  #'],
    # 8    
        ['###',
         '# #',
         '###',
         '# #',
         '###'],
    # 9    
        ['###',
         '# #',
         '###',
         '  #',
         '###']
    ]

    stringNum = str(displayNum)
    numArray = [int(num) for num in stringNum]

    for row in range(5):
        for num in numArray:
            print(displayMatrix[num][row] ,end = " ")
        print('\n')

numToSevenDisplay(123)