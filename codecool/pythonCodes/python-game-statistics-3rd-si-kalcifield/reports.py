
# Report functions




def count_games(file_name):
    myfile = open(file_name)
    num_lines = sum(1 for line in myfile)
    myfile.close()
    return num_lines



def decide(file_name, year):
    givenYear = str(year)
    if givenYear in open(file_name).read():
        return True
    else:
        return False

"""def get_latest(file_name):
    largestInt = 0
    with open(file_name) as f:
        content = f.readlines()
        for line in content:"""



def count_by_genre(file_name, genre):
    with open(file_name) as myFile:
        counter = 0
        for num, line in enumerate(myFile, 1):
            if genre in line:
                counter += 1
        return counter




def get_line_number_by_title(file_name, title):
    myfile = open(file_name)
    num_lines = sum(1 for line in myfile)
    myfile.close()
    # opens the file to count the lines and stores it in a variable
    with open(file_name) as myFile:
        found = False
        counter = 0
        for num, line in enumerate(myFile, 1):
            counter += 1
            if title in line:
                found = True
                return num
                #returns the number of the line for the title
            if found == False and counter == num_lines:
                raise ValueError("no game found")
                # raises valueerror if there was no game with the given title



