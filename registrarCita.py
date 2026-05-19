import pacientes as pac
import especialistas as esp
import turnos as tur
from registrarPaciente import registrar_paciente

def registrar_cita():

    # Identificar o registrar al paciente
    dni = input("Ingrese DNI del paciente: ")
    if dni not in pac.pacientes:
        registrar_paciente(dni)
    else:
        print("Paciente encontrado:", pac.pacientes[dni]["nombre"])

    if dni not in pac.pacientes:
        return

    paciente = pac.pacientes[dni]

    # Obtener especialidades disponibles
    especialidades = list(set(
        e["especialidad"] for e in esp.especialistas.values()
    ))

    print("\n--- Especialidades disponibles ---")
    for i, especialidad in enumerate(especialidades, start=1):
        print(str(i) + " | " + especialidad)
    print("----------------------------------")

    seleccion = int(input("\nIngrese número de especialidad: "))
    especialidad_seleccionada = especialidades[seleccion - 1]
    print("Especialidad seleccionada:", especialidad_seleccionada)

    # Buscar especialistas con esa especialidad
    especialistas_filtrados = [
        dni_esp for dni_esp, e in esp.especialistas.items()
        if e["especialidad"] == especialidad_seleccionada
    ]

    # Buscar turnos RESERVADOS de esos especialistas
    turnos_disponibles = {}
    for idfecha, fecha_data in tur.turnos.items():
        turnos_fecha = {
            idturno: turno
            for idturno, turno in fecha_data["turnos"].items()
            if turno["estado"] == "RESERVADO"
            and turno["especialista"] in especialistas_filtrados
            and turno["paciente"] == "LIBRE"   # ← agregar esta línea
        }
        if turnos_fecha:
            turnos_disponibles[idfecha] = {
                "fecha_data" : fecha_data,
                "turnos"     : turnos_fecha
            }

    if not turnos_disponibles:
        print("No hay turnos disponibles para esta especialidad.")
        return

    # Mostrar turnos disponibles
    print("\n--- Turnos disponibles ---")
    for idfecha, data in turnos_disponibles.items():
        fecha_data = data["fecha_data"]
        turnos_str = " | ".join(
            turno["turno"] for turno in data["turnos"].values()
        )
        print(fecha_data["dia"] + " - " + fecha_data["fecha"] + ":   " + turnos_str)
    print("--------------------------")

    # Seleccionar fecha
    fecha = input("\nIngrese fecha (DD/MM/YYYY): ")
    partes = fecha.split("/")
    dia, mes, anio = partes
    idfecha = anio + mes + dia

    # Mostrar turnos de esa fecha
    turnos_fecha = turnos_disponibles[idfecha]["turnos"]
    fecha_data   = turnos_disponibles[idfecha]["fecha_data"]

    print("\n" + fecha_data["dia"] + " - " + fecha_data["fecha"])
    print("-----------------------------")
    for idturno, turno in turnos_fecha.items():
        print(str(idturno) + " | " + turno["turno"])
    print("-----------------------------")

    # Seleccionar turno
    idturno_seleccionado = int(input("Ingrese número de turno: "))

    # Guardar cita
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["estado"]   = "ASIGNADO"
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["paciente"] = dni

    turno_final = tur.turnos[idfecha]["turnos"][idturno_seleccionado]

    # Resumen final
    print("\n--- Cita registrada exitosamente ---")
    print("DNI          : " + paciente["dni"])
    print("Paciente     : " + paciente["nombre"])
    print("Especialidad : " + especialidad_seleccionada)
    print("Fecha        : " + fecha_data["fecha"])
    print("Hora         : " + turno_final["turno"])
    print("------------------------------------")