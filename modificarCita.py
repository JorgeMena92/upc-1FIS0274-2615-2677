import pacientes as pac
import especialistas as esp
import turnos as tur

def modificar_cita():

    # Buscar citas del paciente
    dni = input("Ingrese DNI del paciente: ")
    paciente = pac.pacientes[dni]

    # Buscar turnos ASIGNADO al paciente
    citas = {}
    for idfecha, fecha_data in tur.turnos_junio.items():
        for idturno, turno in fecha_data["turnos"].items():
            if turno["estado"] == "ASIGNADO" and turno["paciente"] == dni:
                citas[idturno] = {
                    "idfecha"    : idfecha,
                    "fecha_data" : fecha_data,
                    "turno"      : turno
                }

    if not citas:
        print("No se encontraron citas registradas para el paciente.")
        return

    # Mostrar citas del paciente
    print("\n--- Citas registradas ---")
    for idturno, cita in citas.items():
        especialidad = esp.especialistas[cita["turno"]["especialista"]]["especialidad"]
        print(str(idturno) + " | " + cita["fecha_data"]["dia"] + " - " + cita["fecha_data"]["fecha"] + ": " + cita["turno"]["turno"] + " | " + especialidad)
    print("-------------------------")

    # Seleccionar cita a modificar
    idturno_seleccionado = int(input("\nIngrese número de turno a modificar: "))
    cita_seleccionada    = citas[idturno_seleccionado]
    idfecha              = cita_seleccionada["idfecha"]
    especialidad         = esp.especialistas[cita_seleccionada["turno"]["especialista"]]["especialidad"]

    # Seleccionar acción
    print("\n1. REPROGRAMAR")
    print("2. CANCELAR")
    accion = input("Seleccione una acción: ")

    # ── CANCELAR ──────────────────────────────────────────────────────────────
    if accion == "2":
        tur.turnos_junio[idfecha]["turnos"][idturno_seleccionado]["estado"]   = "RESERVADO"
        tur.turnos_junio[idfecha]["turnos"][idturno_seleccionado]["paciente"] = "LIBRE"
        print("Cita cancelada exitosamente.")

    # ── REPROGRAMAR ───────────────────────────────────────────────────────────
    elif accion == "1":

        # Guardar referencia del turno anterior
        idfecha_anterior  = idfecha
        idturno_anterior  = idturno_seleccionado

        # Liberar turno anterior
        tur.turnos_junio[idfecha]["turnos"][idturno_seleccionado]["estado"]   = "RESERVADO"
        tur.turnos_junio[idfecha]["turnos"][idturno_seleccionado]["paciente"] = "LIBRE"

        # Buscar especialistas con la misma especialidad
        especialistas_filtrados = [
            dni_esp for dni_esp, e in esp.especialistas.items()
            if e["especialidad"] == especialidad
        ]

        # Buscar turnos RESERVADOS disponibles (excluyendo el anterior)
        turnos_disponibles = {}
        for idfecha2, fecha_data2 in tur.turnos_junio.items():
            turnos_fecha = {
                idturno: turno
                for idturno, turno in fecha_data2["turnos"].items()
                if turno["estado"] == "RESERVADO"
                and turno["especialista"] in especialistas_filtrados
                and turno["paciente"] == "LIBRE"
                and not (idfecha2 == idfecha_anterior and idturno == idturno_anterior)  # ← excluir anterior
            }
            if turnos_fecha:
                turnos_disponibles[idfecha2] = {
                    "fecha_data" : fecha_data2,
                    "turnos"     : turnos_fecha
                }

        if not turnos_disponibles:
            print("No hay turnos disponibles para reprogramar.")
            return

        # Mostrar turnos disponibles
        print("\n--- Turnos disponibles ---")
        for idfecha2, data in turnos_disponibles.items():
            turnos_str = " | ".join(turno["turno"] for turno in data["turnos"].values())
            print(data["fecha_data"]["dia"] + " - " + data["fecha_data"]["fecha"] + ":   " + turnos_str)
        print("--------------------------")

        # Seleccionar nueva fecha y turno
        fecha2 = input("\nIngrese nueva fecha (DD/MM/YYYY): ")
        dia, mes, anio = fecha2.split("/")
        idfecha2 = anio + mes + dia

        fecha_data2   = turnos_disponibles[idfecha2]["fecha_data"]
        turnos_fecha2 = turnos_disponibles[idfecha2]["turnos"]

        print("\n" + fecha_data2["dia"] + " - " + fecha_data2["fecha"])
        print("-----------------------------")
        for idturno, turno in turnos_fecha2.items():
            print(str(idturno) + " | " + turno["turno"])
        print("-----------------------------")

        idturno_nuevo = int(input("Ingrese número de turno: "))

        # Guardar nuevo turno
        tur.turnos_junio[idfecha2]["turnos"][idturno_nuevo]["estado"]   = "ASIGNADO"
        tur.turnos_junio[idfecha2]["turnos"][idturno_nuevo]["paciente"] = dni

        turno_nuevo = tur.turnos_junio[idfecha2]["turnos"][idturno_nuevo]

        # Resumen
        print("\n--- Cita reprogramada exitosamente ---")
        print("DNI          : " + paciente["dni"])
        print("Paciente     : " + paciente["nombre"])
        print("Especialidad : " + especialidad)
        print("Nueva fecha  : " + fecha_data2["fecha"])
        print("Nueva hora   : " + turno_nuevo["turno"])
        print("--------------------------------------")
