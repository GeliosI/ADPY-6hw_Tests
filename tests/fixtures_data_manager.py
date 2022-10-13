import pytest
from src.data_manager import DataManager


@pytest.fixture
def init_documents():
    yield [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

@pytest.fixture
def init_directories():
    yield {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }       

@pytest.fixture(autouse=True)
def setup_fixture(request, init_documents, init_directories):
    request.cls.dm = DataManager(init_documents, init_directories)


FIXTURES_ADD_DOCUMENTS = [
    ('123123', 'passport', 'Вася', '1', True),
    ('2207 876234', 'passport', 'Василий Гупкин', '1', False),
    ('', '', '', '3', False),
    ('123123', 'passport', 'Вася', '5', False)     
]

FIXTURES_ADD_SHELF = [
    ('4', True),
    ('-1', False),
    ('3', False)
]

FIXTURES_DEL_DOC_BY_NUMBER = [
    ('2207 876234', True),
    ('', False),
    ('-1', False)
]

FIXTURES_MOVE_DOC = [
    ('11-2', '2', True),
    ('1212', '1', False),
    ('11-2', '0', False),
    ('1212', '5', False)  
]