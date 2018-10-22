def divide(A,B,u):
    cakePerPerson = (A/B)*u
    peopleToInvite = int((B/A)*u)
    print("There should be", peopleToInvite, "people invited")
    return peopleToInvite

print(divide(3,19,1))