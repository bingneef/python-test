import sqlalchemy as db
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


class DB:
    def __init__(self):
        self.engine = db.create_engine('postgresql://%s:%s@localhost:5432/%s' % (
            os.getenv('POSTGRES_USER'),
            os.getenv('POSTGRES_PASSWORD'),
            os.getenv('POSTGRES_DB')
        ))

    def store(self, data, table_name):
        pd.DataFrame.from_dict(data).to_sql(table_name, self.engine, if_exists='replace')
        return True
    
    def get_all(self, table_name):
        if not db.inspect(self.engine).has_table(table_name):
            return []

        connection = self.engine.connect()

        tables = db.Table(table_name, db.MetaData(), autoload=True, autoload_with=self.engine)

        query = db.select([tables])
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()

        return pd.DataFrame(result_set)
