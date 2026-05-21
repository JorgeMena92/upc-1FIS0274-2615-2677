import especialistas as esp
import turnos as tur


def obtener_fechas_disponibles(fechas_ya_registradas):
    fechas_disponibles = []
    for idfecha, fecha_data in tur.turnos.items():
        if fecha_data["laborable"] != 1:
            continue
        if idfecha in fechas_ya_registradas:
            continue
        for turno in fecha_data["turnos"].values():
            if turno["estado"] == "LIBRE":
                fechas_disponibles.append(idfecha)
                break
    return fechas_disponibles


def mostrar_fechas(fechas_disponibles):
    print("\n--- Fechas disponibles ---")
    i = 1
    for idfecha in fechas_disponibles:
        fecha_data = tur.turnos[idfecha]
        print(f"{i} | {fecha_data['dia']} - {fecha_data['fecha']}")
        i += 1
    print("--------------------------")


def obtener_turnos_libres(idfecha):
    turnos_libres = []
    fecha_data = tur.turnos[idfecha]
    print(f"\n{fecha_data['dia']} - {fecha_data['fecha']}")
    print("-----------------------------")
    for idturno, turno in fecha_data["turnos"].items():
        if turno["estado"] == "LIBRE":
            turnos_libres.append(idturno)
            print(f"{idturno} | {turno['turno']}")
    print("-----------------------------")
    return turnos_libres


def seleccionar_turnos(idfecha, turnos_libres):
    turnos_seleccionados = []
    while True:
        seleccion = input("Ingrese número de turno (o 'fin' para terminar): ")
        if seleccion == "fin":
            break
        seleccion = int(seleccion)
        if seleccion not in turnos_libres:
            print("Turno no válido o no disponible.")
        elif seleccion in turnos_seleccionados:
            print("Turno ya seleccionado.")
        else:
            turnos_seleccionados.append(seleccion)
            print(f"Turno {tur.turnos[idfecha]['turnos'][seleccion]['turno']} agregado.")
    return turnos_seleccionados


def confirmar_y_guardar(idfecha, fecha, turnos_seleccionados, dni):
    fecha_data = tur.turnos[idfecha]
    print("\n--- Resumen de turnos seleccionados ---")
    for idturno in turnos_seleccionados:
        turno = fecha_data["turnos"][idturno]
        print(f"{fecha_data['dia']} - {fecha}: {turno['turno']}")

    confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
    if confirmacion.upper() != "SI":
        print("Registro cancelado.")
        return False

    for idturno in turnos_seleccionados:
        tur.turnos[idfecha]["turnos"][idturno]["estado"]       = "RESERVADO"
        tur.turnos[idfecha]["turnos"][idturno]["especialista"] = dni
    print("Turnos registrados exitosamente.")
    return True


def registrar_disponibilidad():

    # Identificar al especialista
    dni = input("Ingrese DNI del especialista: ")
    if dni not in esp.especialistas:
        print("Especialista no encontrado, debe registrarse primero.")
        return

    print("Especialista encontrado:", esp.especialistas[dni]["nombre"])

    fechas_ya_registradas = []

    while True:

        fechas_disponibles = obtener_fechas_disponibles(fechas_ya_registradas)
        if not fechas_disponibles: # validar si la lista está vacía
            print("No hay más fechas disponibles con turnos libres.")
            print("Registro de disponibilidad finalizado.")
            break # se termina si no hay fechas disponibles

        mostrar_fechas(fechas_disponibles)

        fecha = input("\nIngrese fecha (DD/MM/YYYY): ")
        dia, mes, anio = fecha.split("/")
        idfecha = anio + mes + dia

        turnos_libres        = obtener_turnos_libres(idfecha)
        turnos_seleccionados = seleccionar_turnos(idfecha, turnos_libres)
        guardado             = confirmar_y_guardar(idfecha, fecha, turnos_seleccionados, dni)

        if guardado:
            fechas_ya_registradas.append(idfecha)

        otra = input("\n¿Desea registrar disponibilidad en otra fecha? (SI/NO): ")
        if otra.upper() != "SI":
            print("Registro de disponibilidad finalizado.")
            break # se termina si el usuario no desea continuar