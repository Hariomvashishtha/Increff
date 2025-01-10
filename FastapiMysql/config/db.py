from sqlalchemy import create_engine , MetaData
meta = MetaData()
engine =create_engine("mysql+pymysql://root:Hariom%402004@localhost:3306/fastapi_docker_db",isolation_level="READ COMMITTED")
# engine = create_engine("mysql+pymysql://username:password@localhost/database_name")
conn = engine.connect()

