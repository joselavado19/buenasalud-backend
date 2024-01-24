from django.db import models


class GridVentasCompara(models.Model):
    total = models.FloatField()
    periodo = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.total} - {self.periodo}"

    class Meta:
        db_table = "gridVentasCompara"
