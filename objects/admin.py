from django.contrib import admin
from .models import Lpu, Object, Error, Documents
# Register your models here.

admin.site.register(Object)
admin.site.register(Lpu)
admin.site.register(Error)
admin.site.register(Documents)