from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    if request.method == 'POST':
        # Retrieve answers from the form
        edad = request.form['edad']
        diabetes = request.form['diabetes']
        anemia = request.form['anemia']
        eyeccion = request.form['eyeccion']
        presion = request.form['presion']
        creatinina = request.form['creatinina']
        plaquetas = request.form['plaquetas']
        sexo = request.form['sexo']
        fuma = request.form['fuma']
        tiempo = request.form['tiempo']
        
        # Repeat for answers 3 to 11
        # Add more lines to retrieve each answer individually

        # Perform any processing needed with the answers
        # For now, just render the submitted answers back to the user
        return render_template('form.html', submitted_answers=(edad, diabetes, anemia, eyeccion, presion, plaquetas, creatinina, sexo, fuma, tiempo))  # Include each answer individually in the tuple

if __name__ == '__main__':
    app.run(debug=True)