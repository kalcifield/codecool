# Export functions
import reports

file = open("export.txt", "w")

# first =

second = str(reports.sum_sold("game_stat.txt")) + "\n"

third = str(reports.get_selling_avg("game_stat.txt")) + "\n"

# fourth =

fifth = str(reports.get_date_avg("game_stat.txt")) + "\n"

sixth = str(reports.get_game("game_stat.txt", "Counter-Strike"))

# file.write(first)
file.write(second)
file.write(third)
# file.write(fourth)
file.write(fifth)
file.write(sixth)
