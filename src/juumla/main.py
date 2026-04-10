from requests import Session
from requests.exceptions import RequestException

from rich.console import Console

from src.juumla.modules.version import get_version

console = Console()


def perform_checks(url: str, session: Session) -> None:
    try:
        response = session.get(url, allow_redirects=True)
        status_code: int = response.status_code
        body: str = response.text

        if response.ok:
            console.print(
                f"[green][+][/] Connected successfully to [yellow]{url}[/]",
                highlight=False,
            )
            detect_joomla(url, body, session)
        else:
            console.print(
                f"[red][-][/] Host returned status code: {status_code}",
                highlight=False,
            )

    except RequestException as error:
        console.print(
            f"[red][-][/] Error when trying to connect to {url}: {error}",
            highlight=False,
        )


def detect_joomla(url: str, body: str, session: Session) -> None:
    console.print(
        "[yellow][!][/] Checking if target is running Joomla...",
        highlight=False,
    )

    if '<meta name="generator" content="Joomla!' in body:
        get_version(url, session)
    else:
        console.print(
            "[red][-][/] Target is not running Joomla apparently",
            highlight=False,
        )
