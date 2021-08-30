import requests
import datetime
import hashlib
from decouple import config
import aiohttp
import asyncio

from .models import Hero, Comic


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


async def get_characters():
    ''''
    function to get the json response of the url request
    returns processed results
    '''
    url = f'{base_url}?orderBy=-name&limit=30&{getUrl()}'
    hero_results = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            resp = await data.json()

            if resp.get('data')['results']:
                hero_results = resp.get('data')['results']
    return await process_characters(hero_results)
     

async def process_characters(results):
    '''
    function that processes the api results and converts them to a list
    '''
    hero_objects = []
    for hero in results:
            id = hero.get('id')
            name = hero.get('name')
            description = hero.get('description')
            thumbnail = hero.get('thumbnail')
            urls = hero.get('urls')
            image_check = thumbnail['path'].endswith('image_not_available')
            # check if the character has a description and image
            if description and not image_check:
                image_path = f"{thumbnail['path']}/portrait_uncanny.{thumbnail['extension']}"
                hero_link = ''
                for url in urls:
                    
                    if url['type'] == 'wiki':
                        hero_link = url['url']
                hero_object = Hero(id=id, name=name, description=description, image_path=image_path, link=hero_link)
                hero_objects.append(hero_object)
    return hero_objects[3:]


async def get_character_details(character_id):
    '''
    function to retrieve a single character and their details from the
    list of already retrieved heroes
    '''
    character_details = {}
    characters = await get_characters()
    for character in characters:
        if character.id == character_id:
            character_details['id'] = character_id
            character_details['name'] = character.name
            character_details['description'] = character.description
            character_details['image_path'] = character.image_path
            character_details['link'] = character.link
    return character_details


async def get_character_comics(character_id):
    '''
    function to retrieve comics per character
    '''
    global base_url
    url = f'{base_url}/{character_id}/comics?{getUrl()}'
    comic_results = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            response = await data.json()
    
            # if the character has comics go ahead and process else return None
            if len(response['data'].get('results')) > 0:
                comic_results = response['data'].get('results')
                return await process_comics(comic_results)
            else:
                return comic_results

async def process_comics(results):
    '''
    function to process comics response and return a list
    '''
    comic_list = []
    for item in results:
        id = item.get('id')
        title = item.get('title')
        description = item.get('description')
        image_path = item.get('thumbnail')

        if description:
            image_path = f"{image_path['path']}/portrait_uncanny.{image_path['extension']}"
            comic = Comic(id=id, title=title, description=description, image_path=image_path)
            comic_list.append(comic)
    return comic_list

def search_hero(name):
    global base_url
    url = f"{base_url}?name={name}&{getUrl()}"
    data = requests.get(url)
    response = data.json()
    # print(response)
    hero = {}

    # process the json reponse
    if response['status'] == "Ok":
        results = response['data'].get('results')[0]
        id = results.get('id')
        name = results.get('name')
        description = results.get('description')
        thumbnail = results.get('thumbnail')
        urls = results.get('urls')

        image_path = f"{thumbnail['path']}/portrait_uncanny.{thumbnail['extension']}"
        hero_link = ''
        for url in urls:
            if url['type'] == 'wiki':
                hero_link = url['url']
        hero = Hero(id=id, name=name, description=description, image_path=image_path, link=hero_link)
    return hero
    








