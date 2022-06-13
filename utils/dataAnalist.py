import pandas as pd
from sqlalchemy import create_engine


class DataAnalist:
    def __init__(self, cols):

        self.df = pd.DataFrame(columns=cols)
    
    def appendRow(self, row=dict):
        self.df = self.df.append(row, ignore_index=True)
        return 'Row added'
        
    def dataFrameToJson(self, dir='./storage/', fileName='data'):

        self.df.to_json(f"{dir}{fileName}.json")
    
    def dataFrameToSql(self, dir='database/Database.db', tableName='countries_languages'):
        """
        dir path to database
        """
        engine = create_engine(f'sqlite:///{dir}', echo=False)
        self.df.to_sql(tableName, con=engine, if_exists='replace', index_label='id')

        return 'Tabla creada correctamente'

    
    def showStats(self):
                
        print(self.df)
        #print(self.df.describe())
        print()
        print(self.df.max(numeric_only=True))
        print(self.df.min(numeric_only=True))
        print(self.df.mean(numeric_only=True))
