from json import load
from pathlib import Path
from typing import Any

from requests import Session
from rich.console import Console

from src.juumla.modules.files import files_manager

console = Console()

_DATA_FILE = Path(__file__).parent.parent / "data" / "vulnerabilities.json"

_SEVERITY_STYLE: dict[str, str] = {
    "critical": "bold red",
    "high": "red",
    "medium": "yellow",
    "low": "cyan",
}


def parse_version(version_str: str) -> tuple[int, ...]:
    parts = version_str.strip().split(".")
    result: list[int] = []
    for part in parts:
        try:
            result.append(int(part))
        except ValueError:
            result.append(0)
    return tuple(result)


def format_vuln(entry: dict[str, Any]) -> str:
    severity: str = entry.get("severity", "unknown").upper()
    style: str = _SEVERITY_STYLE.get(entry.get("severity", ""), "green")
    cve: str | None = entry.get("cve")
    title: str = entry.get("title", "Unknown vulnerability")
    cvss: float | None = entry.get("cvss")

    cve_part = f"[white]{cve}[/] " if cve else ""
    cvss_part = f" [dim](CVSS {cvss})[/]" if cvss is not None else ""

    return (
        f"[green][+][/] [{style}][{severity}][/] "
        f"{cve_part}{title}{cvss_part}"
    )


def vuln_manager(url: str, version: str, session: Session) -> None:
    console.print(
        "\n[yellow][!][/] Running Joomla vulnerabilities scanner! [cyan](2/3)[/]",
        highlight=False,
    )

    parsed_target = parse_version(version)
    found: int = 0

    with open(_DATA_FILE) as file:
        entries: list[dict[str, Any]] = load(file)

    for entry in entries:
        min_str: str = entry["min_version"]
        max_str: str = entry["max_version"]

        if parse_version(min_str) <= parsed_target <= parse_version(max_str):
            console.print(format_vuln(entry), highlight=False)
            found += 1

    if found == 0:
        console.print(
            "[yellow][!][/] No known vulnerabilities found for this version.",
            highlight=False,
        )

    console.print(
        f"[yellow][!][/] Vulnerabilities scanner finished! [cyan](2/3)[/] "
        f"[dim]{found} found[/]",
        highlight=False,
    )
    files_manager(url, session)
