from typing import Dict

import httpx

from src.settings import TEAM_TOKEN


BASE_URL = 'https://datsedenspace.datsteam.dev'
HEADERS = {'X-Auth-Token': TEAM_TOKEN}


def scan_map() -> Dict:
    """ Смотрим карту """

    url = f'{BASE_URL}/player/universe'

    r = httpx.get(url, headers=HEADERS)
    result = r.json()

    return result


def travel(payload) -> Dict:
    """ Перемещение и выгрузка мусора """

    url = f'{BASE_URL}/player/travel'

    r = httpx.post(url, headers=HEADERS, json=payload)
    result = r.json()

    return result


def collect_garbage(payload) -> Dict:
    """ Сборка мусора """
    url = f'{BASE_URL}/player/collect'

    r = httpx.post(url, headers=HEADERS, json=payload)
    result = r.json()

    return result


def reset() -> Dict:
    """ Сброс карты """

    url = f'{BASE_URL}/player/reset'

    r = httpx.delete(url, headers=HEADERS)
    result = r.json()

    return result


def check_rounds() -> Dict:
    """
    Все раунды, время начала и окончания, количество планет и играбельно ли в
    данный момент
    """

    url = f'{BASE_URL}/player/rounds'

    r = httpx.get(url, headers=HEADERS)
    result = r.json()
    return result
