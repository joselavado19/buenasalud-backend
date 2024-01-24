from django.db import models


class ListEspecialidad(models.Model):
    especialidad = models.CharField(max_length=25)
    diminutivo =models.CharField(max_length=5)
    flag = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.especialidad} - {self.diminutivo}"

    class Meta:
        db_table = "listEspecialidad"
