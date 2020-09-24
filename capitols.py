# Python from David Martinez
# Capitols dictionary thing

#import urllib2
#f = urllib2.urlopen("https://projects.intra.42.fr/uploads/document/document/1135/capitols.txt")
f = open("C:\\Users\davma\Downloads\capitols.txt", "r")
capDict = {}
for line in f:
    lx = line.split(",")  # splits line by comma
    a = lx[0]
    b = lx[1]
    lengthC = len(b)-1
    b = b[0:lengthC]
    capDict[a] = b
#
f = open("C:\\Users\davma\Downloads\capitols.txt", "r")
stateDict = {}
for line in f:
    ly = line.split(",")  # splits line by comma
    ay = ly[0]
    bx = ly[1]
    lengthY = len(bx)-1
    bx = bx[0:lengthY]
    stateDict[bx] = ay
#
while(1<2):
    dictIn = input("Ready: ")
    if dictIn in capDict:
        print(capDict[dictIn])
    elif dictIn in stateDict:
        print(stateDict[dictIn])
    elif dictIn == "Done.":
        break
    else:
        print("nil") 
#

      
#S




