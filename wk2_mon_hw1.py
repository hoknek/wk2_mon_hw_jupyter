print('\nWelcome to the calculator!')
while True:
    x = input('Enter a number: ')
    y = input('Enter command "plus", "minus", "multiply", "divide", "square", or "square-root": ')
    if y == "plus" or y == "minus" or y == "multiply" or  y == "divide":
        z = input('Enter another number for "plus", "minus", "multiply", or "divide": ')
        if y == 'plus':
            print("\nYour answer: " + str(float(x) + float(z)))
        if y == 'minus':
            print("\nYour answer: " + str(float(x) - float(z)))
        if y == 'multiply':
            print("\nYour answer: " + str(float(x) * float(z)))
        if y == 'divide':
            print("\nYour answer: " + str(float(x) / float(z)))
    else:
        if y == 'square':
            print("\nYour answer: " + str(float(x)**(2)))
        if y == 'square-root':
            print("\nYour answer: " + str(float(x)**(float(.5))))
    z = input('Press "enter" to continue. Press "q" to quit: ')
    if z == "q":
        break
    



