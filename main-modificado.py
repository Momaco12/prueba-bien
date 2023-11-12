from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from respuesta import Respuesta
import joblib
modelo = joblib.load('../models/modelo9523.joblib')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('../templates/wizard.html')

if __name__ == '__main__':
    app.run(debug=True)

def calculate():
    # edad = 60
    # anemia = 0
    # diabetes = 1
    # eyeccion = 35
    # presion = 0
    # plaquetas = 263358.03
    # creatinina = 1.8
    # sexo = 1 
    # fuma = 1
    # tiempo = 186

    vd = Validator() # instancia del validador
    displayErr = False # si se debe desplegar o no un error en el rango

    try:
        edad = float(request.form['edad'])
        displayErr = vd.validate(30, 120, edad, displayErr)

        anemia = bool(request.form['anemia'])
        displayErr = diabetes = bool(request.form['diabetes'], displayErr)

        eyeccion = int(request.form['eyeccion'])
        displayErr = vd.validate(5, 90, eyeccion, displayErr)

        presion = bool(request.form['presion'])

        plaquetas = float(request.form['plaquetas'])
        displayErr = vd.validate(500, 1200000, plaquetas, displayErr)

        creatinina = float(request.form['creatinina'])
        displayErr = vd.validate(0.2, 15, creatinina, displayErr)

        sexo = bool(request.form['sexo'])

        fuma = bool(request.form['fuma'])

        tiempo = int(request.form['tiempo'])
        displayErr = vd.validate(2, 330, tiempo, displayErr)

        peso = int(request.form['peso']) # Agregar al html
        displayErr = vd.validate(30, 350, peso, displayErr)
    
    except ValueError:
        # Enviar al usuario a un html de error.
        return render_template('../error.html', result='Invalid input')
    
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



    

# edad = 90
# anemia = 1
# diabetes = 1
# eyeccion = 15
# presion = 1
# plaquetas = 327010
# creatinina = 1.0
# sexo = 1
# fuma = 1
# tiempo = 10
# try:
#     edad = float(request.form['edad'])
#     anemia = bool(request.form['anemia'])
#     diabetes = bool(request.form['diabetes'])
#     eyeccion = int(request.form['eyeccion'])
#     presion = bool(request.form['presion'])
#     plaquetas = float(request.form['plaquetas'])
#     creatinina = float(request.form['creatinina'])
#     sexo = bool(request.form['sexo'])
#     fuma = bool(request.form['fuma'])
#     tiempo = int(request.form['tiempo'])
# except ValueError:
#     Enviar al usuario a un html de error.
#     return render_template('red_calculator.html', result='Invalid input')
# datos = []
# datos.append([edad, anemia, diabetes, eyeccion, presion, plaquetas, creatinina, sexo, fuma, tiempo])
# datos = np.array(datos)

# Enviar los datos a analizar
# resultado = modelo.predict_proba(datos)
# print("Predicción: ",resultado)


# Desconozco!!!!!!!!

# app = Flask(_name_)

# @app.route('/')
# def index():
#     return render_template('wizard.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     if request.method == 'POST':
#         try:
#             num1 = float(request.form['num1'])
#             num2 = float(request.form['num2'])
#             operation = request.form['operation']

#             if operation == 'add':
#                 result = num1 + num2
#             elif operation == 'subtract':
#                 result = num1 - num2
#             elif operation == 'multiply':
#                 result = num1 * num2
#             elif operation == 'divide':
#                 result = num1 / num2
#             else:
#                 result = 'Invalid operation'

#             # Redirect to the result page with the calculated result
#             return redirect(url_for('show_result', result=result))

#         except ValueError:
#             return render_template('red_calculator.html', result='Invalid input')

# @app.route('/result/<result>')
# def show_result(result):
#     return render_template('result_page.html', result=result)

# if _name_ == '_main_':
#     app.run(debug=True)