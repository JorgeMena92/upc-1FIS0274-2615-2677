import pacientes as pac

def registrar_paciente(dni=None):

    if dni is None:
        dni = input("Ingrese DNI del paciente: ")
    
    if dni in pac.pacientes:
        print("Paciente ya fue registrado anteriormente.")
    else:
        nombre          = input("Ingrese nombre: ")
        fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/YYYY): ")
        telefono        = input("Ingrese teléfono: ")
        correo          = input("Ingrese correo electrónico: ")
        direccion       = input("Ingrese dirección: ")

        print("\n--- Resumen del paciente ---")
        print("DNI                 :", dni)
        print("Nombre              :", nombre)
        print("Fecha de Nacimiento :", fechaNacimiento)
        print("Teléfono            :", telefono)
        print("Correo              :", correo)
        print("Dirección           :", direccion)
        print("--------------------------------")

        confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
        if confirmacion.upper() != "SI":
            print("Registro cancelado.")
            return

        pac.pacientes[dni] = {
            "dni"              : dni,
            "nombre"           : nombre,
            "fechaNacimiento"  : fechaNacimiento,     
            "telefono"         : telefono,   
            "correo"           : correo,
            "direccion"        : direccion
        }
        
        print("Paciente registrado exitosamente.")