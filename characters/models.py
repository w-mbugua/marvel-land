from django.db import models

# Create your models here.
class Hero:
    '''
      class to define character objects
    '''
    def __init__(self, id, name, description, image):
      self.id = id
      self.name = name
      self.description = description
      self.image = image
