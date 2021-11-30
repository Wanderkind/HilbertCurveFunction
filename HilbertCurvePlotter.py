
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

        L = [[[0, 0]]]
        for i in range(n):
            
            l = []
            
            for j in range(4**i):
                l.append([L[i][j][1], L[i][j][0]])
                
            for j in range(4**i):     
                l.append([L[i][j][0], L[i][j][1] + 2**i])
                
            for j in range(4**i):
                l.append([L[i][j][0] + 2**i, L[i][j][1] + 2**i])
                
            for j in range(4**i):
                l.append([2**(i + 1) - 1 - L[i][j][1], 2**i - 1 - L[i][j][0]])

            L.append(l)

        return L[i + 1][pointround]
    
    print(PHC(n, point))
    cx = PHC(n, point)[0]/(2**n - 1)
    cy = PHC(n, point)[1]/(2**n - 1)
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
