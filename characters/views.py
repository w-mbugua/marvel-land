from django.shortcuts import render
from django.http import HttpResponse
from .req import get_characters, get_character_details, get_character_comics, search_hero
import time 


async def home(request):
  start = time.time()
  characters = await get_characters()
  end = time.time() -start 
  print("Time",characters)
  return render(request, 'home.html', {'characters': characters})


async def character_page(request, id):
  character_info = await get_character_details(id)

  character_comics = await get_character_comics(id)
  context = {
    'character': character_info,
    'comics': character_comics,
    }
  return render(request, 'character_page.html', context)

def search_character(request):
  search_term = request.GET.get('searchTerm').upper()
 
  character = search_hero(search_term)
  return render(request, 'search_page.html', {"character": character})





