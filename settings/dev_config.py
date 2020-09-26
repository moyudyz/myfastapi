'''
Author: moyu
Date: 2020-09-25 13:45:52
LastEditors: moyu
LastEditTime: 2020-09-25 18:28:01
Description: 
FilePath: /myfastapi/settings/dev_config.py
'''
import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Setting(BaseSettings):
    pass


setting = Setting()
