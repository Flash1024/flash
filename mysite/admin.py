from django.contrib import admin
from mysite.models import Contact, Review, Service, Portfolio

# Register your models here.
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Portfolio)