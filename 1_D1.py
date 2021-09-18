# This is a program to determine the no of years required to find the shortest
# possible routes to visit the given number of cities by using brute-force method.
import math

cities = int(input("Enter the number of cities to be visited by a salesman: "))
no_of_routes = math.factorial(cities)    # this gives the total number of possible routes.
# Assuming computer can compute the length of one million routes per second,
# 1 sec > 1000000 then the number of seconds for 'no_of_routes' number of calculations

seconds = no_of_routes//1000000 # Number of seconds required to complete bruteforce.
days = seconds//86400           # Number of days required to complete bruteforce.
no_of_years = round(days/365) # Number of years required.

print(" About",no_of_years, "years are required to solve this problem by brute_force approach")
print(" About",days, "days are required to solve this problem by brute_force approach")


