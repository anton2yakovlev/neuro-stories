from datetime import datetime, timedelta, UTC
from typing import Any
import jwt

from core.config import settings


def enrich_payload(
    payload: dict,
    expire_timedelta: timedelta | None = None,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
) -> dict:
    to_encode = payload.copy()
    now = datetime.now(UTC)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(expire_minutes)
    to_encode.update(exp=expire, iat=now)
    return to_encode


def encode_jwt(
    payload: dict[str, Any],
    private_key: str | bytes = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str | None = settings.auth_jwt.algorithm,
    expire_timedelta: timedelta | None = None,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
):
    to_encode = enrich_payload(payload, expire_timedelta, expire_minutes)
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str | bytes = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str | None = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded
