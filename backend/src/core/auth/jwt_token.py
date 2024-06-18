from typing import Any
import jwt

from core.config import settings


def encode_jwt(
    payload: dict[str, Any],
    key: str | bytes,
    algorithm: str | None = "HS256",
):
    encoded = jwt.encode(payload, key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str | bytes,
    algorithm: str | None = "HS256",
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
