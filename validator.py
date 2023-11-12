class Validator:
    # Func: constructor Validator
    def __init__(self, params):
        # correr validación 
        self.validateParams(params) # params es un renglón de tabla pandas

    # Func: validación de parámetros
    def validateParams(self, params):
        # asignar variables
        age = params['age']
        ejection_fraction = params['ejection_fraction']
        platelets = params['platelets']
        serum_creatinine = params['serum_creatinine']
        time = params['time']
        weight = params['weight']

        # verificación de rangos
        if age < 30 or age > 120:
            print('Not in range')
        if ejection_fraction < 5 or ejection_fraction > 90:
            print('Not in range')
        if platelets < 500 or platelets > 1200000:
            print('Not in range')
        if serum_creatinine < 0.2 or serum_creatinine > 15:
            print('Not in range')
        if time < 2 or time < 330:
            print('Not in range')
        if time < 30 or time > 350:
            print('Not in range')