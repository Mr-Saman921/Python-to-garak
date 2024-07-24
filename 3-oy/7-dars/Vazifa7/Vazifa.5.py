import requests

class Converter:
    @staticmethod
    def get_exchange_rates():
        url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
        response = requests.get(url)
        data = response.json()
        for rate in data:
            if rate['Ccy'] == 'USD':
                return float(rate['Rate'])

    @staticmethod
    def usd_to_uzs(usd_amount):
        rate = Converter.get_exchange_rates()
        uzs_amount = usd_amount * rate
        return uzs_amount

    @staticmethod
    def uzs_to_usd(uzs_amount):
        rate = Converter.get_exchange_rates()
        usd_amount = uzs_amount / rate
        return usd_amount

usd_amount = 100
uzs_amount = Converter.usd_to_uzs(usd_amount)
print(f"{usd_amount} USD = {uzs_amount} UZS")

uzs_amount = 1000000
usd_amount = Converter.uzs_to_usd(uzs_amount)
print(f"{uzs_amount} UZS = {usd_amount} USD")
