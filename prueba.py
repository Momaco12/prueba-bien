from flask import Flask, render_template, request, redirect, url_for
from respuesta import Respuesta
from validator import Validator
import numpy as np
import joblib

modelo = joblib.load('./models/modelo9523.joblib')

datos = []
datos.append([60, 0, 1, 35, 0, 263358.03, 1.8, 1, 1, 186])
datos = np.array(datos)

#Enviar los datos a analizar
resultado = modelo.predict_proba(datos)
#Elegir el primer dato
res = resultado[0][0]

print(resultado)
print(res)