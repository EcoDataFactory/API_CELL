from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


SENSITIVE_NAME_RE = re.compile(
    r"(^|/)(\.env|\.master_env)$|"
    r"oauth|token\.json|secret|private|credential|client_secrets|"
    r"oauth2service|etc\.json|conf\.json|"
    r"\.pem$|\.p12$|\.key$|\.crt$|\.cer$",
    re.IGNORECASE,
)


EPHEMERAL_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "cache",
    "runtime",
}


@dataclass(frozen=True)
class PathDecision:
    path: str
    allowed: bool
    reason: str


def normalize_path(path: str | Path) -> str:
    return str(path).replace("\\", "/").strip()


def is_sensitive_path(path: str | Path) -> bool:
    value = normalize_path(path)
    return bool(SENSITIVE_NAME_RE.search(value))


def is_ephemeral_path(path: str | Path) -> bool:
    value = normalize_path(path)
    parts = [p for p in value.split("/") if p]
    return any(part in EPHEMERAL_DIR_NAMES for part in parts)


def is_private_runtime_path(path: str | Path) -> bool:
    value = normalize_path(path)
    blocked = (
        "GAM_CELL_PKI/" in value
        or value.endswith("GAM_CELL_PKI")
        or "GAM_py/src/gam/gamlib" in value
        or "GAM_py/src/vendor" in value
        or "GAM_py/src/atom" in value
    )
    return blocked


def decide_trackable(path: str | Path) -> PathDecision:
    value = normalize_path(path)

    if not value:
        return PathDecision(value, False, "empty path")

    if is_private_runtime_path(value):
        return PathDecision(value, False, "private or upstream runtime path")

    if is_sensitive_path(value):
        return PathDecision(value, False, "sensitive credential or secret-like path")

    if is_ephemeral_path(value):
        return PathDecision(value, False, "ephemeral cache/runtime/bytecode path")

    return PathDecision(value, True, "trackable path")


def assert_trackable(path: str | Path) -> None:
    decision = decide_trackable(path)
    if not decision.allowed:
        raise ValueError(f"blocked path: {decision.path}: {decision.reason}")
