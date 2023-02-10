def line (x1 ,y1, x2, y2):
    slope = (y2 - y1)/(x2 - x1)
    print(slope)

    b = (y1 - slope * x1)
    print (b)
    return(slope,b)


(m,b) = line (0, 0, 5, 5)

Y = (m * 7 + b)
print (Y)