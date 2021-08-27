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


class Comic:
  '''
    class to define a character's comics
  '''
  def __init__(self, id, title, description, image_path):
    self.id = id
    self.title = title
    self.description = description
    self.image_path = image_path
