import configparser
import pytest

from src.yandex_disk import YandexDisk


@pytest.fixture
def get_token():
    config = configparser.ConfigParser()
    config.read('tests/tokens.ini')
    yield config['YandexDisk']['token']

@pytest.fixture(autouse=True)
def setup_fixture(request, get_token):
    request.cls.dm = YandexDisk(get_token)

FIXTURES_CREATE_DIR = [
    ('123123', 201, 200),
    ('test', 201, 200),
    (f'{"test"*1000}', 404, 404)    
]