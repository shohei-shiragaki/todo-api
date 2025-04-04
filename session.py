# from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import settings

if settings.SQLALCHEMY_DATABASE_URI:
    engine = create_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
    )
    SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    if settings.ENVIRONMENT == "development":
        db_info = f"開発環境URI:{settings.SQLALCHEMY_DATABASE_URI}"

    elif settings.ENVIRONMENT == "production":
        db_info = f"本番環境URI:{settings.SQLALCHEMY_DATABASE_URI}"

else:
    raise ValueError("SQLALCHEMY_DATABASE_URI is not set")