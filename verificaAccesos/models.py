from django.db import models

# Create your models here.
from django.db import models


class VerificaAccesos(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nombre_usuario =models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "verificaAccesos"