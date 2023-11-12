class Respuesta():

    def __init__(self, res, sexo, edad, peso, fuma, hipertenso, diabetes, respuesta=""):

        if(res):
            if(res >= 99.99):
                answer = ""
                respuesta =+ answer
            elif(res >= 99.99):
                answer = ""
                respuesta =+ answer
            elif(res >= 99.99):
                answer = ""
                respuesta =+ answer
            elif(res >= 99.99):
                answer = ""
                respuesta =+ answer
            elif(res >= 99.99):
                answer = ""
                respuesta =+ answer

        if(sexo == 1):
            if(edad >= 65):
                answer = ""
                respuesta =+ answer
            elif(edad < 65):
                answer = ""
                respuesta =+ answer
            if(peso < 99.99):
                answer = ""
                respuesta =+ answer
            elif(peso < 99.99):
                answer = ""
                respuesta =+ answer
            elif(peso < 99.99):
                answer = ""
                respuesta =+ answer
        elif(sexo == 0):
            if(edad >= 50):
                answer = ""
                respuesta =+ answer
            elif(edad < 50):
                answer = ""
                respuesta =+ answer
            if(peso < 99.99):
                answer = ""
                respuesta =+ answer
            elif(peso < 99.99):
                answer = ""
                respuesta =+ answer
            elif(peso < 99.99):
                answer = ""
                respuesta =+ answer

        if(fuma == 1):
            answer = ""
            respuesta =+ answer
        elif(fuma == 0):
            answer = ""
            respuesta =+ answer

        if(hipertenso == 1):
            answer = ""
            respuesta =+ answer
        elif(hipertenso == 0):
            answer = ""
            respuesta =+ answer

        if(diabetes == 1):
            answer = ""
            respuesta =+ answer
        elif(diabetes == 0):
            answer = ""
            respuesta =+ answer

        return respuesta