# UPC - 1FIS0274 Fundamentos de Programación 1 - Trabajo Final

## A. Resumen

El presente proyecto tiene como objetivo el desarrollo de una aplicación de gestión de citas para el consultorio clínico **"El Buen Doctor"**, el cual actualmente presenta deficiencias en la administración de su agenda médica.

La aplicación permitirá centralizar y optimizar el proceso de programación de citas, reemplazando los métodos actuales basados en llamadas telefónicas y mensajes a través de WhatsApp. De esta manera, se busca mejorar la organización, evitar conflictos de horarios y reducir los tiempos de espera tanto para pacientes como para el personal médico.

Asimismo, el sistema facilitará el control de disponibilidad, la correcta asignación de turnos en intervalos definidos (por ejemplo, cada 30 minutos) y la gestión eficiente de reprogramaciones, contribuyendo a elevar la calidad del servicio brindado por el consultorio.

Se asumen una serie de condiciones llamadas "supuestos" para no añadir mayor complejidad al proyecto.

### Integrantes del grupo

| Nombre Completo              | Código Alumno |
|------------------------------|---------------|
| Jorge Luis Mena Salas        | U202616285    |
| Marcelo Valeri Quispe Cruz   | U202619387    |
| Max Harol Cisneros Cabello   | U202520254    |
| Sebastian Paucar Velasquez   | U202617160    |

---

## B. Capítulo 1: Situación Actual

El consultorio clínico **"El Buen Doctor"** presenta deficiencias en la gestión de citas médicas. Actualmente, no cuenta con un proceso estandarizado ni con una herramienta tecnológica que permita administrar las citas de manera eficiente.

La programación de citas se realiza a través de distintos canales, como llamadas telefónicas y mensajes por WhatsApp, lo que genera desorden y falta de control en la agenda.

Debido a la ausencia de un sistema centralizado, el personal no dispone de una visión clara y actualizada de las citas programadas. Como consecuencia, en varias ocasiones se asignan múltiples pacientes en el mismo horario, generando conflictos y tiempos de espera innecesarios.

Asimismo, algunos pacientes olvidan sus citas o solicitan reprogramaciones que no siempre se gestionan adecuadamente, lo que ocasiona pérdida de tiempo tanto para los pacientes como para los profesionales de la salud, afectando la calidad del servicio brindado.

---

## C. Capítulo 2: Propuesta de Innovación

### a. Detalle del nuevo proceso

#### Supuestos

- El consultorio opera de lunes a viernes de 9:00 am a 6:00 pm, y los sábados de 9:00 am a 1:00 pm.
- Cada turno tiene una duración de 30 minutos.
- El consultorio cuenta con un único despacho y atiende un solo médico a la vez.
- La disponibilidad de turnos se gestiona con un enfoque mensual.
- Los datos del especialista deben ser registrados previamente en el sistema antes de asignar turnos.
- Los datos del paciente se registran al momento de agendar la cita, sin necesidad de un registro previo.
- Las citas médicas se generan para el mes.

---

## Estructura del Proyecto

```
sistema-citas-medicas/
├── main.py                     # Menú principal y punto de entrada
├── especialistas.py            # Almacén de datos de especialistas
├── pacientes.py                # Almacén de datos de pacientes
├── turnos.py                   # Almacén de turnos disponibles (junio 2026)
├── registrarEspecialista.py    # Módulo: registro de especialistas
├── registrarPaciente.py        # Módulo: registro de pacientes
├── registrarDisponibilidad.py  # Módulo: disponibilidad del especialista
├── registrarCita.py            # Módulo: registro de citas
└── modificarCita.py            # Módulo: modificar/cancelar citas
```

### Estados de un Turno
 
Cada turno en `turnos.py` tiene un campo `"estado"` que indica su situación actual. Los tres estados posibles son:
 
| Estado | Descripción |
|-----------|-------------|
| `LIBRE` | El turno no tiene especialista asignado. Está disponible para que un especialista registre su disponibilidad. |
| `RESERVADO` | El especialista registró disponibilidad en ese turno, pero aún no hay paciente asignado. Está disponible para agendar una cita. |
| `ASIGNADO` | El turno tiene paciente asignado. La cita está confirmada. La cancelación retorna a asignado.|

### Flujo general del programa

El sistema sigue un orden lógico de uso. Primero se registran los actores (especialista y paciente), luego se configura la agenda y finalmente se gestionan las citas.

