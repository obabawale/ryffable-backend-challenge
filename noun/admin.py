from django.contrib import admin
from .models import Noun, Place, Animal, Thing, Food

# Register your models here.
admin.site.register(Noun)
admin.site.register(Place)
admin.site.register(Animal)
admin.site.register(Thing)
admin.site.register(Food)