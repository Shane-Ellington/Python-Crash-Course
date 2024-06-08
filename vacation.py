# Prompt 7-10: make a poll of name and dream vacation
#start with empty list
responses = {}
# set flag
polling_active = True
while polling_active:
    name = input('What is your name?')
    response = input('Where would you like to go?')
# store in dictonary
    responses[name] = response
    repeat = input("Would anyone else like to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print('*****Poll Results*****')
for name, response in responses.items():
    print(f'{name} wants to visit {response}!')