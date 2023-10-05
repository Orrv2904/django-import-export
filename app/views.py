from django.shortcuts import render
from .forms import PersonForm
from tablib import Dataset
from .resources import PersonResources
from .models import Person

# Create your views here.
def index(request):
    if request.method == 'POST':
        person_resource = PersonResources()
        dataset = Dataset()
        new_persons = request.FILES['my_file']
        imported_data =  dataset.load(new_persons.read(), format='xlsx')
        for data in imported_data:
            value = Person(
                data[0],
                data[1],
                data[2],
            )
            value.save()
    return render(request, "index.html")