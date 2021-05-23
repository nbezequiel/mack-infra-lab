from converter import CurrencyResponse, CurrencyService


class ConverterService():

    def __init__(self):
        self._value = None
        self._bases = {'USD': 'dolar', 'EUR': 'euro'}
        self._currency_service = CurrencyService()

    def convert(self, brl_value: float) -> CurrencyResponse:
        result = CurrencyResponse(brl_value)

        for base, name in self._bases.items():
            value = self._get_value(brl_value, base)
            result.converted.update({name: value})

        return result

    def _get_value(self, brl_value, base):
        base_value = self._currency_service.fetch(base)
        converted = float(brl_value) * float(base_value)
        return format(round(converted, 2))
