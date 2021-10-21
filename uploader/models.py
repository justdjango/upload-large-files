from django.db import models


class UploadFile(models.Model):
    file = models.FileField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
