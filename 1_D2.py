# This is a program to determine the number of years required to
# play all possible occurences of a chess game if every person around the
# world played one chess game per day.
# Population of world is assumed to be 7 billion
no_of_people = 7000000000
# Total number of possibilities of chess game is defined below
total_no_of_possibilities = 10**120
no_of_games_a_day = 7000000000
no_of_games_a_year = 7000000000*365     # Number of games that can be played per year
no_of_years = total_no_of_possibilities//no_of_games_a_year

print("It would take about",format(no_of_years, ','),"years to play all possible chess games if everyone in the world played one game a day.")
print(len(str(no_of_years)))
