from django.db import models


class Zapp(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    zap_definition_language = models.JSONField(default=dict)

    def __str__(self):
        return self.name
