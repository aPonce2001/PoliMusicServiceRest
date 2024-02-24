from sqlalchemy import create_engine, MetaData

engine = create_engine("mssql+pyodbc://usr_polimusic:usr_polimusic@localhost:1433/BDD_PoliMusic?driver=ODBC+Driver+17+for+SQL+Server")
meta = MetaData()
conn = engine.connect()
