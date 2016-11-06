def decide(file_name, year):
    givenYear = str(year)
    if givenYear in open(file_name).read():
        return True
    else:
        return False

decide("game_stat.txt", 2000)