from typing import List


class ConsoleBuffer:
    """In-memory buffer for ComfyUI console output."""

    _lines: List[str] = []
    _max_lines: int = 10000

    @classmethod
    def add(cls, text: str) -> None:
        if not text:
            return
        cls._lines.append(text)

        # Keep a bounded in-memory log.
        if len(cls._lines) > cls._max_lines:
            cls._lines = cls._lines[-8000:]

    @classmethod
    def clear(cls) -> None:
        cls._lines = []

    @classmethod
    def get_all(cls) -> str:
        return "".join(cls._lines) if cls._lines else ""
