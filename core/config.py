import secrets
from typing import List, Optional
from pydantic import BaseSettings, AnyHttpUrl, EmailStr


class Settings(BaseSettings):
    """ 配置文件类 """
    # =============项目配置================
    PROJECT_NAME: str = 'MyFastAPI'
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_HOST: AnyHttpUrl = 'http://localhost:8000'
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # =============数据库配置================
    MYSQL_SERVER: str = ''
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = '123456'
    MYSQL_PORT: str = '3306'
    MYSQL_DB: str = 'test'
    SQLALCHEMY_DATABASE_URI: str = 'mysql://root:123456@127.0.0.1:3306/test?charset=utf8mb4'

    # =============邮箱相关================
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "email-templates/build"
    EMAILS_ENABLED: bool = False

    # =============超级管理员================
    EMAIL_TEST_USER: EmailStr = "admin@admin.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "admin@admin.com"
    FIRST_SUPERUSER_PASSWORD: str = "123456"
    USERS_OPEN_REGISTRATION: bool = False

    SENTRY_DSN: str = None

    class Config:
        case_sensitive = True


settings = Settings()
