from django.shortcuts import render
from .req import get_characters, get_character_details, get_character_comics, search_hero
import time 


async def home(request):
  characters = await get_characters()

  return render(request, 'characters/home.html', {'characters': characters})


async def character_page(request, id):
  character_info = await get_character_details(id)

  character_comics = await get_character_comics(id)
  context = {
    'character': character_info,
    'comics': character_comics,
    }
  return render(request, 'characters/character_page.html', context)

def search_character(request):
  search_term = request.GET.get('searchTerm').upper()
 
  character = search_hero(search_term)
  return render(request, 'characters/search_page.html', {"character": character})





