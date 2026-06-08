from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class ApiResponse:
    ok: bool
    method: str
    path: str
    data: Any
    message: str
    timestamp_utc: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class ApiCell:
    name = "API_CELL"
    version = "0.1.0-public-api-cell"

    def response(self, method: str, path: str, data: Any, message: str, ok: bool = True) -> ApiResponse:
        return ApiResponse(
            ok=ok,
            method=method.upper(),
            path=path,
            data=data,
            message=message,
            timestamp_utc=utc_now(),
        )

    def health(self) -> ApiResponse:
        return self.response("HEALTH", "/health", {"status": "healthy"}, "API_CELL healthy")

    def status(self) -> ApiResponse:
        return self.response(
            "STATUS",
            "/status",
            {"name": self.name, "version": self.version},
            "API_CELL status ready",
        )

    def get(self, path: str) -> ApiResponse:
        if path in {"/", "/status"}:
            return self.status()
        if path == "/health":
            return self.health()
        return self.response("GET", path, None, "GET route accepted")

    def post(self, path: str, data: Any = None) -> ApiResponse:
        return self.response("POST", path, data, "POST route accepted")

    def put(self, path: str, data: Any = None) -> ApiResponse:
        return self.response("PUT", path, data, "PUT route accepted")

    def delete(self, path: str) -> ApiResponse:
        return self.response("DELETE", path, None, "DELETE route accepted")
