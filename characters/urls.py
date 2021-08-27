from django.urls import path
from .views import home, character_page

urlpatterns = [ 
  path('', home, name="home"),
  path('<int:id>', character_page, name="character_page")
]