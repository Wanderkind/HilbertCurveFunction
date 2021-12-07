
n = int(input('PHC order : '))

while True:
    point = float(input('Float between 0 and 1 : '))
    
    if 0 <= point <= 1:
        break
    
    else:
        point = float(input('Float between 0 and 1 : '))
        continue

pointround = round((4**n - 1)*point)

L = []
for i in range(n):
    L.append(pointround//(4**(n - 1 - i)))
    pointround = pointround%(4**(n - 1 - i))

N = [[0, 0]]
for i in range(n):
    if L[n - 1 - i] == 0:
        N.append([-1/4 + N[i][1]/2, -1/4 + N[i][0]/2])
    
    elif L[n - 1 - i] == 1:
        N.append([-1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
    
    elif L[n - 1 - i] == 2:
        N.append([1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
    
    else:
        N.append([1/4 - N[i][1]/2, -1/4 - N[i][0]/2])

cx = round(1/2 + N[n][0], 7)
cy = round(1/2 + N[n][1], 7)

if point == 1 and cy == 0.5:
    cy = 0.0

print([cx, cy])
