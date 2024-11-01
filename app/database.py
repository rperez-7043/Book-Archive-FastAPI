from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from . import config


url_object = URL.create(
    drivername=config.settings.db_drivername,
    host=config.settings.db_host,
    port=config.settings.db_port,
    database=config.settings.db_database,
    username=config.settings.db_username,
    password=config.settings.db_password,
)
engine = create_engine(url_object)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
