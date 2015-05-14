from django.db import models


class ChatJSON(models.Model):
    script = models.FileField 
    version = models.DecimalField(max_digits=6, decimal_places=2)
