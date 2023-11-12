from flask import Flask, render_template, request, redirect, url_for
from respuesta import Respuesta
from validator import Validator
import numpy as np
import joblib

app = Flask(__name__)

modelo = joblib.load('./models/modelo9523.joblib')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit_answers', methods=['POST'])
def handle_button():
    if request.method == 'POST':
        # try:
        edad = float(request.form['edad'])
        anemia = str(request.form['anemia'])
        anemia = anemia.upper()
        diabetes = str(request.form['diabetes'])
        diabetes = diabetes.upper()
        eyeccion = int(request.form['eyeccion'])
        presion = str(request.form['presion'])
        presion = presion.upper()
        plaquetas = float(request.form['plaquetas'])
        creatinina = float(request.form['creatinina'])
        sexo = str(request.form['sexo'])
        sexo = sexo.upper()
        cigarrillos = int(request.form['fuma'])
        tiempo = int(request.form['tiempo'])
        peso = int(request.form['peso'])
        
        if(anemia == "SI" or anemia == "Sí"):
            anemia = 1
        else:
            anemia = 0
        if(diabetes == "SI" or diabetes == "Sí"):
            diabetes = 1
        else:
            diabetes = 0
        if(presion == "SI" or presion == "Sí"):
            presion = 1
        else:
            presion = 0
        if(sexo == "F" or sexo == "FEMENINO" or sexo == "MUJER"):
            sexo = 1
        else:
            sexo = 0
        if(cigarrillos == 0):
            fuma = False
        else:
            fuma = True

        #Creación del arreglo a enviar al árbol
        datos = []
        datos.append([edad, anemia, diabetes, eyeccion, presion, plaquetas, creatinina, sexo, fuma, tiempo])
        datos = np.array(datos)
        
        #Enviar los datos a analizar
        resultado = modelo.predict_proba(datos)
        #Elegir el primer dato
        res = resultado[0]
        print(res)
        
        respuesta_instance = Respuesta(res, sexo, edad, peso, fuma, diabetes, diabetes)

        respuesta_text = respuesta_instance.respuesta

        #Creacion del output a mostar
        # stringFinal = Respuesta(res, sexo, edad, peso, cigarrillos, presion, diabetes)
        # print(stringFinal)
        # stringFinal = "holis si jala el boton"
        #Enviar el string al HTML
        return render_template('form.html', submitted_answers = respuesta_text)
        

if __name__ == '__main__':
    app.run(debug=True)