from django.db import models

# Create your models here.


class Document(models.Model):
        document_name = models.CharField(max_length=100)
        document_year = models.DateTimeField('date published')
        document_abstract = models.CharField(max_length=1000)
        document_journal = models.CharField(max_length=50)
        document_authors = models.CharField(max_length=50)