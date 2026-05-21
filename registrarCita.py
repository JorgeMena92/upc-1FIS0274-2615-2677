import pacientes as pac
import especialistas as esp
import turnos as tur
from registrarPaciente import registrar_paciente


def identificar_paciente(dni):
    if dni not in pac.pacientes:
        registrar_paciente(dni)
    else:
        print(f"Paciente encontrado: {pac.pacientes[dni]['nombre']}")

# Obteniendo especialidades de diccionario de especialistas
def obtener_especialidades():
    especialidades = []
    for e in esp.especialistas.values():
        if e["especialidad"] not in especialidades:
            especialidades.append(e["especialidad"])

    print("\n--- Especialidades disponibles ---")
    i = 1
    for especialidad in especialidades:
        print(f"{i} | {especialidad}")
        i += 1
    print("----------------------------------")

    seleccion = int(input("\nIngrese número de especialidad: "))
    especialidad_seleccionada = especialidades[seleccion - 1]
    print(f"Especialidad seleccionada: {especialidad_seleccionada}")
    return especialidad_seleccionada


def obtener_turnos_disponibles(especialidad_seleccionada):

    especialistas_filtrados = []
    for dni_esp, e in esp.especialistas.items():
        if e["especialidad"] == especialidad_seleccionada:
            especialistas_filtrados.append(dni_esp)

    turnos_disponibles = {}
    for idfecha, fecha_data in tur.turnos.items():
        turnos_fecha = {}
        for idturno, turno in fecha_data["turnos"].items():
            if turno["estado"] != "RESERVADO":
                continue
            if turno["especialista"] not in especialistas_filtrados:
                continue
            if turno["paciente"] != "LIBRE":
                continue
            turnos_fecha[idturno] = turno # filtra los turnos que cumplen las condiciones de arriba
        if turnos_fecha:
            turnos_disponibles[idfecha] = {
                "fecha_data": fecha_data,
                "turnos"    : turnos_fecha
            }

    return turnos_disponibles


def mostrar_turnos_disponibles(turnos_disponibles):
    print("\n--- Turnos disponibles ---")
    for idfecha, data in turnos_disponibles.items():
        fecha_data = data["fecha_data"]
        turnos_lista = []
        for turno in data["turnos"].values():
            turnos_lista.append(turno["turno"])
        turnos_str = " | ".join(turnos_lista)
        print(f"{fecha_data['dia']} - {fecha_data['fecha']}:   {turnos_str}")
    print("--------------------------")


def seleccionar_fecha_y_turno(turnos_disponibles):
    fecha = input("\nIngrese fecha (DD/MM/YYYY): ")
    dia, mes, anio = fecha.split("/")
    idfecha = anio + mes + dia

    turnos_fecha = turnos_disponibles[idfecha]["turnos"]
    fecha_data   = turnos_disponibles[idfecha]["fecha_data"]

    print(f"\n{fecha_data['dia']} - {fecha_data['fecha']}")
    print("-----------------------------")
    for idturno, turno in turnos_fecha.items():
        print(f"{idturno} | {turno['turno']}")
    print("-----------------------------")

    idturno_seleccionado = int(input("Ingrese número de turno: "))
    return idfecha, idturno_seleccionado, fecha_data


def guardar_cita(idfecha, idturno_seleccionado, dni):
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["estado"]   = "ASIGNADO"
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["paciente"] = dni


def mostrar_resumen_cita(dni, especialidad_seleccionada, fecha_data, turno_final):
    paciente = pac.pacientes[dni]
    print("\n--- Cita registrada exitosamente ---")
    print(f"DNI          : {paciente['dni']}")
    print(f"Paciente     : {paciente['nombre']}")
    print(f"Especialidad : {especialidad_seleccionada}")
    print(f"Fecha        : {fecha_data['fecha']}")
    print(f"Hora         : {turno_final['turno']}")
    print("------------------------------------")


def registrar_cita():

    dni = input("Ingrese DNI del paciente: ")
    identificar_paciente(dni)

    # Validación de confirmación del registro del paciente
    if dni not in pac.pacientes:
        return

    especialidad_seleccionada = obtener_especialidades()

    turnos_disponibles = obtener_turnos_disponibles(especialidad_seleccionada)
    if not turnos_disponibles:
        print("No hay turnos disponibles para esta especialidad.")
        return

    mostrar_turnos_disponibles(turnos_disponibles)

    idfecha, idturno_seleccionado, fecha_data = seleccionar_fecha_y_turno(turnos_disponibles)

    guardar_cita(idfecha, idturno_seleccionado, dni)

    turno_final = tur.turnos[idfecha]["turnos"][idturno_seleccionado]
    mostrar_resumen_cita(dni, especialidad_seleccionada, fecha_data, turno_final)