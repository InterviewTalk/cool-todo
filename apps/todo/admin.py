from django.contrib import admin
from .models import Todo

# add our model to the admin site
admin.site.register(Todo)