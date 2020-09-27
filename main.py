from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.api_v1.api import api_router
from core.config import settings
from utils.custom_exc import register_exc

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(api_router, prefix=settings.API_V1_STR)

# 注册异常处理
register_exc(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="127.0.0.1",
                port=8000, reload=True, debug=False)
