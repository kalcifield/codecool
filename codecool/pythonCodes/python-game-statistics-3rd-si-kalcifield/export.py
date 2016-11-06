# Export functions
import reports

file = open("export.txt", "w")

first = str(reports.count_games("game_stat.txt")) + "\n"

second = str(reports.decide("game_stat.txt", "2000")) + "\n"

#third = str(reports.get_latest("game_stat.txt")) + "\n"

fourth = str(reports.count_by_genre("game_stat.txt", "RPG")) + "\n"

fifth = str(reports.get_line_number_by_title("game_stat.txt", "Counter-Strike: Condition Zero"))

file.write(first)
file.write(second)
#file.write(third)
file.write(fourth)
file.write(fifth)