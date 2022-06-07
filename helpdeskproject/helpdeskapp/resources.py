from import_export import resources
from .models import AddTicket

class PersonResource(resources.ModelResource):
    class Meta:
        model = AddTicket