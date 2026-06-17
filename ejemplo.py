import time
diccionario = {"nombre":"Juan",
                "fonos":[98659865,63365412,8796542],
                "activo":True
            }

#búsqueda
print("Nombre: ",diccionario["nombre"])
print("Fonos: ",diccionario["fonos"][1])
time.sleep(1)

#Insertar
diccionario["email"]= "juan@gmail.com"
diccionario["fonos"].append(11111111)
print(diccionario)
time.sleep(1)

#Actualizar
diccionario["activo"]=False
diccionario["fonos"][0] = 9999999
print(diccionario)
time.sleep(1)

#Eliminar
del diccionario["nombre"]
diccionario["fonos"].pop(1)
print(diccionario)