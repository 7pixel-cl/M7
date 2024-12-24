# Proyecto de Administración de Tareas y Subtareas

Este proyecto Django implementa un sistema de administración de tareas y subtareas con las siguientes funcionalidades:

## Funcionalidades

- Creación de tareas
- Creación de subtareas asociadas a tareas específicas
- Eliminación lógica de tareas (soft delete)
- Eliminación lógica de subtareas
- Recuperación de tareas y subtareas activas
- Visualización jerárquica de tareas y subtareas

## Estructura del Proyecto

- `desafio2/`: Directorio principal del proyecto Django
  - `desafioadl/`: Aplicación principal
    - `models.py`: Define los modelos Tarea y SubTarea
    - `services.py`: Implementa la lógica de negocio

## Modelos

### Tarea
- id: AutoField (Primary Key)
- descripcion: CharField(max_length=255)
- eliminada: BooleanField(default=False)

### SubTarea
- id: AutoField (Primary Key)
- descripcion: CharField(max_length=255)
- eliminada: BooleanField(default=False)
- tarea: ForeignKey(Tarea)

## Servicios Implementados

1. `recupera_tareas_y_sub_tareas()`: Retorna todas las tareas activas con sus subtareas
2. `crear_nueva_tarea(descripcion)`: Crea una nueva tarea
3. `crear_sub_tarea(tarea_id, descripcion)`: Crea una subtarea asociada a una tarea
4. `elimina_tarea(tarea_id)`: Realiza eliminación lógica de una tarea y sus subtareas
5. `elimina_sub_tarea(sub_tarea_id)`: Realiza eliminación lógica de una subtarea
6. `imprimir_en_pantalla(arreglo)`: Muestra las tareas y subtareas en formato jerárquico

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Aplicar migraciones:
```bash
python manage.py migrate
```

## Uso

El proyecto puede ser utilizado a través de la Django shell:

```python
from desafioadl.services import *

# Crear una tarea
resultado = crear_nueva_tarea("Mi primera tarea")

# Crear una subtarea
crear_sub_tarea(1, "Mi primera subtarea")

# Obtener todas las tareas y subtareas
tareas = recupera_tareas_y_sub_tareas()

# Mostrar tareas en pantalla
imprimir_en_pantalla(tareas)
``` 