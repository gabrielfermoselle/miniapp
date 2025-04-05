

tareas = []

def guardar_tarea(nombre):
    """Guarda una tarea en la lista simulada."""
    tareas.append(nombre)

def obtener_tareas():
    """Devuelve la lista de tareas guardadas."""
    return tareas

# Escalabilidad: Se puede reemplazar fácilmente por una base de datos real.
# Mantenibilidad: Separar el acceso a datos facilita los cambios futuros.
