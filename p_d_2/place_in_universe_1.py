# Your place in the universe.

# This program will determine the approximate number of atoms that a
# person consists of and the percent of universe that they comprise.

# Initialisation
num_of_atoms_universe = 10e80
weight_avg_person = 70 # in Kg
num_atoms_avg_person = 7e27

#Program greeting
print("This program will determine your place in the universe.")

# prompt for user weight
weight_kg = int(input('Enter your weight in Kg: '))

# convert lbs to kg
#weight_kg = 2.2 * weight_lbs

# determine amount of atoms in person
num_atoms = (weight_kg/weight_avg_person)*num_atoms_avg_person
percent_of_universe = (num_atoms / num_of_atoms_universe)*100

#display output
print('You contain approximately ', format(num_atoms, '.2e'), 'atoms')
print('Hence, you comprise', format(percent_of_universe, '.2e'),
        '% of the universe.')
        