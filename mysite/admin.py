from django.contrib import admin
from .models import About, Review, Portfolio, Contact, ContactInfo

# Register your models here.
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Portfolio)
admin.site.register(ContactInfo)