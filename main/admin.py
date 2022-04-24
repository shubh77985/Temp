from django.contrib import admin
from main.models import Contact, Feedback
from main.models import User

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Feedback)