import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '3ca4b4f15bbecca1f0cf7aef39736cf4'
HEADERS = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 184})
    assert response.status_code == 200

def test_trainers_name():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 184})
    assert response.json()['data'][0]['trainer_name'] == 'Елисей'