
import matplotlib.pyplot as plt

while True:
    point = float(input('Float between 0 and 1 : '))
    
    if 0 <= point <= 1:
        break
    
    else:
        point = float(input('Float between 0 and 1 : '))
        continue

px = []
py = []
for k in range(int(1/point) + 1):

    pointround = round((4**50 - 1)*k*point)

    L = []
    for i in range(50):
        L.append(pointround//(4**(49 - i)))
        pointround = pointround%(4**(49 - i))

    N = [[0, 0]]
    for i in range(50):
        if L[49 - i] == 0:
            N.append([-1/4 + N[i][1]/2, -1/4 + N[i][0]/2])
        
        elif L[49 - i] == 1:
            N.append([-1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
        
        elif L[49 - i] == 2:
            N.append([1/4 + N[i][0]/2, 1/4 + N[i][1]/2])
        
        else:
            N.append([1/4 - N[i][1]/2, -1/4 - N[i][0]/2])

    cx = round(1/2 + N[50][0], 7)
    cy = round(1/2 + N[50][1], 7)
    px.append(cx)
    py.append(cy)

if int(1/point)*point == 1.0:
    
    del py[int(1/point)]
    py.append(0.0)

for k in range(int(1/point) + 1):
    print(k*point, ':', [px[k], py[k]])

plt.plot(px, py, '.r-')
plt.title('Coordinate Convergence')

plt.show()