import especialistas as esp
import turnos as tur

def registrar_disponibilidad():

    # Identificar al especialista
    dni = input("Ingrese DNI del especialista: ")
    if dni not in esp.especialistas:
        print("Especialista no encontrado, debe registrarse primero.")
        return

    print("Especialista encontrado:", esp.especialistas[dni]["nombre"])

    fechas_ya_registradas = []

    while True:

        # Recalcular fechas disponibles en cada iteración
        fechas_disponibles = [
            idfecha for idfecha, fecha_data in tur.turnos.items()
            if fecha_data["laborable"] == 1
            and idfecha not in fechas_ya_registradas
            and any(turno["estado"] == "LIBRE" for turno in fecha_data["turnos"].values())
        ]

        if not fechas_disponibles:
            print("No hay más fechas disponibles con turnos libres.")
            break

        # Mostrar fechas disponibles
        print("\n--- Fechas disponibles ---")
        for i, idfecha in enumerate(fechas_disponibles, start=1):
            fecha_data = tur.turnos[idfecha]
            print(str(i) + " | " + fecha_data["dia"] + " - " + fecha_data["fecha"])
        print("--------------------------")

        # Solicitar fecha
        fecha = input("\nIngrese fecha (DD/MM/YYYY): ")
        partes = fecha.split("/")
        dia, mes, anio = partes
        idfecha = anio + mes + dia

        # Mostrar turnos libres
        turnos_libres = []
        fecha_data = tur.turnos[idfecha]
        print("\n" + fecha_data["dia"] + " - " + fecha_data["fecha"])
        print("-----------------------------")
        for idturno, turno in fecha_data["turnos"].items():
            if turno["estado"] == "LIBRE":
                turnos_libres.append(idturno)
                print(str(idturno) + " | " + turno["turno"])
        print("-----------------------------")

        # Seleccionar turnos
        turnos_seleccionados = []
        while True:
            seleccion = input("Ingrese número de turno (o 'fin' para terminar): ")
            if seleccion == "fin":
                break
            seleccion = int(seleccion)
            if seleccion not in turnos_libres:          # ← validación agregada
                print("Turno no válido o no disponible.")
            elif seleccion in turnos_seleccionados:
                print("Turno ya seleccionado.")
            else:
                turnos_seleccionados.append(seleccion)
                print("Turno " + tur.turnos[idfecha]["turnos"][seleccion]["turno"] + " agregado.")
                
        # Mostrar resumen
        print("\n--- Resumen de turnos seleccionados ---")
        for idturno in turnos_seleccionados:
            turno = fecha_data["turnos"][idturno]
            print(fecha_data["dia"] + " - " + fecha + ": " + turno["turno"])

        # Confirmación
        confirmacion = input("\n¿Confirma el registro? (SI/NO): ")
        if confirmacion.upper() != "SI":
            print("Registro cancelado.")
        else:
            for idturno in turnos_seleccionados:
                tur.turnos[idfecha]["turnos"][idturno]["estado"]       = "RESERVADO"
                tur.turnos[idfecha]["turnos"][idturno]["especialista"] = dni
            fechas_ya_registradas.append(idfecha)
            print("Turnos registrados exitosamente.")

        # ¿Otra fecha?
        otra = input("\n¿Desea registrar disponibilidad en otra fecha? (SI/NO): ")
        if otra.upper() != "SI":
            break


registrar_disponibilidad()