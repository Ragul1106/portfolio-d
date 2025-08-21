from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title
