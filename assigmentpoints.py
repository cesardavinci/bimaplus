n = int(input("Input number of points: "))
# Create empty lists
x = []
y = []

# input coordinates
for i in range(0, n):
    inputx = float(input("Please Input x: "))
    x.append(inputx)
    inputy = float(input("Please Input y: "))
    y.append(inputy)


# Print coordinates
print("Coordinate Data")
print("Point", "X", "Y")
print("------------")
for i in range(0, n):
    print(i+1, ":", x[i], y[i])

# Create empty list for the individual areas
lax = []
for i in range(0, n):
    ax = (x[i]+x[i-1]) * (y[i]-y[i-1])
    lax.append(ax)
# print lax areas from list and divide in 2
tax = 0.5*sum(lax)

lsx = []
for i in range(0, n):
    sx = (x[i]-x[i-1]) * (y[i]**2+y[i]*y[i-1]+y[i-1]**2)
    lsx.append(sx)

# print lsx from list and divide by 2
tax = 0.5*sum(lax)
tsx = -1/6*sum(lsx)

lsy = []
for i in range(0, n):
    sy = (y[i]-y[i-1]) * (x[i]**2+x[i]*x[i-1]+x[i-1]**2)
    lsy.append(sy)
# print lsy

lix = []
for i in range(0, n):
    ix = (x[i]-x[i-1]) * (y[i]**3+y[i]**2*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    lix.append(ix)
# print lix

liy = []
for i in range(0, n):
    iy = (y[i]-y[i-1]) * (x[i]**3+x[i]**2*(x[i-1])+x[i]*x[i-1]**2+x[i-1]**3)
    liy.append(iy)
# print liy

lixy = []
for i in range(0, n):
    ixy = (y[i]-y[i-1]) * (y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)) + \
        y[i-1]*(3*x[i]**2+2*x[i]*x[i-1]+x[i]**2)
    lixy.append(ixy)
# print lixy
# areas list and divide by 2
tax = 0.5*sum(lax)
tsx = -1/6*sum(lsx)
tsy = 1/6*sum(lsy)
tix = -1/12*sum(lix)
tiy = 1/12*sum(liy)
tixy = -1/24*sum(lixy)
xt = tsy/tax
yt = tsx/tax
ixt = tix - yt**2*tax
iyt = tiy - xt**2*tax
ixyt = tixy + xt*yt*tax

# Print outputs
print("The outputs are:")
print("Ax= ", "%.2f" % (tax))
print("Sx=", "%.2f" % tsx)
print("Sy=", "%.2f" % tsy)
print("Ix=", "%.2f" % tix)
print("Iy=", "%.2f" % tiy)
print("Ixy=", "%.2f" % tixy)
print("xt=", "%.2f" % xt)
print("yt=", "%.2f" % yt)
print("Ixt=", "%.2f" % ixt)
print("Iyt=", "%.2f" % iyt)
print("Ixyt=", "%.2f" % ixyt)