import requests
from celery import shared_task, chain

# Create a task in order to parse currency rates.
from home.models import Currency


@shared_task
def pars_private():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    return response.json()


# Create a task to save currency rates to the "models".
@shared_task
def save_pars_private(currencies):
    for currency in currencies:
        currency_instance = Currency()

        currency_instance.ccy = currency['ccy']
        currency_instance.base_ccy = currency['base_ccy']
        currency_instance.buy = currency['buy']
        currency_instance.sale = currency['sale']

        currency_instance.save()


# Create a task to execution of tasks sequentially.
@shared_task
def chain_pars_private():
    return chain(pars_private.s(), save_pars_private.s())()
