from django.contrib import admin
from .models import Articles, Author
# Register your models here.

admin.site.register(Articles)
admin.site.register(Author)