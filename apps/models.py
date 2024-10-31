from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    pin = models.CharField(max_length=6)  # PIN code field
