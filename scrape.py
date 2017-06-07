import re
import os

with open("pk1") as f:
    content1 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content1 = [x.strip() for x in content1] 

with open("pk2") as f:
    content2 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content2 = [x.strip() for x in content2] 

with open("pk3") as f:
    content3 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content3 = [x.strip() for x in content3] 

with open("pk4") as f:
    content4 = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content4 = [x.strip() for x in content4] 



def search(filename, string):   #searches for first occurence of string in filename (for find how many tests per class)
    x = 0
   # print(string)
    while filename[x] != string:
        x+=1
    return x

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def firstregexmatch(filename):
    regex = re.compile('\d*,*\d*\/\d*')
    x = 0
    while not regex.match(filename[x]):
        #print(filename[x])
        x+=1
    return x

#print(content1[firstregexmatch(content1)])

def lastregexmatch(filename):
    regex = re.compile('\d*,*\d*\/\d*')
    x = firstregexmatch(filename)
    while regex.match(filename[x]):
        #print(filename[x])
        x+=1
    return x
#print(lastregexmatch(content1))


def firstdatematch(filename):
    regex = re.compile('\d+\s(januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december)')
    x = 0
    while not regex.match(filename[x]):
        #print(filename[x])
        x+=1
    return x

#print(content1[firstdatematch(content1)])

def lastdatematch(filename):
    print(len(filename))
    regex = re.compile('\d+\s(januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december)')
    x = firstdatematch(filename)
    while regex.match(filename[x]):
#        print(x)
#        print(filename[x])
        x+=3
        if x > len(filename)-1:
            y = x - 3
            x = 0
    return y
#print(lastdatematch(content1))


class Vak():
            
    def __init__(self, name): #inits object with subject name
        self.name = name
    
    def appendtofile(self, data): #opens a new file and appends "data" to it
        file = open(self.name,"a+")
        file.write("%s\r\n" % (data))
        return

    def teachername(self, content): #outputs name of teacher for subject
        return content[search(content,  self.name) + 1]
    
    def amount(self, content): #outputs amount of tests made for subject
        x = content[search(content,  self.name) + 2]
        if is_number(x):
            return x
        else:
            return 0









### Init classes
Aardrijkskunde = Vak("Aardrijkskunde")
Engels = Vak("Engels")
Frans = Vak("Frans")
Geschiedenis = Vak("Geschiedenis")
Godsdienst = Vak("Godsdienst")
Lichamelijke_Opvoeding = Vak("Lichamelijke Opvoeding")
Nederlands = Vak("Nederlands")
Toegepaste_Chemie = Vak("Toegepaste Chemie")
Toegepaste_Fysica = Vak("Toegepaste Fysica")
Toegepaste_Wiskunde = Vak("Toegepaste Wiskunde")
Wiskunde = Vak("Wiskunde")
Elektrische_Wetenschappen_Elektriciteit = Vak("Elektrische Wetenschappen - Elektriciteit")
Elektrische_Wetenschappen_Elektronica = Vak("Elektrische Wetenschappen - Elektronica")
Engineering = Vak("Engineering")
Mechanische_Wetenschappen = Vak("Mechanische Wetenschappen")
GIP_Productevaluatie = Vak("GIP Productevaluatie")
GIP_Procesevaluatie = Vak("GIP Procesevaluatie")
klassen = [Aardrijkskunde, Engels, Frans, Geschiedenis, Godsdienst, Lichamelijke_Opvoeding, Nederlands, Toegepaste_Chemie, Toegepaste_Fysica, Toegepaste_Wiskunde, Wiskunde, Elektrische_Wetenschappen_Elektriciteit, Elektrische_Wetenschappen_Elektronica, Engineering, Mechanische_Wetenschappen, GIP_Productevaluatie, GIP_Procesevaluatie]


#print(regexmatch(content1)) #finds the first occurence of grade,decimalgrade/maxgrade

 
def debug(): #debug function, for testing
    total=0
    for i in klassen: #Begint met naam van de leerkracht
        i.appendtofile("Vak: %s" % (i.name))  
        i.appendtofile("Leerkracht: %s" % (i.teachername()))
        total += float(i.amount())
        print("%s added %s" % (i.name, i.amount()))
        print(total)
    print(lastregexmatch(content1) - firstregexmatch(content1)) 

def writegradestofile(content):
    first = firstregexmatch(content)
    firstdate = firstdatematch(content)
    total=0
    pointer=0
    for i in klassen:
        amount = int(i.amount(content))
        while pointer < amount: #zolang da uw pointer minder is dan uw totaal
            pointer += 1 
            data = ('{} {} {}'.format(content[firstdate + 3*(pointer-1)], content[firstdate + 3*(pointer-1)+2], content[first - 1 + pointer]))
            print(data)
            i.appendtofile(data)

        pointer = 0
        first += amount
        firstdate += amount*3

#print(Aardrijkskunde.amount(content1))
#print(Aardrijkskunde.amount(content2))
#print(Aardrijkskunde.amount(content3))
#print(Aardrijkskunde.amount(content4))
writegradestofile(content1)
writegradestofile(content2)
writegradestofile(content3)
writegradestofile(content4)


#debug()

#So if aard has no tests, skip
#if engels has 8 tests: 
#
#

