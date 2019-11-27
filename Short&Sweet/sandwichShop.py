import pyinputplus as pyip

while True:
    cost = 0
    consent = pyip.inputYesNo(prompt='Would you like a sandwhich? ')
    if consent == 'yes':
        print('Alright, let\'s get started on the bread')
        bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
        cost += 1.50
        protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
        cost += 3.50
        cheeseDesire = pyip.inputYesNo(prompt='Would you like cheese on that? ')
        if cheeseDesire == 'yes':
            cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
            cost += 1.25
        else:
            pass
        extra = pyip.inputYesNo(prompt='Would you like mayo, mustard, lettuce or tomato? ')
        if extra == 'yes':
            cost += 1.15
        else:
            pass
        print(f'The total cost of this sandwich is ${cost:.2f}.')
        anotherSandwich = pyip.inputYesNo(prompt='Would you like to make another sandwich? ')
        if anotherSandwich == 'yes':
            continue
        else:
            break
    else:
        print('No sandwich for you!')
        break