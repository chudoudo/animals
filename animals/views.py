from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from dataclasses import dataclass

# Create your views here.

animal_dict = {
    'dogs': "The dog is a domesticated descendant of the wolf.",
    'cats': "The cat is a domesticated species of small carnivorous mammal.",
    'horses': "The horse is a domesticated, one-toed, hoofed mammal.",
    'snakes': "The snake is a reptile with a long, thin body but no legs."
}


def index(request):
    types = list(animal_dict)
    li_elements = ''
    # f"<li> <a href = '{redirect_path}'>{i.title()}</a> </li>"
    context = {
        'types': types
    }
    return render(request, 'animals/index.html', context=context)


@dataclass
class Type:
    breed: str
    age: int

    def __str__(self):
        return f'This is {self.breed}'


def get_list_of_the_animal(request, animal_type: str):
    description = animal_dict.get(animal_type)
    data = {
        'description_animal': description,
        'animal_type': animal_type,
    }
    return render(request, 'animals/info_animal.html', context=data)
