'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
Using the information given below, determine the number of apples and oranges that land on Sam's house.
The red region denotes the house, where s is the start point, and t is the endpoint. 
The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
When a fruit falls from its tree, it lands  d units of distance from its tree of origin along the x-axis. 
*A negative value of  d means the fruit fell d units to the tree's left, 
and a positive value of d means it falls d units to the tree's right. *
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculate the positions where apples and oranges land
    apple_positions = [a + d for d in apples]
    orange_positions = [b + d for d in oranges]

    # Count the number of apples and oranges that land within the house boundaries
    apples_in_house = sum(1 for pos in apple_positions if s <= pos <= t)
    oranges_in_house = sum(1 for pos in orange_positions if s <= pos <= t)

    # Print the results
    print(apples_in_house)
    print(oranges_in_house)

# Example usage:
s_house = 7
t_house = 11
a_apple_tree = 5
b_orange_tree = 15
apples_fallen = [-2, 2, 1]
oranges_fallen = [5, -6]
countApplesAndOranges(s_house, t_house, a_apple_tree, b_orange_tree, apples_fallen, oranges_fallen)
