from requests import Session
from requests.exceptions import RequestException
from xmltodict import parse

from rich.console import Console

from src.juumla.modules.vulns import vuln_manager

console = Console()

_APP_XML = "application/xml"
_TEXT_XML = "text/xml"


def _is_xml_response(content_type: str) -> bool:
    return _APP_XML in content_type or _TEXT_XML in content_type


def get_version(url: str, session: Session) -> None:
    console.print(
        "\n[yellow][!][/] Running Joomla version scanner! [cyan](1/3)[/]",
        highlight=False,
    )

    xml_file = f"{url}/language/en-GB/en-GB.xml"

    try:
        response = session.get(xml_file, allow_redirects=True)
        content_type: str = response.headers.get("Content-Type", "")

        if response.ok and _is_xml_response(content_type):
            data = parse(response.content)
            version: str = data["metafile"]["version"]
            console.print(
                f"[green][+][/] Joomla version is: {version}",
                highlight=False,
            )
            vuln_manager(url, version, session)
        else:
            console.print(
                "[yellow][!][/] Couldn't get Joomla version, trying other way...",
                highlight=False,
            )
            get_version_second(url, session)

    except RequestException as error:
        console.print(
            f"[red][-][/] Error when trying to get {url} Joomla version in first method: {error}",
            highlight=False,
        )


def get_version_second(url: str, session: Session) -> None:
    manifest_file = f"{url}/administrator/manifests/files/joomla.xml"

    try:
        response = session.get(manifest_file, allow_redirects=True)
        content_type: str = response.headers.get("Content-Type", "")

        if response.ok and _is_xml_response(content_type):
            data = parse(response.content)
            version: str = data["extension"]["version"]
            console.print(
                f"[green][+][/] Joomla version is: {version}",
                highlight=False,
            )
            vuln_manager(url, version, session)
        else:
            console.print(
                "[red][-][/] Couldn't get Joomla version, stopping...",
                highlight=False,
            )

    except RequestException as error:
        console.print(
            f"[red][-][/] Error when trying to get {url} Joomla version in second method: {error}",
            highlight=False,
        )
