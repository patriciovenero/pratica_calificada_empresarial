from django.db import models

# Create your models here.
class pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publised')


    def __str__(self):
        return self.pregunta

class respuesta(models.Model):
    pregunta1 = models.ForeignKey(pregunta,on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=200)
    valor = models.IntegerField(default=1)

    def __str__(self):
        return self.opcion_texto
