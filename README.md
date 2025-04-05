# Mini App de Tareas

Este proyecto simula una aplicación de tareas con arquitectura en tres capas:

- **Frontend**: Simulado por consola (formulario de texto).
- **Backend**: Lógica de validación y procesamiento.
- **Base de datos**: Lista en memoria.

---

## 💡 Características

- **Escalabilidad**: Cada capa está separada, lista para crecer (ej: base de datos real, interfaz web, API REST).
- **Mantenibilidad**: Cambiar un componente no afecta a los otros.
- **Seguridad**: Validación de entrada para evitar tareas vacías.

---

## ▶️ Cómo ejecutar

```bash
python main.py
```

---

## 📂 Estructura

```
database.py   # Simula base de datos
backend.py    # Lógica de negocio
frontend.py   # Interfaz en consola
main.py       # Punto de entrada
```
