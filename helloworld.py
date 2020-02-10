import datetime
import sys

#Name function
def check_name(name, name_length):
    if name_length >= 10:
        print "There is no way your name is that long. Closing program"
        sys.exit()
    if name[0] == "Z" or name[0] == "z":
        print "Highly unlikely your name starts with Z. This time we will let it slide."

#Input Variable
name = raw_input("What is your name: ")
name_length = len(name)
now = datetime.datetime.now()

#Run Name Check
check_name(name, name_length)

#Display Output
print "\n"
print "Hello my name is " + name + " and it is now " + str(now)
print"\n"
print "There are " + str(name_length) + " characters in this name"

#Manipulate Input
if name == "Mike":
    print "\n"
    print "You are the teacher"
    print "\n"
else: 
    print "You are the student"
    print "\n"
    
#For Loop
for i in range (0, name_length):
    print "Letter number " + str(i + 1) + " in your name is " + name[i]