from flask import Flask, render_template, request, redirect, url_for
from respuesta import Respuesta
from validator import Validator
import numpy as np
import joblib

app = Flask(__name__)

modelo = joblib.load('./models/modelo9523.joblib')

@app.route('/')
def index():
    return render_template('./templates/wizard.html')

if __name__ == '__main__':
    app.run(debug=True)

def calculate():
    try:
        edad = float(request.form['edad'])
        anemia = bool(request.form['anemia'])
        diabetes = bool(request.form['diabetes'])
        eyeccion = int(request.form['eyeccion'])
        presion = bool(request.form['presion'])
        plaquetas = float(request.form['plaquetas'])
        creatinina = float(request.form['creatinina'])
        sexo = bool(request.form['sexo'])
        fuma = bool(request.form['fuma'])
        tiempo = int(request.form['tiempo'])
        peso = int(request.form['peso']) # Agregar al html
    except ValueError:
        # Enviar al usuario a un html de error.
        return render_template('./templates/error.html', result='Invalid input')
    
    #validación de error


    #Creación del arreglo a enviar al árbol
    datos = []
    datos.append([edad, anemia, diabetes, eyeccion, presion, plaquetas, creatinina, sexo, fuma, tiempo])
    datos = np.array(datos)
    
    #Enviar los datos a analizar
    resultado = modelo.predict_proba(datos)
    #Elegir el primer dato
    res = resultado[0]

    #Creacion del output a mostar
    stringFinal = Respuesta(res, sexo, edad, peso, fuma, presion, diabetes)

    #Enviar el string al HTML
    return redirect(url_for('show_result', respuesta=stringFinal))

@app.route('/page')
def page():
    return render_template('wizard.html', texto='texto')

