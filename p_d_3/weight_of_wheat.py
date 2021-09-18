# Weight of wheat for all squares in a chess board.
'''The game of chess is generally believed to have been invented in India in the sixth century for a ruling
king by one of his subjects. The king was supposedly very delighted with the game and asked the sub-
ject what he wanted in return. The subject, being clever, asked for one grain of wheat on the first
square, two grains of wheat on the second square, four grains of wheat on the third square, and so forth,
doubling the amount on each next square. The king thought that this was a modest reward for such an
invention. However, the total amount of wheat would have been more than 1,000 times the current
world production.'''
# The program is  calculates how much wheat this would be in pounds, using
#the fact that a grain of wheat weighs approximately 1/7,000 of a pound.

#There are totally 204 squares in a chess board.

no_of_squares = 204
no_of_grains = 0
i =1
for i in range(204):
    no_of_grains+=i**2

weight = no_of_grains*1/7000

print('The weight of wheat grains will be: ', weight, 'pounds\n')
