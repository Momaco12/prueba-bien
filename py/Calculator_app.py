from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('wizard.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
            else:
                result = 'Invalid operation'

            return render_template('multi_tab_calculator.html', result=result)

        except ValueError:
            return render_template('multi_tab_calculator.html', result='Invalid input')

if __name__ == '__main__':
    app.run(debug=True)