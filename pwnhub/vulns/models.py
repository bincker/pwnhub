from django.db import models
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class VulnerabilityType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Signature(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    vuln_type = models.ForeignKey(VulnerabilityType)
    grep_line = models.CharField(max_length=10000) #TODO: come up with a more suitable length...

    def __unicode__(self):
        return self.name

class Vulnerability(models.Model):
    line_number = models.IntegerField()
    vuln_signature = models.ForeignKey(Signature)

    def __unicode__(self):
        return self.vuln_signature.vuln_type.name + ": " + self.vuln_signature.name

class Repo(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255) #TODO: add model for owner?
    url = models.URLField()
    vulnerabilities = models.ManyToManyField(Vulnerability)

    def __unicode__(self):
        return self.name
