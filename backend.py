# backend.py
# Lógica de negocio: valida y procesa tareas

from database import guardar_tarea

def procesar_tarea(nombre_tarea):
    """
    Valida la tarea y la guarda si es válida.
    """
    if not nombre_tarea or not nombre_tarea.strip():
        return "Error: la tarea no puede estar vacía."  # Seguridad: valida entrada.

    nombre_tarea = nombre_tarea.strip()
    guardar_tarea(nombre_tarea)
    return f"Tarea guardada: {nombre_tarea}"

# Escalabilidad: Puede crecer con reglas adicionales, prioridades, etc.
# Mantenibilidad: Está desacoplado del frontend, facilitando el cambio.
