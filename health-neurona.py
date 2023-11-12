import numpy as np
import pandas as pd
from  sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from random import random
from neurona import Neurona
#Leer Dataset
data = pd.read_csv("../data/heartFailure2.csv", header=0)
#dividir dataset
target = data.iloc[:,10].to_numpy()
source = data.iloc[:,0:10].to_numpy()
lista = []
for i in range(target.shape[0]):
    if target[i] == 0:
        lista.append([0])
    else:
        lista.append([1])
#Crear indices
lista = np.asarray(lista)
indices_s = np.arange(target.shape[0])
#barajar indicesrr
np.random.shuffle(indices_s)
#dividir en train y test
Y_train = lista[indices_s[0:199]]
X_train = source[indices_s[0:199]]
Y_test = lista[indices_s[199:]]
X_test = source[indices_s[199:]]
#definimos pesos

neurona1 = Neurona(10, u = 0.5, alfa = 0.5)
for i in range(1):  #veces que se recorre conjunto de entenamiento
    for j in range(X_train.shape[0]): #este es el tamaño del conjunto de entenamiento
        neurona1.train(X_train[j], Y_train[j][0])

y_pred = []
for i in range(X_test.shape[0]):
    resp1 = neurona1.predict(X_test[i])
    print("resp1",resp1)
    y_pred.append([resp1])

#imprimir metricas
print("Y_test: ", Y_test)
print("y_pred: ", y_pred)
print(f1_score(Y_test, y_pred, average='binary'))
y_pred = np.asarray(y_pred)
print(confusion_matrix(Y_test[:,0], y_pred[:,0]))