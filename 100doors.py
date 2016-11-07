door = [0] * 100
text =" " * 5
# 0 means the door is closed
# 1 means the door is open

for i in range(100):
    for j in range(i, 100, i+1):
        if door[j] == 0:
            door[j] = 1
        elif door[j] == 1:
                door[j] = 0


#printing the number of the open doors                
for i in range(100):
    if door[i] == 1:
        text += (str(i+1) + ", ")

print ("The following doors are open: ", text)