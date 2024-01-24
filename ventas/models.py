from django.db import models


class Ventas(models.Model):
    title = models.CharField(max_length=200)
    metric = models.FloatField()
    progress = models.FloatField()
    target = models.FloatField()
    delta = models.FloatField()
    deltaType = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.title} - {self.metric}"

    class Meta:
        db_table = "ventas"