from django.shortcuts import render
from django.http import HttpResponse
from .req import get_characters, get_character_details, get_character_comics

# Create your views here.
def home(request):
  characters = get_characters()[3:]
  return render(request, 'home.html', {'characters': characters})


def character_page(request, id):
  character_info = get_character_details(id)
  character_comics = get_character_comics(id)
  context = {
    'character': character_info,
    'comics': character_comics,
    }
  return render(request, 'character_page.html', context)


