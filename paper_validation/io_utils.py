from __future__ import annotations

from collections.abc import Iterator
import json
import os
from pathlib import Path
from typing import Any, TextIO


def long_path(path: os.PathLike[str] | str) -> str:
    raw = os.fspath(path)
    if os.name != "nt":
        return raw
    absolute = os.path.abspath(raw)
    if absolute.startswith("\\\\?\\"):
        return absolute
    if absolute.startswith("\\\\"):
        return "\\\\?\\UNC\\" + absolute.lstrip("\\")
    return "\\\\?\\" + absolute


def ensure_parent(path: os.PathLike[str] | str) -> None:
    parent = Path(path).parent
    if str(parent) not in ("", "."):
        os.makedirs(long_path(parent), exist_ok=True)


def open_text(path: os.PathLike[str] | str, mode: str = "r", *, encoding: str = "utf-8", newline: str | None = None) -> TextIO:
    if any(flag in mode for flag in ("w", "a", "x", "+")):
        ensure_parent(path)
    return open(long_path(path), mode, encoding=encoding, newline=newline)


def read_text(path: os.PathLike[str] | str, *, encoding: str = "utf-8") -> str:
    with open_text(path, "r", encoding=encoding) as handle:
        return handle.read()


def write_text(path: os.PathLike[str] | str, text: str, *, encoding: str = "utf-8") -> None:
    with open_text(path, "w", encoding=encoding) as handle:
        handle.write(text)


def read_bytes(path: os.PathLike[str] | str) -> bytes:
    with open(long_path(path), "rb") as handle:
        return handle.read()


def iter_files(root: os.PathLike[str] | str) -> Iterator[Path]:
    root_path = Path(root)
    pending = [root_path]
    while pending:
        current = pending.pop()
        with os.scandir(long_path(current)) as entries:
            for entry in entries:
                path = current / entry.name
                if entry.is_dir(follow_symlinks=False):
                    pending.append(path)
                elif entry.is_file(follow_symlinks=True):
                    yield path


def exists(path: os.PathLike[str] | str) -> bool:
    return os.path.exists(long_path(path))


def read_json(path: os.PathLike[str] | str) -> Any:
    return json.loads(read_text(path, encoding="utf-8"))


def write_json(path: os.PathLike[str] | str, data: Any) -> None:
    write_text(path, json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
