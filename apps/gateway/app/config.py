from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    carnival_base_url: str
    msc_base_url: str
    ncl_base_url: str
    royal_base_url: str


settings = Settings(_env_file=("apps/gateway/.env.example", "apps/gateway/.env"))
