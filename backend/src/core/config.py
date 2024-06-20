from pathlib import Path
from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    environment: str = "dev"


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class AuthJWT(BaseModel):
    public_key_path: Path = BASE_DIR / "utils" / "certs" / "jwt-public.pem"
    private_key_path: Path = BASE_DIR / "utils" / "certs" / "jwt-private.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 2


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
print(settings.db.url)
