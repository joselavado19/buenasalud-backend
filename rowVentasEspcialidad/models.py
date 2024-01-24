from django.db import models


class RowVentasEspcialidad(models.Model):
    total = models.FloatField()
    cantidad = models.PositiveIntegerField()
    especialidad = models.CharField(max_length=5)
    id_especialidad = models.PositiveIntegerField()
    deltaType = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.total} - {self.cantidad}"

    class Meta:
        db_table = "rowVentasEspcialidad"
