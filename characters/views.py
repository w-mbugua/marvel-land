from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator
from .req import get_characters, get_character_details, get_character_comics, search_hero
import time 


async def home(request):
  characters = await get_characters()
  characters = Paginator(characters, 6)
  page_num = request.GET.get('page', 1)
  try:
    page = characters.page(page_num)
  except EmptyPage:
    page = characters.page(1)

  return render(request, 'characters/home.html', {'characters': page})


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





