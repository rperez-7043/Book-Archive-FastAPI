from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_drivername: str
    db_host: str
    db_port: int
    db_database: str
    db_username: str
    db_password: str
    
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

""" .env file
DB_DRIVERNAME=""
DB_HOST=""
DB_PORT=""
DB_DATABASE=""
DB_USERNAME=""
DB_PASSWORD=""

SECRET_KEY=""
ALGORITHM=""
ACCESS_TOKEN_EXPIRE_MINUTES=
"""