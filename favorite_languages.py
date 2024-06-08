#6-6 practice prompt
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}, You chose {language.title()}!")
    
programmers = ['jen', 'sarah', 'edward', 'phil', 'john', 'shane']
for programmer in programmers:
    if programmer in favorite_languages.keys():
        print(f"Thanks for participating {programmer.title()}.")
        
    else:
        print(f"{programmer.title()}, you need to complete the poll.")    
