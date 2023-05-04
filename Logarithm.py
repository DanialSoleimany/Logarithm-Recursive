def log_rec(x, y):
    if (x == 1):
        return 0
    else:
        return 1 + log_rec(x/y, y) 
     
x = int(input("value: "))
y = int(input("base: "))

print(log_rec(x, y))