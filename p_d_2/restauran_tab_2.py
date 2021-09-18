# Restaurant Tab calculation
# This program calculates the restaurant tab with a gift certificate.

# Initialization.
#get the tax rate.
tax = float(input('Enter the rate of tax of restaurant: '))

#Program greet
print('This program calculates the restaurant tab calculation for a couple with')
print('a gift certificate, with a restaurant tax of', tax*100,'%\n')

#get amount on gift certificate
amount = float(input('Enter the amount on the gift certifcate: '))

# cost of ordered items
print('Enter the ordered items for the person 1')

appetizer_per1 = float(input('Appetizier: '))
entree_per1 = float(input('Entree: '))
drinks_per1 = float(input('Drinks: '))
dessert_per1 = float(input('Dessert: '))

print('Enter the ordered items for the person 2')

appetizer_per2 = float(input('Appetizier: '))
entree_per2 = float(input('Entree: '))
drinks_per2 = float(input('Drinks: '))
dessert_per2 = float(input('Dessert: '))

# total items' cost
amt_person1 = appetizer_per1 + entree_per1 + drinks_per1 + dessert_per1
amt_person2 = appetizer_per2 + entree_per2 + drinks_per2 + dessert_per2

# compute tab with tax
total_cost = amt_person1 + amt_person2
total_drinks = drinks_per1 + drinks_per2
percent_cost_drinks = (total_drinks/total_cost)*100
total_desserts = dessert_per1 + dessert_per2
percent_cost_desserts = (total_desserts/total_cost)*100
tab = total_cost + total_cost*tax

#Display Percent of total cost the drinks and desserts comprise.

print('\nDrinks:',total_drinks,'\n','Desserts:',total_desserts,'\n')
print('\nPercent of total cost the drinks comprise: ',format(percent_cost_drinks,'.2f'),'%\n',
    'Percent of total cost the desserts comprise:',format(percent_cost_desserts,'.2f'),'%\n')

#Display amount owe
print('\nOrdered items: $', format(total_cost, '.2f'))
print('Restaurant tax: $', format(total_cost*tax , '0.2f' ))
print('Tab: $', format(tab - amount, '.2f'))
print('(negative amount indicates the unused amount in the gift certificate)')