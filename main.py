import time
from utils.requestAPI import RestCountries
from config import countries, dataFrameCols, newData
from utils.dataAnalist import DataAnalist as da
from utils.cryptographicHash import CryptographicHash as CH

#   Iniciamos un objeto para crear el DataFrame base 
dataFrame = da(dataFrameCols)

#   Iteramos la lista de países a consultar (Que se encuentra como una lista en el archivo config.py)
for ct in countries:

    #   Iniciamos el temporizador
    st = time.time()

    #   Iniciamos el objeto para consultar la API de https://restcountries.com/
    reqOb = RestCountries()

    #   Consultamos el país y verificamos la respuesta del metodo.
    rslt = reqOb.countryByName(ct)
    if 'message' in rslt.keys():
        print(rslt)
        continue

    #   Inicializamos un objeto para la encriptacion del lenguaje
    objetoCH = CH("sha1")
    language = rslt['languages'][list(rslt['languages'])[0]]
    EncryptedData = objetoCH.encrypt(language)

    #   Actualizamos las claves del diccionario para agregar la nueva fila al DataFrame
    newData['Region'] = rslt['region']
    newData['Country name'] = rslt['name']['common']
    newData['Language'] = EncryptedData
    newData['Time (ms)'] = round((time.time()-st)*1000, 2)
    dataFrame.appendRow(newData)

# Mostramos por consola Info Relevante del DataFrame
dataFrame.showStats()

#Salvamos el DataFrame como Json y en SQLite
dataFrame.dataFrameToJson() 
dataFrame.dataFrameToSql()