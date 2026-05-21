import pacientes as pac


def pedir_datos_paciente(dni):

    nombre          = input("Ingrese nombre: ")
    fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/YYYY): ")
    telefono        = input("Ingrese teléfono: ")
    correo          = input("Ingrese correo electrónico: ")
    direccion       = input("Ingrese dirección: ")

    return {
        "dni"            : dni,
        "nombre"         : nombre,
        "fechaNacimiento": fechaNacimiento,
        "telefono"       : telefono,
        "correo"         : correo,
        "direccion"      : direccion
    }


def mostrar_resumen_paciente(datos):
    
    print("\n--- Resumen del paciente ---")
    print(f"DNI                 : {datos['dni']}")
    print(f"Nombre              : {datos['nombre']}")
    print(f"Fecha de Nacimiento : {datos['fechaNacimiento']}")
    print(f"Teléfono            : {datos['telefono']}")
    print(f"Correo              : {datos['correo']}")
    print(f"Dirección           : {datos['direccion']}")
    print("--------------------------------")


def registrar_paciente(dni=None):

    if dni is None:
        dni = input("Ingrese DNI del paciente: ")

    if dni in pac.pacientes:
        print("Paciente ya fue registrado anteriormente.")
        return

    datos = pedir_datos_paciente(dni)
    mostrar_resumen_paciente(datos)

    confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
    if confirmacion.upper() != "SI":
        print("Registro cancelado.")
        return

    pac.pacientes[dni] = datos
    print("Paciente registrado exitosamente.")