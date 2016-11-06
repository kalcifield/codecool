
# Report functions


#def get_most_played(file_name)

def sum_sold(file_name):
    with open(file_name) as myFile:
        counter = 0
        for num, line in enumerate(myFile, 1):
            ke = list(line)
            tab = 0
            nums = []
            for i in ke:
                if i == "\t":
                    tab += 1
                if tab == 1:
                    nums.append(i)
            s = float(''.join(nums))
            counter += s
        return counter

def get_selling_avg(file_name):
    with open(file_name) as myFile:
        number_of_games = 0
        counter = 0
        for num, line in enumerate(myFile, 1):
            number_of_games += 1
            ke = list(line)
            tab = 0
            nums = []
            for i in ke:
                if i == "\t":
                    tab += 1
                if tab == 1:
                    nums.append(i)
            s = float(''.join(nums))
            counter += s
        avg_sell = counter / number_of_games
        return avg_sell


# nemjó. egy listbe kéne tenni a title-ket, vesszővel elválasztva, majd max-al megkeresni a leghosszabbat   
"""def count_longest_title(file_name):   
    with open(file_name) as myFile:
        counter = []
        for num, line in enumerate(myFile, 1):
            ke = list(line)
            tab = 0
            nums = []
            for i in ke:
                if i == "\t":
                    tab += 1
                if tab == 0:
                    nums.append(i)
            s = ''.join(nums)
            counter += s
        test = ''.join(counter)
        print(test)"""


def get_date_avg(file_name):
    with open(file_name) as myFile:
        number_of_lines = 0
        counter = 0
        for num, line in enumerate(myFile, 1):
            number_of_lines += 1
            ke = list(line)
            tab = 0
            nums = []
            for i in ke:
                if i == "\t":
                    tab += 1
                if tab == 2:
                    nums.append(i)
            s = int(''.join(nums))
            counter += s
        avg_years = round(counter / number_of_lines)
        return avg_years


def get_game(file_name, title):
    with open(file_name) as myFile:
        for num, line in enumerate(myFile, 1):
            ke = list(line)
            tab = 0
            nums = []
            for i in ke:
                if i == "\t":
                    tab += 1
                if tab == 0:
                    nums.append(i)
            s = ''.join(nums)
            if s == title:
                final_form = line.split("\t")
                return final_form  # numbers should be floats
