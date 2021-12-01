
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
    a = pointround//(4**(n - 1 - i))
    pointround = pointround%(4**(n - 1 - i))
    L.append([a, pointround])

N = [[0, 0]]
for i in range(n):
    if L[n - 1 - i][0] == 0:
        N.append([-1/4 + N[i][1]/2, -1/4 + N[i][0]/2])
    
    elif L[n - 1 - i][0] == 1:
        N.append([-1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
    
    elif L[n - 1 - i][0] == 2:
        N.append([1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
    
    else:
        N.append([1/4 - N[i][1]/2, -1/4 - N[i][0]/2])

print([round(1/2 + N[n][0], 8), round(1/2 + N[n][1], 8)])
