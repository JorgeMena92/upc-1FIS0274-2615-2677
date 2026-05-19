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