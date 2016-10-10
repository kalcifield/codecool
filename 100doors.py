num_doors = 100
door = ["closed"] * num_doors
text =" "

for i in range(len(door)):
    for j in range(i, len(door), i+1):
        if door[j] == "closed":
            door[j] = "open"
        elif door[j] == "open":
                door[j] = "closed"
for i in range(len(door)):
    if door[i] == "open":
        text += (" " + str(i+1))

print ("The following doors are open: ", text)  