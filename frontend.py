# frontend.py
# Simulación de frontend vía consola

from backend import procesar_tarea
from database import obtener_tareas

def mostrar_formulario():
    """Simula una interfaz de ingreso de tareas por consola."""
    print("=== Mini App de Tareas ===")
    tarea = input("Ingresá una tarea: ")
    mensaje = procesar_tarea(tarea)
    print(mensaje)

    print("\nTareas actuales:")
    for t in obtener_tareas():
        print(f"- {t}")

# Escalabilidad: Puede ser reemplazado por una interfaz web.
# Mantenibilidad: Se actualiza sin afectar la lógica ni el almacenamiento.
# Seguridad: En una interfaz real, se validaría en cliente y servidor.
