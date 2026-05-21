import especialistas as esp
import pacientes as pac
import turnos as tur

from registrarEspecialista import registrar_especialista
from registrarPaciente import registrar_paciente
from registrarDisponibilidad import registrar_disponibilidad
from registrarCita import registrar_cita
from modificarCita import modificar_cita

def main():

    while True:

        print("\n=== Sistema de Citas Médicas ===")
        print("1. Registrar especialista")
        print("2. Registrar paciente")
        print("3. Registrar disponibilidad de especialista")
        print("4. Registrar cita médica")
        print("5. Modificar cita médica")
        print("6. Salir")
        print("================================")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_especialista()
        elif opcion == "2":
            registrar_paciente()
        elif opcion == "3":
            registrar_disponibilidad()
        elif opcion == "4":
            registrar_cita()
        elif opcion == "5":
            modificar_cita()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

main()