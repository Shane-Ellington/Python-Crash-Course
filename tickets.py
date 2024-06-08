active = True
while True:
    age = input('What is the age of the guest? (Enter "quit" to finish):')

    if age.lower() == 'quit':
        active = False
    else:
        try:
            age = int(age)
            if age > 12:
                print('The ticket is $15.')
            elif age > 3:
                print('The ticket is $10.')
            elif age > 0:
                print('The ticket is FREE!')
            else:
                print('Invalid age.')
        except ValueError:
            print("Please enter a valid age or 'quit' to exit.")
                


