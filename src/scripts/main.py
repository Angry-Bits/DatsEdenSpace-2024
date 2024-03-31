# !usr/bin/env python3

import httpx

from src.logger import logger
from src.settings import TEAM_TOKEN


def main(url: str = 'https://www.google.ru/') -> None:
    """Request checking script."""
    page = httpx.get(url)
    logger.info(f'Выполнен запрос на {url}')
    if TEAM_TOKEN:
        logger.info('Введен секретный токен.')
    else:
        logger.info(
            ('Вы не ввели секретный токен! '
            'Заполните его и повторите попытку.')
        )
        return
    if page.status_code:
        logger.info('К хакатону готовы!')
    else:
        logger.info(
            ('Ответ на запрос не получен. '
            'Убедитесь в корректности адреcа запрашиваемого ресурса.')
        )


if __name__ == '__main__':
    main()
