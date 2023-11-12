import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

#Acceder a la base de datos
data = pd.read_csv("/data/heartFailure2.csv", header=0)
target = data.iloc[:,10].to_numpy()
source = data.iloc[:,0:10].to_numpy()
indices_s = np.arange(target.shape[0])

#Mesclar los datos
np.random.shuffle(indices_s)

#Dividir datos para entrenar y testear
Y_train = target[indices_s[0:249]]
X_train = source[indices_s[0:249]]
Y_test = target[indices_s[249:]]
X_test = source[indices_s[249:]]

#Entretar con gini
randomF = RandomForestClassifier(n_estimators = 100, criterion = 'gini')
randomF.fit(X_train, Y_train)
#testear
y_pred = randomF.predict(X_test)

#Resultados
print(f1_score(Y_test, y_pred,average='macro'))
print(confusion_matrix(Y_test, y_pred))

#Entretar con entropia
randomFo = RandomForestClassifier(n_estimators = 100, criterion = 'entropy')
randomFo.fit(X_train, Y_train)
#testear
y_predict = randomFo.predict(X_test)
#Resultados
print(f1_score(Y_test, y_predict,average='macro'))
print(confusion_matrix(Y_test, y_predict))

#PRUEBAS
# print("Prueba: ",randomF.predict_proba(X_test))
# print("Prueba: ",randomFo.predict_proba(X_test))

#Guardar el documento
joblib.dump(randomF, 'modeloA.joblib')
joblib.dump(randomFo, 'modeloB.joblib')