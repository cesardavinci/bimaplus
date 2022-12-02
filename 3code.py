n = int(input ("number of points?"))

x = []
y = []

# ask for coordinates
for i in range (0,n):
    inputx = int(input("enter x: "))
    x.append(inputx)
    inputx = int(input("enter y: "))
    y.append(inputx)

# print coordinates
for i in range (0, n):
    print("Point", i+1, ":", x[i], y[i])
    
# empty list of individual areas
lax= []
for i in range(0,n-1):
    ax = (x[i+1]+x[i]) * (y[i], y[i])
    lax.append(ax)

# sum all areas form list and divide them by 2
tax = 0.5*sum(lax)

# output results
print(n) 
print(x)
print(y)
print("Area: ", tax) 



