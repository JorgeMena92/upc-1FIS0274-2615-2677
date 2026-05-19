import especialistas as esp

def registrar_especialista(dni=None):

    if dni is None:
        dni = input("Ingrese DNI del especialista: ")

    if dni in esp.especialistas:
        print("Especialista ya fue registrado anteriormente.")
    else:
        nombre          = input("Ingrese nombre: ")
        fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/YYYY): ")
        telefono        = input("Ingrese teléfono: ")
        correo          = input("Ingrese correo electrónico: ")
        direccion       = input("Ingrese dirección: ")
        cmp             = input("Ingrese CMP: ")
        rne             = input("Ingrese RNE: ")
        especialidad    = input("Ingrese especialidad: ")

        print("\n--- Resumen del especialista ---")
        print("DNI                 :", dni)
        print("Nombre              :", nombre)
        print("Fecha de Nacimiento :", fechaNacimiento)
        print("Teléfono            :", telefono)
        print("Correo              :", correo)
        print("Dirección           :", direccion)
        print("CMP                 :", cmp)
        print("RNE                 :", rne)
        print("Especialidad        :", especialidad)
        print("--------------------------------")

        confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
        if confirmacion.upper() != "SI":
            print("Registro cancelado.")
            return

        esp.especialistas[dni] = {
            "dni"              : dni,
            "nombre"           : nombre,
            "fechaNacimiento"  : fechaNacimiento,
            "telefono"         : telefono,
            "correo"           : correo,
            "direccion"        : direccion,
            "cmp"              : cmp,
            "rne"              : rne,
            "especialidad"     : especialidad
        }

        print("Especialista registrado exitosamente.")