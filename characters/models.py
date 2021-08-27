from django.db import models

# Create your models here.
class Hero:
    '''
      class to define character objects
    '''
    def __init__(self, id, name, description):
      self.id = id
      self.name = name
      self.description = description
