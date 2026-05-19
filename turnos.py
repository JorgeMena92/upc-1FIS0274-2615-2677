# Datos de prueba precargados debido a que el proyecto no cuenta con
# persistencia de datos al no utilizar base de datos. Estos valores
# simulan registros previos para poder probar todas las funcionalidades.

# En este caso se usan los datos de los dos primeros día de Junio 2026.

# Estados posibles de un turno:
#   LIBRE     → el turno no tiene especialista asignado, está disponible para registrar disponibilidad.
#   RESERVADO → el especialista registró disponibilidad, pero aún no hay paciente asignado.
#   ASIGNADO  → el turno tiene paciente asignado, la cita está confirmada.

turnos = {
    "20260601": {
        "idfecha": "20260601",
        "fecha": "01/06/2026",
        "dia": "Lunes",
        "laborable": 1,
        "turnos": {
            1:  { "idturno": 1,  "hora_inicio": "9:00",  "hora_fin": "9:30",  "turno": "9:00 - 9:30",   "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            2:  { "idturno": 2,  "hora_inicio": "9:30",  "hora_fin": "10:00", "turno": "9:30 - 10:00",  "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            3:  { "idturno": 3,  "hora_inicio": "10:00", "hora_fin": "10:30", "turno": "10:00 - 10:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            4:  { "idturno": 4,  "hora_inicio": "10:30", "hora_fin": "11:00", "turno": "10:30 - 11:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            5:  { "idturno": 5,  "hora_inicio": "11:00", "hora_fin": "11:30", "turno": "11:00 - 11:30", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "54124536" },
            6:  { "idturno": 6,  "hora_inicio": "11:30", "hora_fin": "12:00", "turno": "11:30 - 12:00", "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
            7:  { "idturno": 7,  "hora_inicio": "12:00", "hora_fin": "12:30", "turno": "12:00 - 12:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            8:  { "idturno": 8,  "hora_inicio": "12:30", "hora_fin": "13:00", "turno": "12:30 - 13:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            9:  { "idturno": 9,  "hora_inicio": "13:00", "hora_fin": "13:30", "turno": "13:00 - 13:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            10: { "idturno": 10, "hora_inicio": "13:30", "hora_fin": "14:00", "turno": "13:30 - 14:00", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "08371624" },
            11: { "idturno": 11, "hora_inicio": "14:00", "hora_fin": "14:30", "turno": "14:00 - 14:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            12: { "idturno": 12, "hora_inicio": "14:30", "hora_fin": "15:00", "turno": "14:30 - 15:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            13: { "idturno": 13, "hora_inicio": "15:00", "hora_fin": "15:30", "turno": "15:00 - 15:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            14: { "idturno": 14, "hora_inicio": "15:30", "hora_fin": "16:00", "turno": "15:30 - 16:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            15: { "idturno": 15, "hora_inicio": "16:00", "hora_fin": "16:30", "turno": "16:00 - 16:30", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "37294815" },
            16: { "idturno": 16, "hora_inicio": "16:30", "hora_fin": "17:00", "turno": "16:30 - 17:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            17: { "idturno": 17, "hora_inicio": "17:00", "hora_fin": "17:30", "turno": "17:00 - 17:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            18: { "idturno": 18, "hora_inicio": "17:30", "hora_fin": "18:00", "turno": "17:30 - 18:00", "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
        }
    },
    "20260602": {
        "idfecha": "20260602",
        "fecha": "02/06/2026",
        "dia": "Martes",
        "laborable": 1,
        "turnos": {
            1:  { "idturno": 1,  "hora_inicio": "9:00",  "hora_fin": "9:30",  "turno": "9:00 - 9:30",   "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
            2:  { "idturno": 2,  "hora_inicio": "9:30",  "hora_fin": "10:00", "turno": "9:30 - 10:00",  "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            3:  { "idturno": 3,  "hora_inicio": "10:00", "hora_fin": "10:30", "turno": "10:00 - 10:30", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "12345678" },
            4:  { "idturno": 4,  "hora_inicio": "10:30", "hora_fin": "11:00", "turno": "10:30 - 11:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            5:  { "idturno": 5,  "hora_inicio": "11:00", "hora_fin": "11:30", "turno": "11:00 - 11:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            6:  { "idturno": 6,  "hora_inicio": "11:30", "hora_fin": "12:00", "turno": "11:30 - 12:00", "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
            7:  { "idturno": 7,  "hora_inicio": "12:00", "hora_fin": "12:30", "turno": "12:00 - 12:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            8:  { "idturno": 8,  "hora_inicio": "12:30", "hora_fin": "13:00", "turno": "12:30 - 13:00", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "08371624" },
            9:  { "idturno": 9,  "hora_inicio": "13:00", "hora_fin": "13:30", "turno": "13:00 - 13:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            10: { "idturno": 10, "hora_inicio": "13:30", "hora_fin": "14:00", "turno": "13:30 - 14:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            11: { "idturno": 11, "hora_inicio": "14:00", "hora_fin": "14:30", "turno": "14:00 - 14:30", "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
            12: { "idturno": 12, "hora_inicio": "14:30", "hora_fin": "15:00", "turno": "14:30 - 15:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            13: { "idturno": 13, "hora_inicio": "15:00", "hora_fin": "15:30", "turno": "15:00 - 15:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            14: { "idturno": 14, "hora_inicio": "15:30", "hora_fin": "16:00", "turno": "15:30 - 16:00", "estado": "ASIGNADO",  "especialista": "47485946", "paciente": "54124536" },
            15: { "idturno": 15, "hora_inicio": "16:00", "hora_fin": "16:30", "turno": "16:00 - 16:30", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            16: { "idturno": 16, "hora_inicio": "16:30", "hora_fin": "17:00", "turno": "16:30 - 17:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
            17: { "idturno": 17, "hora_inicio": "17:00", "hora_fin": "17:30", "turno": "17:00 - 17:30", "estado": "RESERVADO", "especialista": "47485946", "paciente": "LIBRE" },
            18: { "idturno": 18, "hora_inicio": "17:30", "hora_fin": "18:00", "turno": "17:30 - 18:00", "estado": "LIBRE",     "especialista": "LIBRE",    "paciente": "LIBRE" },
        }
    }
}