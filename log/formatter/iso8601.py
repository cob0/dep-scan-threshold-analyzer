import logging
from datetime import datetime, timezone


class ISO8601Formatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%') -> None:
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

    def formatTime(self, record, datefmt=None) -> str:
        dt = datetime.fromtimestamp(record.created, tz=timezone.utc)

        if datefmt:
            dtstr = dt.strftime(datefmt)
            if '%f' in datefmt:
                dtstr = dtstr.replace('%f', f"{int(record.msecs):03d}")
        else:
            dtstr = dt.isoformat(timespec='milliseconds')
        return dtstr
