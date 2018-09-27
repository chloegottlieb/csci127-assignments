#Chloe Gottlieb (done as HW assignment due to holiday)
def fizzbuzz(max_value):
    i = 1
    while i != max_value + 1:
        if i % 5 == 0 and i % 3 == 0:
            fizzBuzz = print('fizzBuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i = i+1
print(fizzbuzz(100))
