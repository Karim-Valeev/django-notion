from django.contrib import admin

from .models import Note
from .models import User

admin.site.register(User)
admin.site.register(Note)
