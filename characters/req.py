import requests
import os
import datetime
import hashlib
from decouple import config

from .models import Hero



def getUrl():
    '''
        method to return the marvel url
    '''
    ts = datetime.datetime.now()
    ts = str(int(ts.timestamp()))

    public_key = config('PUBLIC_KEY')
    private_key = config('PRIVATE_KEY')

    hash = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()

    base_url = f'https://gateway.marvel.com:443/v1/public/characters?'
    return f'{base_url}ts={ts}&apikey={public_key}&hash={hash}'


def get_heroes():
    ''''
    function to get the json response of the url request
    returns processed results
    '''
    url = getUrl()
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
            hero_object = Hero(id=id, name=name, description=description)
            hero_objects.append(hero_object)
    return hero_objects
