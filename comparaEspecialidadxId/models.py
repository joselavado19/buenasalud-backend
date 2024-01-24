from django.db import models


class ComparaEspecialidadxId(models.Model):
    periodo = models.CharField(max_length=5)
    total22 = models.FloatField()
    total23 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.periodo} - {self.total22}"

    class Meta:
        db_table = "comparaEspecialidadxId"
