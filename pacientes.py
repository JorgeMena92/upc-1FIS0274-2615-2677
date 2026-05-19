# Datos de prueba precargados debido a que el proyecto no cuenta con
# persistencia de datos al no utilizar base de datos. Estos valores
# simulan registros previos para poder probar todas las funcionalidades.

pacientes = {
    "54124536": {
        "dni"             : "54124536",
        "nombre"          : "Daniel Pérez",
        "fechaNacimiento" : "10/08/1998",
        "telefono"        : "924456654",
        "correo"          : "danielperez98@gmail.com",
        "direccion"       : "Lima, Peru"
    },
    "08371624": {
        "dni"             : "08371624",
        "nombre"          : "María Torres",
        "fechaNacimiento" : "22/03/1985",
        "telefono"        : "951782340",
        "correo"          : "mariatorres85@gmail.com",
        "direccion"       : "Miraflores, Lima"
    },
    "37294815": {
        "dni"             : "37294815",
        "nombre"          : "Carlos Quispe",
        "fechaNacimiento" : "05/11/2001",
        "telefono"        : "963104782",
        "correo"          : "carlosquispe01@gmail.com",
        "direccion"       : "San Juan de Lurigancho, Lima"
    },
    "12345678": { # Paciente registrado pero sin cita
        "dni"             : "12345678",
        "nombre"          : "Lucía Ramírez",
        "fechaNacimiento" : "14/07/1995",
        "telefono"        : "987654321",
        "correo"          : "luciaramirez95@gmail.com",
        "direccion"       : "Surco, Lima"
    }
}


# Plantilla de diccionario con datos de paciente

'''
paciente = {
    "dni"             : "",
    "nombre"          : "",
    "fechaNacimiento" : "",
    "telefono"        : "",
    "correo"          : "",
    "direccion"       : ""
}
'''