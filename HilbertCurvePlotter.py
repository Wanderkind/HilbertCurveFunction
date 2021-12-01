
import matplotlib.pyplot as plt

N = int(input('Max PHC order : '))

while True:
    point = float(input('Float between 0 and 1 : '))
    
    if 0 <= point <= 1:
        break
    
    else:
        point = float(input('Float between 0 and 1 : '))
        continue

px = []
py = []
for s in range(N):
    
    n = s + 1
    
    def PHC(n, point):

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

        return [round(1/2 + N[n][0], 8), round(1/2 + N[n][1], 8)]
    
    H = PHC(n, point)
    cx = H[0]
    cy = H[1]
    print([cx, cy])
    px.append(cx)
    py.append(cy)

plt.subplot(2, 1, 1)
plt.plot(px, 'r-')
plt.title('cx')

plt.subplot(2, 1, 2)
plt.plot(py, 'b-')
plt.title('cy')

plt.show()

plt.plot(px, py, '.g-')
plt.title('Coordinate Convergence')

plt.show()
