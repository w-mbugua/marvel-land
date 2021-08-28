from django.urls import path
from .views import home, character_page, search_character

urlpatterns = [ 
  path('', home, name="home"),
  path('<int:id>', character_page, name="character_page"),
  path('search/', search_character, name="search")
]