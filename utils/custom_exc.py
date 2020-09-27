'''
Author: moyu
Date: 2020-09-27 15:23:22
LastEditors: moyu
LastEditTime: 2020-09-28 01:15:36
Description: 自定义异常处理
FilePath: /myfastapi/utils/custom_exc.py
'''
import traceback
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from extensions import logger
from utils import response_code


class NotFoundException(Exception):
    """ 资源找不到异常 """

    def __init__(self, err_desc: str = "Page Not Found"):
        self.err_desc = err_desc


class UserTokenException(Exception):
    """ 用户认证失败 """

    def __init__(self, err_desc: str = "Forbidden"):
        self.err_desc = err_desc


class UnicornException(Exception):
    """ 自定义异常 """

    def __init__(self, err_desc: str):
        self.err_desc = err_desc


def register_exc(app: FastAPI) -> None:
    """ 注册/覆盖异常处理 """

    # UserTokenError异常处理
    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        logger.debug(
            f"认证异常\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return response_code.resp_400(exc.err_desc)

    # UserTokenError异常处理
    @app.exception_handler(UserTokenException)
    async def token_exception_handler(request: Request, exc: UserTokenException):
        logger.debug(
            f"认证异常\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return response_code.resp_403(exc.err_desc)

    # NotFoundError异常处理
    @app.exception_handler(NotFoundException)
    async def notfount_exception_handler(request: Request, exc: NotFoundException):
        logger.debug(
            f"无效请求\n{request.method} | URL:{request.url} | {exc.err_desc}")
        return response_code.resp_404(exc.err_desc)

    # 覆盖HTTPException异常处理
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.debug(
            f"HTTP异常\n{request.method} | URL:{request.url} | {exc.detail}")
        return response_code.resp_400(exc.detail)

    # 覆盖RequestValidationError异常处理
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.debug(
            f"参数异常\n{request.method} | URL:{request.url}\n{exc}")
        return response_code.resp_400(str(exc))

    # 覆盖全部异常处理
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: HTTPException):
        logger.error(
            f"全局异常\n{request.method} | URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return response_code.resp_500()
