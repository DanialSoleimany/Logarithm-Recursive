def log_rec(argument, base):
    if (argument == 1):
        return 0
    else:
        return 1 + log_rec(argument/base, base) 
     
argument = int(input("argument: "))
base = int(input("base: "))

print("Exponent : {0}".format(log_rec(argument, base)))
