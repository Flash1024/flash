from django.db import models
PROJ_TYPE = (
    ("web", "Web"),
    ("app", "App"),
)

class Contact(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=40, null=True, blank=True)
    desc = models.TextField(max_length=400, null=True)
    date = models.DateField()

    def __str__(self):
            return self.name

class Review(models.Model):
    person_name = models.CharField(max_length=120, null=True, blank=True)
    jobpost = models.CharField(max_length=120, null=True, blank=True)
    review = models.TextField(max_length=250, null=True)
    image = models.ImageField(upload_to='review/images', default="")

    def __str__(self):
            return self.person_name

class Service(models.Model):
    service_name = models.CharField(max_length=120, null=True, blank=True)
    service_desc = models.TextField(max_length=250, null=True)
    
    def __str__(self):
            return self.service_name

class Portfolio(models.Model):
    project_name = models.CharField(max_length=120, null=True, blank=True)
    project_link = models.URLField(max_length=750, blank=True)
    project_thumbnail = models.ImageField(upload_to='portfolio/images', default="")
    project_type = models.CharField(max_length=20, choices= PROJ_TYPE, default="web")
    
    def __str__(self):
            return self.project_name