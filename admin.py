from django.contrib import admin

# Register your models here.

from .models import defi, bookMark, catego
admin.site.register(defi)
admin.site.register(bookMark)
admin.site.register(catego)
