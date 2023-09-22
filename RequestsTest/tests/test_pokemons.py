import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "49fa59775f9f61dad0adc11fc326381c"

def test_get_200():
    response = requests.get(f'{host}/trainers',params={'trainer id' = 1611})
    assert response.status_code == 200


def test_trainers_name():
    response = requests.get(f'{host}/trainers',params={'trainer id' = 1611})
    assert response.json()["trainer_name"] == "Cheese"