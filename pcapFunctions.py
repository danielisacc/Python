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



def caesarCypherEncryption():
    unencrypted = input("Please enter a message: ")
    cypher = int(input("Enter a number between 1 and 25: "))
    encrypted = ""

    for char in unencrypted:
        if (char.isupper()):
            difference = ord('Z') - ord(char)
            if (difference < cypher):
                encrypted += chr(ord('A') + cypher - difference)
            else:
                encrypted += chr(ord(char) + cypher)
        elif (char.islower()):
            difference = ord('z') - ord(char)
            if (difference < cypher):
                encrypted += chr(ord('a') + cypher - difference)
            else:
                encrypted += chr(ord(char) + cypher)
        else:
            encrypted += char
            
    print(encrypted)


def palindromeChecker():
    statement = input("Please input a message: ").replace(" ", "").upper()
    stringArray = list(statement)
    stringArray.reverse()
    print("".join(stringArray) == statement)



def isAnagram():
    word1 = input("Please enter your first phrase: ").replace(" ", "").upper()
    word2 = input("Please enter your second phrase: ").replace(" ", "").upper()
    isAnagram = "Not Anagrams"
    if (word1 != "" and word2 != ""):
        word1 = "".join(sorted(list(word1)))
        word2 = "".join(sorted(list(word2)))
        if (word1 == word2):
            isAnagram = "Anagrams"
    print(isAnagram)



def digitOfLife():
    birthday = input("Please provide your birthday as YYYYDDMM or YYYYMMDD: ")
    totalStr = birthday
    while(len(totalStr) > 1):
        total = 0
        for s in totalStr:
            total += int(s)
        totalStr = str(total)
    print(total)


def wordInPhrase(word, phrase):
    inPhrase = "yes"
    for char in word:
        if (phrase.find(char) < 0):
            inPhrase = "no"
    print(inPhrase)



def read_int(prompt, min, max):
    invalid = True
    val = 0
    while(invalid):
        try:
            val = int(input(prompt))
            if (val >= min and val <= max):
                invalid = False
            else:
                print("Error: the value is not within the permitted range(" , min, "..", max,")")
        except ValueError:
            print("Error: Wrong input. Please enter again as Integer")
    
    return val


class QueueError(LookupError):
    def __init__(self, message = "Queue error"):
        self.value = value
        super().__init__(self.message)

class Queue:
    def __init__(self):
        self.q = []

    def put(self, elem):
        self.q.append(elem)

    def get(self):
        if (len(self.q) == 0):
            raise QueueError()
        else:
            val = self.q[0]
            del self.q[0]
            return val