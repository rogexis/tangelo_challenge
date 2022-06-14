import requests

class RestCountries:
    """
        Consumo de API de https://restcountries.com en v3.1
    """
    def __init__(self):
        self.url = 'https://restcountries.com/v3.1/'

    def countryByName(self, name):
        """
            Obtenemos datos buscando directamente el nombre del país
        """
        getCountryInfo = requests.get(self.url+f"name/{str(name).lower()}").json()
        if type(getCountryInfo) is list:
            return getCountryInfo[0]
        else:
            return {"message": f"Country > {name} < Not Found"}