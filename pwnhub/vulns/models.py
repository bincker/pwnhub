from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)

class Signature(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    grep_line = models.CharField(max_length=10000) #TODO: come up with a more suitable length...

class Vulnerability(models.Model):
    line_number = models.IntegerField()
    vuln_type = models.ForeignKey(Signature)

class Repo(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255) #TODO: add model for owner?
    url = models.URLField()
    vulnerability = models.ManyToManyField(Vulnerability)


