#Chloe Gottlieb and Chana Abramov
def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = (n / 2)
            steps = steps + 1
        else:
            n = (3 * n + 1)
            steps = steps + 1
    stepsFinal = "it took ", steps, "steps"
    stepsFinalFinal = print(stepsFinal)
    return n
    return stepsFinalFinal
print(collatz(93401345))
