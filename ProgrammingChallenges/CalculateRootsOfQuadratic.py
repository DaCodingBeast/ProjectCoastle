import math



def calcdiscriminat(a, b, c):
    return b**2 - 4*a*c



def getRoots(a,b,c):

    discriminant = calcdiscriminat(a,b,c)
    
    if discriminant <0:
        return
    elif discriminant>0:
        return (-b + math.sqrt(discriminant))/(2*a), (-b- math.sqrt(discriminant))/(2*a)
    else:
        return -b/(2*a)


print(getRoots(1,0,0))
print(getRoots(1,0,-1))
print(getRoots(1,0,1))
print(getRoots(1,1,-1))
