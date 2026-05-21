import pacientes as pac
import especialistas as esp
import turnos as tur


def buscar_citas_paciente(dni):
    citas = {}
    for idfecha, fecha_data in tur.turnos.items():
        for idturno, turno in fecha_data["turnos"].items():
            if turno["estado"] != "ASIGNADO":
                continue
            if turno["paciente"] != dni:
                continue
            citas[idturno] = {
                "idfecha"   : idfecha,
                "fecha_data": fecha_data,
                "turno"     : turno
            }
    return citas


def mostrar_citas(citas):
    print("\n--- Citas registradas ---")
    for idturno, cita in citas.items():
        especialidad = esp.especialistas[cita["turno"]["especialista"]]["especialidad"]
        print(f"{idturno} | {cita['fecha_data']['dia']} - {cita['fecha_data']['fecha']}: {cita['turno']['turno']} | {especialidad}")
    print("-------------------------")


def cancelar_cita(idfecha, idturno_seleccionado):
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["estado"]   = "RESERVADO"
    tur.turnos[idfecha]["turnos"][idturno_seleccionado]["paciente"] = "LIBRE"
    print("Cita cancelada exitosamente.")


def obtener_turnos_reprogramar(especialidad, idfecha_anterior, idturno_anterior):
    especialistas_filtrados = []
    for dni_esp, e in esp.especialistas.items():
        if e["especialidad"] == especialidad:
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
            if idfecha == idfecha_anterior and idturno == idturno_anterior:
                continue
            turnos_fecha[idturno] = turno
        if turnos_fecha:
            turnos_disponibles[idfecha] = {
                "fecha_data": fecha_data,
                "turnos"    : turnos_fecha
            }
    return turnos_disponibles


def mostrar_turnos_reprogramar(turnos_disponibles):
    print("\n--- Turnos disponibles ---")
    for idfecha, data in turnos_disponibles.items():
        turnos_lista = []
        for turno in data["turnos"].values():
            turnos_lista.append(turno["turno"])
        turnos_str = " | ".join(turnos_lista)
        print(f"{data['fecha_data']['dia']} - {data['fecha_data']['fecha']}:   {turnos_str}")
    print("--------------------------")


def seleccionar_nuevo_turno(turnos_disponibles):
    fecha = input("\nIngrese nueva fecha (DD/MM/YYYY): ")
    dia, mes, anio = fecha.split("/")
    idfecha = anio + mes + dia

    fecha_data   = turnos_disponibles[idfecha]["fecha_data"]
    turnos_fecha = turnos_disponibles[idfecha]["turnos"]

    print(f"\n{fecha_data['dia']} - {fecha_data['fecha']}")
    print("-----------------------------")
    for idturno, turno in turnos_fecha.items():
        print(f"{idturno} | {turno['turno']}")
    print("-----------------------------")

    idturno_nuevo = int(input("Ingrese número de turno: "))
    return idfecha, idturno_nuevo, fecha_data


def guardar_reprogramacion(idfecha_nuevo, idturno_nuevo, dni):
    tur.turnos[idfecha_nuevo]["turnos"][idturno_nuevo]["estado"]   = "ASIGNADO"
    tur.turnos[idfecha_nuevo]["turnos"][idturno_nuevo]["paciente"] = dni


def mostrar_resumen_reprogramacion(dni, especialidad, fecha_data, turno_nuevo):
    paciente = pac.pacientes[dni]
    print("\n--- Cita reprogramada exitosamente ---")
    print(f"DNI          : {paciente['dni']}")
    print(f"Paciente     : {paciente['nombre']}")
    print(f"Especialidad : {especialidad}")
    print(f"Nueva fecha  : {fecha_data['fecha']}")
    print(f"Nueva hora   : {turno_nuevo['turno']}")
    print("--------------------------------------")


def reprogramar_cita(dni, idfecha, idturno_seleccionado, especialidad):

    # Liberar turno anterior
    idfecha_anterior  = idfecha
    idturno_anterior  = idturno_seleccionado
    cancelar_cita(idfecha, idturno_seleccionado)

    turnos_disponibles = obtener_turnos_reprogramar(especialidad, idfecha_anterior, idturno_anterior)
    if not turnos_disponibles:
        print("No hay turnos disponibles para reprogramar.")
        return

    mostrar_turnos_reprogramar(turnos_disponibles)

    idfecha_nuevo, idturno_nuevo, fecha_data = seleccionar_nuevo_turno(turnos_disponibles)

    guardar_reprogramacion(idfecha_nuevo, idturno_nuevo, dni)

    turno_nuevo = tur.turnos[idfecha_nuevo]["turnos"][idturno_nuevo]
    mostrar_resumen_reprogramacion(dni, especialidad, fecha_data, turno_nuevo)


def modificar_cita():

    dni      = input("Ingrese DNI del paciente: ")
    paciente = pac.pacientes[dni]

    citas = buscar_citas_paciente(dni)
    if not citas:
        print("No se encontraron citas registradas para el paciente.")
        return

    mostrar_citas(citas)

    idturno_seleccionado = int(input("\nIngrese número de turno a modificar: "))
    cita_seleccionada    = citas[idturno_seleccionado]
    idfecha              = cita_seleccionada["idfecha"]
    especialidad         = esp.especialistas[cita_seleccionada["turno"]["especialista"]]["especialidad"]

    print("\n1. REPROGRAMAR")
    print("2. CANCELAR")
    accion = input("Seleccione una acción: ")

    if accion == "2":
        cancelar_cita(idfecha, idturno_seleccionado)
    elif accion == "1":
        reprogramar_cita(dni, idfecha, idturno_seleccionado, especialidad)