import sys

from loguru import logger

from src.main.config.settings import settings

logger.remove()


def custom_formatter():
    format_string = (
        "[{time:YYYY-MM-DD HH:mm:ss.SSS}] {extra[request_id]}[{level}] {message}"
    )
    return format_string


def enrich_record(record):
    rid = record["extra"].get("request_id", None)
    record["extra"]["request_id"] = f"[rid={rid}] " if rid else ""


logger = logger.patch(enrich_record)
logger.add(
    sink=sys.stdout,
    format=custom_formatter(),
    level=settings.LOG_LEVEL,
    enqueue=True,
    backtrace=True,
    diagnose=True,
)
