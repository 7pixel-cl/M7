from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    """Retorna un arreglo que contiene todas las tareas y sus subtareas asociadas."""
    tareas = Tarea.objects.filter(eliminada=False)
    resultado = []
    
    for tarea in tareas:
        tarea_dict = {
            'id': tarea.id,
            'descripcion': tarea.descripcion,
            'subtareas': []
        }
        for subtarea in tarea.subtareas.filter(eliminada=False):
            tarea_dict['subtareas'].append({
                'id': subtarea.id,
                'descripcion': subtarea.descripcion
            })
        resultado.append(tarea_dict)
    
    return resultado

def crear_nueva_tarea(descripcion):
    """Crea una nueva tarea y retorna todas las tareas con sus subtareas."""
    try:
        Tarea.objects.create(descripcion=descripcion, eliminada=False)
        return recupera_tareas_y_sub_tareas()
    except Exception as e:
        print(f"Error al crear tarea: {str(e)}")
        return []

def crear_sub_tarea(tarea_id, descripcion):
    """Crea una subtarea relacionada con una tarea específica."""
    try:
        tarea = Tarea.objects.get(id=tarea_id, eliminada=False)
        SubTarea.objects.create(descripcion=descripcion, tarea=tarea, eliminada=False)
        return recupera_tareas_y_sub_tareas()
    except Tarea.DoesNotExist:
        print(f"No se encontró la tarea con ID {tarea_id}")
        return []
    except Exception as e:
        print(f"Error al crear subtarea: {str(e)}")
        return []

def elimina_tarea(tarea_id):
    """Elimina (marca como eliminada) una tarea específica y sus subtareas asociadas."""
    try:
        tarea = Tarea.objects.get(id=tarea_id, eliminada=False)
        tarea.eliminada = True
        tarea.save()
        # Marcar todas las subtareas como eliminadas
        tarea.subtareas.all().update(eliminada=True)
        return recupera_tareas_y_sub_tareas()
    except Tarea.DoesNotExist:
        print(f"No se encontró la tarea con ID {tarea_id}")
        return []
    except Exception as e:
        print(f"Error al eliminar tarea: {str(e)}")
        return []

def elimina_sub_tarea(sub_tarea_id):
    """Elimina (marca como eliminada) una subtarea específica."""
    try:
        subtarea = SubTarea.objects.get(id=sub_tarea_id, eliminada=False)
        subtarea.eliminada = True
        subtarea.save()
        return recupera_tareas_y_sub_tareas()
    except SubTarea.DoesNotExist:
        print(f"No se encontró la subtarea con ID {sub_tarea_id}")
        return []
    except Exception as e:
        print(f"Error al eliminar subtarea: {str(e)}")
        return []

def imprimir_en_pantalla(arreglo):
    """Imprime las tareas y subtareas en un formato jerárquico."""
    for tarea in arreglo:
        print(f"[{tarea['id']}] {tarea['descripcion']}")
        for subtarea in tarea['subtareas']:
            print(f"    .... [{subtarea['id']}] {subtarea['descripcion']}") 