from json import load
from pathlib import Path

from requests import Session
from rich.console import Console

from src.juumla.modules.files import files_manager

console = Console()

_DATA_FILE = Path(__file__).parent.parent / "data" / "vulnerabilites.json"


def parse_version(version_str: str) -> tuple[int, ...]:
    parts = version_str.strip().split(".")
    result: list[int] = []
    for part in parts:
        try:
            result.append(int(part))
        except ValueError:
            result.append(0)
    return tuple(result)


def vuln_manager(url: str, version: str, session: Session) -> None:
    console.print(
        "\n[yellow][!][/] Running Joomla vulnerabilities scanner! [cyan](2/3)[/]",
        highlight=False,
    )

    parsed_target = parse_version(version)

    with open(_DATA_FILE) as file:
        content = load(file)

        for vuln_title, version_range in content.items():
            min_str, max_str = version_range.split("|")
            if parse_version(min_str) <= parsed_target <= parse_version(max_str):
                console.print(f"[green][+][/] {vuln_title}", highlight=False)

    console.print(
        "[yellow][!][/] Vulnerabilities scanner finished! [cyan](2/3)[/]",
        highlight=False,
    )
    files_manager(url, session)
