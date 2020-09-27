'''
Author: moyu
Date: 2020-09-27 13:57:02
LastEditors: moyu
LastEditTime: 2020-09-28 00:39:06
Description: 统一响应格式
FilePath: /myfastapi/utils/response_code.py
'''

from fastapi import status
from fastapi.responses import Response, ORJSONResponse, PlainTextResponse

from typing import Union


def resp_200(data: Union[list, dict, str] = None) -> Response:
    """ 正常响应 """
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': "Success",
            'data': data,
        }
    )


def resp_400(data: str = None) -> Response:
    """ 错误响应 """
    return PlainTextResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=data
    )


def resp_403(data: str = "Forbidden") -> Response:
    """ 请求被拒绝 """
    return PlainTextResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=data
    )


def resp_404(data: str = "Page Not Found") -> Response:
    """ 请求资源找不到 """
    return PlainTextResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=data
    )


def resp_500(data: str = "Server internal error") -> Response:
    """ 服务器内部错误 """
    return PlainTextResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=data
    )
