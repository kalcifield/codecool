def isFloat(string):
    try:
        float(string)
        return True
    except:


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
                print(final_form)


get_game("game_stat.txt", "Counter-Strike")