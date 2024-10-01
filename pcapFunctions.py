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
