from fastapi import FastAPI

from slowapi.errors import (
    RateLimitExceeded
)

from slowapi.middleware import (
    SlowAPIMiddleware
)

from slowapi import (
    _rate_limit_exceeded_handler
)

from auth.routes import (
    router as auth_router
)

from api.chat import (
    router as chat_router
)

from middleware.limiter import (
    limiter
)

app = FastAPI()

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(
    SlowAPIMiddleware
)

app.include_router(
    auth_router
)

app.include_router(
    chat_router
)