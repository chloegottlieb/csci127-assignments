fillName = input("What is your name?\n")

def greeter(name):
    """
    greeter('steve') --> 'Hello Steve!')
    greeter('dana') --> 'Hello Dana!')
    """
    if name == 'dana':
        print('hello dana')
    elif name == 'steve':
        print('hello steve')
    else:
        print('you are not a greeter. goodbye.')
        
greeter(fillName)