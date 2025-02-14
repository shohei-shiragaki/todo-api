import enum
from typing import Any, Optional

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class AppEnvironment(str, enum.Enum):
    # ここで環境を指定する
    # ENVIRONMENT = "development"
     ENVIRONMENT = "production"

class Settings(BaseSettings):
    ENVIRONMENT: AppEnvironment
    # API_V1_STR: str = "/api/v1"
    # PROJECT_NAME: str = "TODO-API"
    # 開発環境用
    DEV_POSTGRES_USER: str
    DEV_POSTGRES_PASSWORD: str
    DEV_POSTGRES_DB: str
    DEV_POSTGRES_SERVER: str
    DEV_POSTGRES_PORT: str
    # 本番環境用
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_SSLMODE: str = "require"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        
        if values.data.get("ENVIRONMENT") == "development":
            # 開発環境用（dockerのコンテナ内）
            return str(PostgresDsn.build(
                    scheme="postgresql",
                    username=values.data.get("DEV_POSTGRES_USER"),
                    password=values.data.get("DEV_POSTGRES_PASSWORD"),
                    host=values.data.get("DEV_POSTGRES_SERVER"),
                    port=int(values.data.get("DEV_POSTGRES_PORT")),
                    path=f"{values.data.get('DEV_POSTGRES_DB') or ''}",
                ))
        elif values.data.get("ENVIRONMENT") == "production":
            # 本番用（Neon　posgres）
            return str(PostgresDsn.build(
                    scheme="postgresql",
                    username=values.data.get("POSTGRES_USER"),
                    password=values.data.get("POSTGRES_PASSWORD"),
                    host=values.data.get("POSTGRES_SERVER"),
                    path=f"{values.data.get('POSTGRES_DB') or ''}",
                    port=int(values.data.get("POSTGRES_PORT")),
                    query=f"sslmode={values.data.get('POSTGRES_SSLMODE')}"
                ))

    class Config:
        env_file = ".env"

settings = Settings()