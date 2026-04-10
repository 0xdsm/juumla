from pathlib import Path
from random import choice

from requests import Session
from urllib3 import disable_warnings

disable_warnings()

_BASE_DIR = Path(__file__).parent


def get_user_agent() -> str:
    ua_path = _BASE_DIR / "user-agents.txt"
    with open(ua_path) as f:
        agents = f.readlines()
    return choice(agents).strip()


def build_session(custom_headers: dict[str, str] | None = None) -> Session:
    session = Session()
    headers: dict[str, str] = {
        "User-Agent": get_user_agent(),
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    if custom_headers:
        headers.update(custom_headers)
    session.headers.update(headers)
    session.verify = False
    return session
