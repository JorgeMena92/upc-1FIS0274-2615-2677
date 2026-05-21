import especialistas as esp


def pedir_datos_especialista(dni):

    nombre          = input("Ingrese nombre: ")
    fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/YYYY): ")
    telefono        = input("Ingrese teléfono: ")
    correo          = input("Ingrese correo electrónico: ")
    direccion       = input("Ingrese dirección: ")
    cmp             = input("Ingrese CMP: ")
    rne             = input("Ingrese RNE: ")
    especialidad    = input("Ingrese especialidad: ")

    return {
        "dni"            : dni,
        "nombre"         : nombre,
        "fechaNacimiento": fechaNacimiento,
        "telefono"       : telefono,
        "correo"         : correo,
        "direccion"      : direccion,
        "cmp"            : cmp,
        "rne"            : rne,
        "especialidad"   : especialidad
    }


def mostrar_resumen_especialista(datos):
    
    print("\n--- Resumen del especialista ---")
    print(f"DNI                 : {datos['dni']}")
    print(f"Nombre              : {datos['nombre']}")
    print(f"Fecha de Nacimiento : {datos['fechaNacimiento']}")
    print(f"Teléfono            : {datos['telefono']}")
    print(f"Correo              : {datos['correo']}")
    print(f"Dirección           : {datos['direccion']}")
    print(f"CMP                 : {datos['cmp']}")
    print(f"RNE                 : {datos['rne']}")
    print(f"Especialidad        : {datos['especialidad']}")
    print("--------------------------------")


def registrar_especialista(dni=None):

    if dni is None:
        dni = input("Ingrese DNI del especialista: ")

    if dni in esp.especialistas:
        print("Especialista ya fue registrado anteriormente.")
        return

    datos = pedir_datos_especialista(dni)
    mostrar_resumen_especialista(datos)

    confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
    if confirmacion.upper() != "SI":
        print("Registro cancelado.")
        return

    esp.especialistas[dni] = datos
    print("Especialista registrado exitosamente.")