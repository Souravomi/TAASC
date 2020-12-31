from django.contrib import admin
from .models import BasicDetails
from .models import FamilyMembers
from .models import DomesticAnimals
from .models import VegFru
from .models import Fish
from .models import Rubber
from .models import Survey

# Register your models here.
admin.site.register(BasicDetails)
admin.site.register(FamilyMembers)
admin.site.register(DomesticAnimals)
admin.site.register(VegFru)
admin.site.register(Fish)
admin.site.register(Rubber)
admin.site.register(Survey)