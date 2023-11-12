class Respuesta():

    def __init__(self, res, sexo, edad, peso, fuma, hipertenso, diabetes, respuesta=""):

        if(res):
            if(0 <= res <=10):
                answer = "Normal:\nSi no estás sintiendo ningún dolor o molestia en el pecho, y los resultados de las pruebas médicas salen bien, estamos en un nivel normal. No hay señales de un ataque cardíaco."
                respuesta =+ answer
            elif(10 < res <=25):
                answer = "Medio:\nSi tienes algún dolor en el pecho, podríamos estar en una etapa intermedia. Necesitamos más evaluaciones para entender mejor lo que está sucediendo."
                respuesta =+ answer
            elif(25 < res <=50):
                answer = "Alto:\nAquí vemos señales de daño al corazón en las pruebas. Los síntomas podrían ser más notorios y es importante actuar rápidamente."
                respuesta =+ answer
            elif(50 < res <=70):
                answer = "Preocupante:\nAhora estamos en un punto donde el daño al corazón es más significativo. Los síntomas son graves, y necesitamos tomar medidas urgentes para abordar la situación.\n"
                respuesta =+ answer
            elif(70 < res <=100):
                answer = "Emergencia:\nEsto es una emergencia. Hay evidencia clara de daño al corazón y los síntomas son graves. Llama al 911 o al número de emergencias de inmediato. Necesitamos ayuda médica urgente para brindarte la atención necesaria y salvarte la vida.\n"
                respuesta =+ answer

            answer = "Recuerda, si sientes algo inusual en tu pecho o experimentas síntomas preocupantes, no dudes en buscar ayuda médica de inmediato. El tiempo es crucial en estas situaciones, y estamos aquí para ayudarte a recibir la atención que necesitas.\n"
            respuesta =+ answer

        if(sexo == 0):
            if(edad >= 65):
                answer = "Seguir un estilo de vida cardiosaludable que incluya ejercicio físico aeróbico moderado de 3 a 5 veces a la semana -por ejemplo, caminar al menos 150 minutos semanales- y dieta mediterránea baja en sal con consumo de pescado, fruta, verdura y aceite de oliva.\nRealiza chequeos médicos regulares y sigue las recomendaciones de tu médico. Esto incluye mediciones de la presión arterial, el colesterol y la glucosa en sangre.\n\n"
                respuesta =+ answer
            elif(edad < 65):
                answer = "Una dieta saludable puede ayudar a proteger el corazón, mejorar la presión arterial y el colesterol, y reducir el riesgo de tener diabetes tipo 2.\n\n"
                respuesta =+ answer
            if((peso/3.24) < 16.95):
                answer = "La malnutrición, común en personas con peso bajo, puede llevar a una debilidad muscular generalizada, incluido el músculo cardíaco. Un músculo cardíaco debilitado puede tener dificultades para bombear la sangre de manera eficiente, lo que aumenta el riesgo de problemas cardiovasculares.\n\n"
                respuesta =+ answer
            elif(26.3 >= (peso/3.24) >= 16.95):
                answer = "La presión arterial alta y el colesterol alto pueden dañar el corazón y los vasos sanguíneos. Pero sin hacerte los análisis, probablemente no sabrás si tienes estas afecciones. Los exámenes de detección regulares pueden indicarte cuáles son tus cifras y si necesitas tomar medidas.\n\n"
                respuesta =+ answer
            elif((peso/3.24) > 26.3):
                answer = "Tener sobrepeso, especialmente en la mitad del cuerpo, aumenta el riesgo de padecer enfermedades cardíacas. El exceso de peso puede llevar a afecciones que aumentan las probabilidades de desarrollar enfermedades cardíacas, incluidos la presión arterial alta, el colesterol alto y la diabetes tipo 2.\nAntes de realizar cambios significativos en tu dieta o rutina de ejercicios, es recomendable hablar con un médico o un dietista. Obtener orientación personalizada es esencial.\nDefine metas alcanzables y realistas. Establecer objetivos pequeños y a corto plazo puede hacer que el proceso sea más manejable y motivador\n\n"
                respuesta =+ answer
        elif(sexo == 1):
            if(edad >= 50):
                answer = "Seguir un estilo de vida cardiosaludable que incluya ejercicio físico aeróbico moderado de 3 a 5 veces a la semana -por ejemplo, caminar al menos 150 minutos semanales- y dieta mediterránea baja en sal con consumo de pescado, fruta, verdura y aceite de oliva.\nRealiza chequeos médicos regulares y sigue las recomendaciones de tu médico. Esto incluye mediciones de la presión arterial, el colesterol y la glucosa en sangre.\nDiscute con tu médico los cambios hormonales asociados con la menopausia y las opciones de terapia hormonal, si es necesario.\n\n"
                respuesta =+ answer
            elif(edad < 50):
                answer = "Una dieta saludable puede ayudar a proteger el corazón, mejorar la presión arterial y el colesterol, y reducir el riesgo de tener diabetes tipo 2.\n\n"
                respuesta =+ answer
            if((peso/3.09) < 17.95):
                answer = "Antes de realizar cambios en tu dieta o estilo de vida, es crucial hablar con un médico, dietista o nutricionista. Pueden evaluar tu situación específica y proporcionar recomendaciones personalizadas.\n\n"
                respuesta =+ answer
            elif(26.20 >= (peso/3.09) >= 17.95):
                answer = "La presión arterial alta y el colesterol alto pueden dañar el corazón y los vasos sanguíneos. Pero sin hacerte los análisis, probablemente no sabrás si tienes estas afecciones. Los exámenes de detección regulares pueden indicarte cuáles son tus cifras y si necesitas tomar medidas.\n\n"
                respuesta =+ answer
            elif((peso/3.24) > 26.2):
                answer = "Tener sobrepeso, especialmente en la mitad del cuerpo, aumenta el riesgo de padecer enfermedades cardíacas. El exceso de peso puede llevar a afecciones que aumentan las probabilidades de desarrollar enfermedades cardíacas, incluidos la presión arterial alta, el colesterol alto y la diabetes tipo 2.\nAntes de realizar cambios significativos en tu dieta o rutina de ejercicios, es recomendable hablar con un médico o un dietista. Obtener orientación personalizada es esencial.\nDefine metas alcanzables y realistas. Establecer objetivos pequeños y a corto plazo puede hacer que el proceso sea más manejable y motivador\n\n"
                respuesta =+ answer

        if(1 <= fuma < 6):
            answer = "Fumador ligero:\nAunque el consumo es ligero, considera un programa de cese del tabaco para recibir apoyo y estrategias para dejar de fumar.\nDado que el riesgo aún está presente, enfócate en medidas preventivas como la adopción de una dieta saludable y la práctica regular de actividad física.\nRealiza chequeos médicos regulares, especialmente para evaluar la salud cardiovascular y monitorear cualquier cambio.\nRecuerda que estas recomendaciones son generales, y es crucial obtener orientación personalizada de profesionales de la salud. Dejar de fumar y adoptar un estilo de vida saludable son pasos significativos para reducir el riesgo cardiovascular.\n\n"
            respuesta =+ answer
        elif(6 <= fuma < 16):
            answer = "Fumador moderado:\nConsidera programas de cese del tabaco más estructurados, que pueden incluir terapias conductuales y medicamentos recetados si es necesario.\nRealiza una evaluación de riesgo cardiovascular con tu médico y trabaja en medidas específicas para reducir el riesgo.\nAumenta la intensidad y la regularidad de la actividad física para mejorar la salud cardiovascular.\nRecuerda que estas recomendaciones son generales, y es crucial obtener orientación personalizada de profesionales de la salud. Dejar de fumar y adoptar un estilo de vida saludable son pasos significativos para reducir el riesgo cardiovascular.\n\n"
            respuesta =+ answer
        elif(16 <= fuma):
            answer = "mador Pesado:\nBusca asesoramiento profesional para dejar de fumar, que podría incluir terapias intensivas y medicamentos bajo supervisión médica.\nRealiza una evaluación cardíaca completa para evaluar cualquier daño existente y establecer un plan de manejo.\nMantén un control riguroso de la presión arterial, colesterol y azúcar en la sangre. Considera medicamentos si es necesario.\nMantén una supervisión médica continua, especialmente después de dejar de fumar, para evaluar cualquier cambio en la salud.\nRecuerda que estas recomendaciones son generales, y es crucial obtener orientación personalizada de profesionales de la salud. Dejar de fumar y adoptar un estilo de vida saludable son pasos significativos para reducir el riesgo cardiovascular.\n\n"
            respuesta =+ answer

        if(hipertenso == 1):
            answer = "Toma en cuenta estos consejos del Hopital Universari General de Catalunya\n- Debe seguir una dieta pobre en sal. El exceso de sal causa retención de líquidos y en consecuencia aumenta la tensión arterial.\n- Recomendamos no tomar alcohol\n- Un programa de ejercicios adecuado a la edad y capacidades personales ayuda a controlar el peso, a fortalecer nuestro corazón y a controlar la Tensión arterial.\n- Tome la medicación tal y como se le ha indicado. Aunque la presión arterial se haya normalizado no hay que dejar de tomar la medicación nunca.\n- Consulte cualquier duda sobre el tratamiento.\n- Informe siempre a cualquier médico que visite de todos los fármacos que toma, dosis etc.\nAdemás estos puntos importantes, recomendamos además evitar el estrés.\n---SIGNOS DE ALERTA---\nDebe de consultar a su médico o acudir a urgencias en caso de:\nSensación de mareo intenso, alteraciones visuales.\nFuertes dolores de cabeza\nSangrado nasal\nSe ha tomado la tensión y tiene cifras elevadas, y tras nueva toma, habiendo estado sentado 10 minutos se mantienen cifras elevadas.\n\n"
            respuesta =+ answer

        if(diabetes == 1):
            answer = "como ha indicado la World Heart Federation, mantener a raya la diabetes puede reducir hasta en un 42% la probabilidad de padecer una enfermedad cardiovascular y en un 57% el riesgo de infarto, ictus o muerte por causa cardiovascular. Esa es la razón por la que quienes ya padecen la enfermedad deben seguir una serie de recomendaciones que ayudan a prevenir posibles consecuencias cardiovasculares\nAlimentación saludable y equilibrada. Priorizar los alimentos ricos en vitaminas, minerales y fibra, evitar consumir carnes muy grasas o sustituirlas por carnes magras, incluir en el menú verduras, hortalizas, legumbres y pescados, reducir la ingesta de azúcares y de hidratos de carbono, en especial los de alto índice glucémico, o evitar en lo posible el consumo de alcohol.\nPracticar ejercicio de forma frecuente.  Practicar rutinas deportivas de forma regular ayuda al control de la patología.\n\n"
            respuesta =+ answer

        return respuesta