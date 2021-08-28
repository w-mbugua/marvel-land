from django.shortcuts import render
from django.http import HttpResponse
from .req import get_characters, get_character_details, get_character_comics, search_hero

# Create your views here.
def home(request):
  characters = get_characters()[3:]
  return render(request, 'home.html', {'characters': characters})


def character_page(request, id):
  character_info = get_character_details(id)
  print("character",character_info)
  character_comics = get_character_comics(id)
  print("comics",character_comics)
  context = {
    'character': character_info,
    'comics': character_comics,
    }
  return render(request, 'character_page.html', context)

def search_character(request):
  search_term = request.GET.get('searchTerm').upper()
  print(search_term)
  character = search_hero(search_term)
  return render(request, 'search_page.html', {"character": character})





