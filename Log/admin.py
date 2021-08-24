from django.contrib import admin

# Register your models here.
from Log.models import BDAdata, Book
from Log.models import Account

admin.site.register(BDAdata)
admin.site.register(Account)
admin.site.register(Book)