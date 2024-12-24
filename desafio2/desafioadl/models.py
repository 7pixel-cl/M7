from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255, default="")
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    descripcion = models.CharField(max_length=255, default="")
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')

    def __str__(self):
        return self.descripcion
