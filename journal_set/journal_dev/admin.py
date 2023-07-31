from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import journal
# Register your models here.
#from import_export.admin import ImportExportModelAdmin


class RegisterJournal(admin.ModelAdmin):
    list_display = [ 'npp', 'dateReg','content','executor']

admin.site.register(journal,RegisterJournal)
