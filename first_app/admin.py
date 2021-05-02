from django.contrib import admin
from first_app.models import Asset,Task,Worker
# Register your models here.
admin.site.register(Asset)
admin.site.register(Task)
admin.site.register(Worker)
