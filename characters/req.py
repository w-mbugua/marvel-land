import requests
import os
import datetime
import hashlib
from decouple import config

from .models import Hero


base_url = 'https://gateway.marvel.com:443/v1/public/characters'

def getUrl():
    '''
        method to return the base marvel url
    '''
    global base_url
    ts = datetime.datetime.now()
    ts = str(int(ts.timestamp()))

    public_key = config('PUBLIC_KEY')
    private_key = config('PRIVATE_KEY')

    hash = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
    return f'ts={ts}&apikey={public_key}&hash={hash}'


def get_characters():
    ''''
    function to get the json response of the url request
    returns processed results
    '''
    url = f'{base_url}?orderBy=-name&limit=100&{getUrl()}'
    data = requests.get(url)
    resp = data.json()
    
    hero_results = None
    if resp.get('data')['results']:
        hero_results = resp.get('data')['results']
    return process_characters(hero_results)
     

def process_characters(results):
    '''
    function that processes the api results and converts them to a list
    '''
    hero_objects = []
    for hero in results:
            id = hero.get('id')
            name = hero.get('name')
            description = hero.get('description')
            thumbnail = hero.get('thumbnail')
            image_check = thumbnail['path'].endswith('image_not_available')
            # check if the character has a description and image
            if description and not image_check:
                image_path = f"{thumbnail['path']}/portrait_uncanny.{thumbnail['extension']}"
                hero_object = Hero(id=id, name=name, description=description, image=image_path)
                hero_objects.append(hero_object)
    return hero_objects


def get_character_details(character_id):
    global base_url
    url = f'{base_url}/{character_id}?{getUrl()}'
    data = requests.get(url)
    response = data.json()

    detail_results = None
    if response['data'].get('results'):
        detail_results = response['data'].get('results')




def get_character_comics(character_id):
    global base_url
    url = f'{base_url}/{character_id}/comics?{getUrl()}'
    data = requests.get(url)
    response = data.json()

    comic_results = None
    if response['data'].get('results'):
        comic_results = response['data'].get('results')