```
main.py
    [1] Registrar especialista
    [2] Registrar paciente
    [3] Registrar disponibilidad
    [4] Registrar cita
    [5] Modificar cita
```

#### 1. Registrar especialista — `registrarEspecialista.py`
El especialista es el primer actor que debe existir en el sistema. Se ingresan sus datos personales y profesionales (CMP, RNE, especialidad) y se almacenan en el diccionario `especialistas` usando su DNI como clave.

#### 2. Registrar paciente — `registrarPaciente.py`
El paciente puede registrarse de forma independiente o automáticamente al momento de agendar una cita. Sus datos se guardan en el diccionario `pacientes` con su DNI como clave.

#### 3. Registrar disponibilidad — `registrarDisponibilidad.py`
El especialista indica en qué fechas y turnos estará disponible. El sistema muestra solo las fechas laborables con turnos `LIBRE` y, al confirmar, los cambia a estado `RESERVADO` asignando el DNI del especialista.

#### 4. Registrar cita — `registrarCita.py`
El paciente elige una especialidad y selecciona un turno `RESERVADO` disponible. Al confirmar, el turno pasa a estado `ASIGNADO` y se registra el DNI del paciente en ese turno.

#### 5. Modificar cita — `modificarCita.py`
El paciente puede realizar dos acciones sobre una cita existente:

- **Cancelar:** el turno vuelve a estado `RESERVADO` y queda disponible para otro paciente.
- **Reprogramar:** el turno anterior se libera (`RESERVADO`) y se asigna uno nuevo (`ASIGNADO`) de la misma especialidad.

---

## Material Adicional

## Estructura de Datos: Diccionarios en Python
 
### ¿Qué es un diccionario?
 
Un diccionario es una estructura de datos que almacena pares **clave: valor**. En lugar de acceder a los datos por posición (como en una lista), se accede por una **clave única**.
 
```python
# Sintaxis básica
mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
}
```
 
### Acceder a valores
 
```python
persona = {
    "nombre": "Jorge",
    "edad": 25
}
 
print(persona["nombre"])  # → Jorge
print(persona["edad"])    # → 25
```
 
### Agregar y modificar
 
```python
persona["telefono"] = "999888777"   # agrega nueva clave
persona["edad"] = 26                # modifica valor existente
```
 
### Verificar si una clave existe
 
```python
if "47485946" in especialistas:
    print("Especialista encontrado")
```
 
Exactamente así lo usa el proyecto en `registrarEspecialista.py` y `registrarDisponibilidad.py`.
 
### Diccionarios anidados
 
Un diccionario puede contener otro diccionario como valor. Esto es lo que se usa en `especialistas.py` y `pacientes.py`:
 
```python
# Un especialista es un diccionario dentro del diccionario principal
especialistas = {
    "47485946": {                # clave: el DNI
        "dni"         : "47485946",
        "nombre"      : "Jorge Mena",
        "especialidad": "Medicina General"
    }
}
 
# Para acceder:
especialistas["47485946"]["nombre"]        # → "Jorge Mena"
especialistas["47485946"]["especialidad"]  # → "Medicina General"
```
 
### Tres niveles de anidación
 
El archivo `turnos.py` va un nivel más profundo — diccionario dentro de diccionario dentro de diccionario:
 
```python
turnos_junio = {
    "20260601": {                         # nivel 1: fecha
        "fecha": "01/06/2026",
        "turnos": {
            5: {                          # nivel 2: turno
                "turno"      : "11:00 - 11:30",
                "estado"     : "ASIGNADO",
                "especialista": "47485946",
                "paciente"   : "54124536"
            }
        }
    }
}
 
# Para acceder al estado del turno 5 del 01/06/2026:
turnos_junio["20260601"]["turnos"][5]["estado"]  # → "ASIGNADO"
 
# Para modificarlo (así lo hace modificarCita.py):
turnos_junio["20260601"]["turnos"][5]["estado"]   = "RESERVADO"
turnos_junio["20260601"]["turnos"][5]["paciente"] = "LIBRE"
```
 
### Recorrer un diccionario
 
```python
# .items() te da la clave y el valor a la vez
for dni, especialista in especialistas.items():
    print(dni, especialista["nombre"])
# → 47485946  Jorge Mena
```
 
Así es como se recorre en `registrarCita.py` al buscar especialistas por especialidad.
 
---
 
> **Nota:** Toda la "base de datos" del proyecto son diccionarios anidados. Las operaciones del sistema (registrar, buscar, modificar) son simplemente lecturas y escrituras sobre esas estructuras.