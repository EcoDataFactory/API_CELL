from __future__ import annotations

from typing import Any

from .core import ApiCell, ApiResponse


def dispatch(method: str, path: str = "/", data: Any = None) -> ApiResponse:
    api = ApiCell()
    action = method.lower().strip()

    if action == "health":
        return api.health()
    if action == "status":
        return api.status()
    if action == "get":
        return api.get(path)
    if action == "post":
        return api.post(path, data)
    if action == "put":
        return api.put(path, data)
    if action == "delete":
        return api.delete(path)

    return api.response(method, path, data, f"unsupported method: {method}", ok=False)
