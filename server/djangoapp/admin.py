from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "type"]
    list_filter = ["year"]
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
