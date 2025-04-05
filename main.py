

from frontend import mostrar_formulario

if __name__ == "__main__":
    while True:
        mostrar_formulario()
        continuar = input("\n¿Agregar otra tarea? (s/n): ").lower()
        if continuar != 's':
            break
