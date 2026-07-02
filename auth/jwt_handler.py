import jwt

from datetime import datetime
from datetime import timedelta

from config import JWT_SECRET

ALGORITHM = "HS256"


def create_access_token(user_id: str):

    payload = {
        "sub": user_id,
        "exp": datetime.utcnow()
        + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token: str):

    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[ALGORITHM]
    )

    return payload["sub"]