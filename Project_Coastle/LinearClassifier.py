import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, num_features):
        self.thetaZero = 0.0
        self.theta = np.zeros(num_features)
        print(self.theta)

    def fit(self, data, tauRuns):
        self.loss_history = []

        for i in range(tauRuns):
            countWrong = 0

            for point in data:
                x = np.array(point[0])
                y= point[1]
                # print(f"Point: {x}, Label: {y}")

                if y * (self.theta.dot(x) + self.thetaZero) <= 0:
                    self.theta = self.theta + (np.array(x) * y)

                    # Change thetaZero update
                    self.thetaZero += y
                    countWrong +=1

            iterationResults = {
                "percent_wrong": countWrong / len(data) * 100,
                "epoch": i,
                "theta": self.theta,
                "thetaZero": self.thetaZero
            }
            self.loss_history.append(iterationResults)

            if countWrong ==0:
                for x in range(5):
                    self.loss_history.append({"percent_wrong": 0, "epoch": i+x+1, "theta": self.theta.tolist(), "thetaZero": self.thetaZero})
                break

        print(f"Final theta: {self.theta}, thetaZero: {self.thetaZero}")
        
    def predict(self, x):
        x = np.array(x)
        result = self.theta.dot(x) + self.thetaZero
        if result > 0:
            return 1
        else:
            return -1
    
    def plotConvergence(self, dataSpread=5):

        epochs = [entry["epoch"] for entry in self.loss_history[::dataSpread]]
        percent_wrong = [entry["percent_wrong"] for entry in self.loss_history[::dataSpread]]
        percent_wrong = [entry["percent_wrong"] for entry in self.loss_history[::dataSpread]]

        plt.plot(epochs, percent_wrong, marker='o')
        plt.xlabel('Epochs')
        plt.ylabel('Percent Wrong (%)')
        plt.title('Perceptron Convergence')
        plt.ylim(0, 100)
        plt.grid()
        plt.show()