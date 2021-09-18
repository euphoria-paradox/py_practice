# The SETI Program

# Drake equation developed in 1960 to estimate the number of
# estraterrestrial civilizations , N, may exist in our galaxy
# at any given time , it is given by
#
# N = R * p * n * f * i * c * L
#
# where,
#   R - estimated rate of star creation in our galaxy.
#   p - estimated percent of stars that have planets
#   n - estimated average number of planets that can potentially support life
#       in for each star with planets
#   f - estimated percent of those planets that can actually go on to develop
#       life.
#   i - estimated percent of those planets go on to develop intelligent life.
#   c - estimated percent of those that are willing and able to communicate
#   L - estimated expected lifetime for such civilization.
#
# Given the value of R , 7 per year, the user is prompted to enter rest 6 factors,
# the result will be displayed by the solution of the Drake equation.

# Display welcome of program.
print(format("Welcome to the SETI program", "-^10"))
print('The program will allow you to enter specific values related to')
print('the likelihood of finding intelligent life in our galaxy. All')
print('percentages should be entered as integer values i.e, 40 and not 0.4')
print()

# get user input
p = int(input('What percent of stars do you think have planets? '))
n = int(input('How many planets per star do you think can support life? '))
f = int(input('What percentage do you think can develop life? '))
i = int(input('What percentage of those do you think have intelligent life? '))
c = int(input('What percentage of those do you think can communicate with us? '))
L = int(input('Number of years you think the civilization lasts? '))

# calculate result
num_of_detectable_civilisation = 7 * (p/100) * (n/100) * (f/100) * (i/100) * (c/100) * L

#Display result
print('\n')
print('Based on the obtained input values....')
print('there are estimated ', round(num_of_detectable_civilisation),
        'potentially detectable civilizations in our galaxy')

