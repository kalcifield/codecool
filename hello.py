import sys

if len(sys.argv) > 1:                    #if you enter argument (for e.g.: a name), the script welcomes him
    print("Hello " + sys.argv[1] + "!")
else:
    print("Hello World!")                #in case of no argument, the script welcomes the world