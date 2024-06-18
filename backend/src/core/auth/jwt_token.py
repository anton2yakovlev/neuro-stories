from typing import Any
import jwt

from core.config import settings


def encode_jwt(
    payload: dict[str, Any],
    private_key: str | bytes = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str | None = settings.auth_jwt.algorithm,
):
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str | bytes = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str | None = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded
