def fact(n):
    if(n==0 or n==1): # base condition which doesn’t call the function any further
        return 1
    return n * fact(n-1) # function calling itself

print(fact(4))