
# Datos de prueba precargados debido a que el proyecto no cuenta con
# persistencia de datos al no utilizar base de datos. Estos valores
# simulan registros previos para poder probar todas las funcionalidades.

especialistas = {
    "47485946": {
        "dni"                    : "47485946",
        "nombre"                 : "Jorge Mena",
        "fechaNacimiento"        : "16/12/1992",
        "telefono"               : "924976359",
        "correo"                 : "jorgemenasalas92@gmail.com",
        "direccion"              : "Oxapampa, Peru",
        "cmp"                    : "20451246",
        "rne"                    : "21678542",
        "especialidad"           : "Medicina General"
    }
}


# Plantilla de diccionario con datos de especialista

'''
especialista = {
    "nombre"              : "",
    "dni"                 : "",
    "fechaNacimiento"     : "",
    "telefono"            : "",
    "correo"              : "",
    "direccion"           : "",
    "cmp"                 : "",
    "rne"                 : "",
    "especialidad"        : ""
}
'''

print(especialistas)