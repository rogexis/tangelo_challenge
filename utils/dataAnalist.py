import pandas as pd
from sqlalchemy import create_engine


class DataAnalist:
    """
        Esta clase sirve para facilitar aun más el uso de la paquetería Pandas
    """
    def __init__(self, cols):
        """
            Inicializamos un dataFrame vacío
        """
        self.df = pd.DataFrame(columns=cols)
        self.ms = []
    
    def appendRow(self, row=dict):
        """
            Agregamos una fila al dataFrame enviando como parametro un diccionario con los elementos de la fila
        """
        self.df = self.df.append(row, ignore_index=True)
        return 'Row added'
        
    def dataFrameToJson(self, dir='./storage/', fileName='data'):
        """
            Guardamos el dataFrame como un archivo Json
        """
        self.df.to_json(f"{dir}{fileName}.json")
    
    def dataFrameToSql(self, dir='database/Database.db', tableName='countries_languages'):
        """
            Creamos una tabla en SQLite donde almacenamos el contenido del data frame
        """
        engine = create_engine(f'sqlite:///{dir}', echo=False)
        self.df.to_sql(tableName, con=engine, if_exists='replace', index_label='id')

        return 'Tabla creada correctamente'

    
    def showStats(self):
        """
            Mostramos estadisticas del dataFrame
        """     
        print(self.df)
        #print(self.df.describe())
        print()
        print("Tiempo Total", self.df.sum(numeric_only=True))
        print("Tiempo Máximo", self.df.max(numeric_only=True))
        print("Tiempo Mínimo", self.df.min(numeric_only=True))
        print("Tiempo Promedio", self.df.mean(numeric_only=True))