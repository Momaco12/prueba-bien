from random import random
class Neurona():
    def __init__(self, pesos, u = 0.5, alfa = 0.2):
        self.u = u
        self.alfa = alfa
        self.w = []
        for i in range(pesos):
            self.w.append(random())
    
    def predict(self, instancia):
        sumatoria = 0
        #print(self.w)
        for i in range(len(self.w)):
            sumatoria = sumatoria + self.w[i]*instancia[i]
        sumatoria = sumatoria - self.u
        print("sumatoria: ", sumatoria)
        if sumatoria > 0:
            sumatoria = 1
        else: 
            sumatoria = 0
        return sumatoria  
    
    def train(self, instancia, target):
        pred = self.predict(instancia)
        for k in range(len(self.w)):
            self.w[k] = self.w[k] + self.alfa*(target - pred)*instancia[k]


