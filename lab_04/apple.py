def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    for i in apples:
        if (a + i) in range (s, t + 1):
            apple_count = apple_count + 1
            
    for i in oranges:
        if (b - 1) in range (s, t + 1):
            orange_count = orange_count + 1
    
    return apple_count + orange_count

print(countApplesAndOranges(12, 24, 3, 13, [-4, 3, 2], [8, -5, 16]))