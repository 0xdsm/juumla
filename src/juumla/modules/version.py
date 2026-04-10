from requests import get, exceptions
from xmltodict import parse, expat

from rich.console import Console
console = Console()

from urllib3 import disable_warnings
disable_warnings()

from src.juumla.settings import props
from src.juumla.modules.vulns import vuln_manager

app_xml_header = "application/xml"
text_xml_header = "text/xml"


def get_version(url: str) -> None:
    " Get Joomla version based on XML files response "

    console.print("\n[yellow][!][/] Running Joomla version scanner! [cyan](1/3)[/]", highlight=False)

    try:
        xml_file = f"{url}/language/en-GB/en-GB.xml"
        response: str = get(xml_file, **props)
        headers: str = response.headers

        if response.ok and (app_xml_header in headers.get('Content-Type', '') or text_xml_header in headers.get('Content-Type', '')):
            data = parse(response.content)
            version = data["metafile"]["version"]

            console.print(f"[green][+][/] Joomla version is: {version}", highlight=False)
            vuln_manager(url, version)
        else:
            console.print("[yellow][!][/] Couldn't get Joomla version, trying other way...", highlight=False)
            get_version_second(url)

    except Exception as error:
        console.print(f"[red][-][/] Error when trying to get {url} Joomla version in first method: {error}", highlight=False)
        return


def get_version_second(url) -> None:
    """ Last try to get Joomla version """

    manifest_file = f"{url}/administrator/manifests/files/joomla.xml"

    try:
        response = get(manifest_file, **props)
        headers = response.headers

        if response.ok and (app_xml_header in headers.get('Content-Type', '') or text_xml_header in headers.get('Content-Type', '')):
            data = parse(response.content)
            version = data["extension"]["version"]

            console.print(f"[green][+][/] Joomla version is: {version}", highlight=False)
            vuln_manager(url, version)
        else:
            console.print("[red][-][/] Couldn't get Joomla version, stopping...", highlight=False)
            return

    except Exception as error:
        console.print(f"[red][-][/] Error when trying to get {url} Joomla version in second method: {error}", highlight=False)
        return