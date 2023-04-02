import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formated_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert (len(get_filtered_data(test_data, filtered_empty_from=True, filtered_empty_date=True))) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    assert ([x['date'] for x in data]) == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']


def test_get_formated_data(test_data):
    data = get_formated_data(test_data[1:2])
    assert (data) == [
        '\n        03.07.2019 Перевод организации\n        Maestro 1596 83** **** 5199 -> Счет **9589\n        8221.37 USD\n        '
    ]
