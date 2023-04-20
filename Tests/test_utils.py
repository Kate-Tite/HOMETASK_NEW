from utils import filter_sort, load_data, format_date, mask_card, formatted_data


def test_load_data():
    list_ = [
              {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }
            ]
    assert load_data('test.json') == list_


def test_filter_sort():
    list_ = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2019-11-29T07:18:23.941293'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        }
    ]
    sorted_list = [
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        },
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        },
    ]
    assert filter_sort(list_) == sorted_list

def test_format_date():
    assert format_date('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert format_date('2018-08-19T04:27:37.904916') == '19.08.2018'

def test_mask_card():
    assert mask_card('Счет 44812258784861134719') == 'Счет **4719'
    assert mask_card('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert mask_card('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'

def test_formatted_data():
    dict_ =  {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }
    str_ = '26.08.2019 Перевод организации\n' \
           'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
           '31957.58 руб.\n'
    assert formatted_data(dict_) == str_