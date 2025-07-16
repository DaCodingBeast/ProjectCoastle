from math import sqrt
import math
import random
import matplotlib.pyplot as plt

class linearClassifyingTools():

    def __init__(self):
        pass

    def dot(a, b):
        return sum([a[x] * b[x] for x in range(len(a))])

    def sign(x):
        if x > 0:
            return 1
        else:
            return -1
        
    def multiplyVector(a,b):
        return [a[i] * b[i]  for i in range(len(a))]

    def multScalar(a, scalar):
        return [a[i] * scalar  for i in range(len(a))]
    
    def plusVector(a, b):
        return [a[i] +b[i]  for i in range(len(a))]
    
    def getNorm(theta):
        return sqrt(sum(x**2 for x in theta))
    
    def generateRandomData(dimensions,dataPoints = 150, MinMargin = 1.0, thetaRange=(-10,10)):
        artificialTheta = [random.random() for i in range(dimensions)]
        offset = random.randint(thetaRange[0],thetaRange[1])

        norm = linearClassifyingTools.getNorm(artificialTheta)

        data = []
        for i in range(dataPoints):

            while True:
                
                xs = [random.randint(thetaRange[0],thetaRange[1]) for x in range(dimensions)]
                margin = (linearClassifyingTools.dot(artificialTheta,xs) + offset) / norm

                if abs(margin) >= MinMargin:
                    classification = linearClassifyingTools.sign(margin)
                    data.append((xs,classification))
                    break

        return data
    

    def findLoss(theta,theta_zero,data):
        loss = 0
        for element in data:
            x,y = element
            
            result = linearClassifyingTools.dot(theta, x) + theta_zero
            if linearClassifyingTools.sign(result) != y:
                loss +=1
                # print("This element " + str(x) + "is not of the sign" + str(sign(result)))
                
            # print("This element " + str(x) + "is of the actual sign" + str(y))
            
        return loss
    
    def createTwoPointsOnLine(theta, theta_zero, thetaRange):
        x = thetaRange
        y = [ (-i*theta[0] - theta_zero)/theta[1] for i in x]
        return x,y
    
    def plot (data, theta,theta_zero, thetaRange):
        
        x1Data = [element[0][0] for element in data]
        x2Data = [element[0][1] for element in data]
        yData =  [element[1] for element in data]

        colors = []

        for i in yData:
            if i == 1:
                colors.append('blue')
            else:
                colors.append('red')

        # print(data)
        # print(x1Data)
        # print(x2Data)
        plt.scatter(x1Data, x2Data ,c = colors)

        x, y = linearClassifyingTools.createTwoPointsOnLine(theta, theta_zero, thetaRange)

        plt.plot(x,y)
        plt.show()

    def createColors(dimensionNum):
        colors = []
        for i in range(dimensionNum):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rgb = (r,g,b)
            colors.append(tuple([v / 255 for v in rgb]))
        return colors
    
    def plotKs(data,dimNums):

        colors = linearClassifyingTools.createColors(len(data[0][0]))
        colorcount = 0

        graphCounter = 0

        print(len(data))
        cols = 4
        rows = math.ceil(len(data)/cols)

        print("rows"+ str(rows))

        fig,axes = plt.subplots(rows,cols,figsize = (20, 5*rows))

        axes = axes.flatten()
        dimensionNumber = dimNums[0]
        
        start = True

        for dimenesion in data:

            axes[graphCounter].set_xlabel("Perceptron Runs")
            axes[graphCounter].set_ylabel("% Mistakes")

            axes[graphCounter].set_title(f"Dimension {dimensionNumber}")

            for graph in dimenesion:
                x =[]
                y=[]

                for i in range(0,len(graph),10):
                    x.append(graph[i][1])
                    y.append(graph[i][0])    
                    
                # print(colors[colorcount])
                print(axes[graphCounter])
                print(colors[colorcount])
                axes[graphCounter].plot(x,y, color = colors[colorcount])

                
                colorcount+= 1
            dimensionNumber += dimNums[2]
            graphCounter+=1
            colorcount= 0

            start = True

        plt.show()
    def plotK(data):

        x =[]
        y=[]
        for i in range(len(data)):
            if i %10 ==0 :
                x.append(data[i][1])
                y.append(data[i][0]) 
            # print(y[i])   
                    
        plt.plot(x,y, color = "blue")

        plt.show()
        return
