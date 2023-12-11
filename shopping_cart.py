# Build a shopping cart program with the following capabilities:
# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.


# My steps:
# Create an empty dict
# Create a dict with predefined items and prices
# Create a function that will check the input (if statements?) and execute the related code. i.e. input = add | add item selected to the empty dict.
# 

# if statement to check what option they put in the input
# if: add - add an item from predefined dict to empty dict
# if: remove - remove item from dict 
# if: clear - clear dict
# if: quit - end and print out list



# Brian's "starter code" he showed in class:
# def store():
#     while True:
#         to_do = input('What would you like to do?')
#         if to_do == 'quit':
#             break
            
# store()


cart = {}
options = {
    'apples': .50,
    'chocolate': 2.99,
    'bread': 1.99,
    'milk': 3.99
}

def shop():
    while True:
        
        to_do = input('What would you like to do? (add/remove/clear/quit): ')
        if to_do == 'add':
            print('Items and Prices:')
            for item, price in zip(options.keys(), options.values()):
                print(f'{item}: ${price:.2f}')
        else:
            break
        
        
        
        # elif to_do == 'remove':
        #     break
        # elif to_do == 'clear':
        #     break
        # elif to_do == 'quit':
        #     break

