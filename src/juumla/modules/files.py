from requests import Session
from requests.exceptions import RequestException
from rich.console import Console

console = Console()


def file_scan(file_to_check: str, file_url: str, session: Session) -> None:
    try:
        response = session.get(f"{file_url}/{file_to_check}", allow_redirects=True)
        content_type: str = response.headers.get("Content-Type", "").lower()

        if response.ok and "text/html" not in content_type:
            console.print(
                f"[green][+][/] Sensitive file found: [yellow]{response.url}[/]",
                highlight=False,
            )
        elif response.ok:
            console.print(
                f"[yellow][!][/] File is HTML, not a sensitive file: {response.url}",
                highlight=False,
            )

    except RequestException as error:
        console.print(
            f"[red][-][/] Error when trying to find sensitive files: {error}",
            highlight=False,
        )


def files_manager(url: str, session: Session) -> None:
    console.print(
        "\n[yellow][!][/] Running backup and config files scanner! [cyan](3/3)[/]",
        highlight=False,
    )

    config_files = [
        "configuration.php~", "configuration.php.new", "configuration.php.new~",
        "configuration.php.old", "configuration.php.old~", "configuration.bak",
        "configuration.php.bak", "configuration.php.bkp", "configuration.txt",
        "configuration.php.txt", "configuration - Copy.php", "configuration.php.swo",
        "configuration.php_bak", "configuration.orig", "configuration.php.save",
        "configuration.php.original", "configuration.php.swp", "configuration.save",
        ".configuration.php.swp", "configuration.php1", "configuration.php2",
        "configuration.php3", "configuration.php4", "configuration.php6",
        "configuration.php7", "configuration.phtml", "configuration.php-dist",
    ]

    bkp_files = [
        "1.gz", "1.rar", "1.save", "1.tar", "1.tar.bz2", "1.tar.gz", "1.tgz",
        "1.tmp", "1.zip", "2.back", "2.backup", "2.gz", "2.rar", "2.save",
        "2.tar", "2.tar.bz2", "2.tar.gz", "2.tgz", "2.tmp", "2.zip",
        "backup.back", "backup.backup", "backup.bak", "backup.bck", "backup.bkp",
        "backup.copy", "backup.gz", "backup.old", "backup.orig", "backup.rar",
        "backup.sav", "backup.save", "backup.sql~", "backup.sql.back",
        "backup.sql.backup", "backup.sql.bak", "backup.sql.bck", "backup.sql.bkp",
        "backup.sql.copy", "backup.sql.gz", "backup.sql.old", "backup.sql.orig",
        "backup.sql.rar", "backup.sql.sav", "backup.sql.save", "backup.sql.tar",
        "backup.sql.tar.bz2", "backup.sql.tar.gz", "backup.sql.tgz",
        "backup.sql.tmp", "backup.sql.txt", "backup.sql.zip", "backup.tar",
        "backup.tar.bz2", "backup.tar.gz", "backup.tgz", "backup.txt",
        "backup.zip", "database.back", "database.backup", "database.bak",
        "database.bck", "database.bkp", "database.copy", "database.gz",
        "database.old", "database.orig", "database.rar", "database.sav",
        "database.save", "database.sql~", "database.sql.back", "database.sql.backup",
        "database.sql.bak", "database.sql.bck", "database.sql.bkp",
        "database.sql.copy", "database.sql.gz", "database.sql.old",
        "database.sql.orig", "database.sql.rar", "database.sql.sav",
        "database.sql.save", "database.sql.tar", "database.sql.tar.bz2",
        "database.sql.tar.gz", "database.sql.tgz", "database.sql.tmp",
        "database.sql.txt", "database.sql.zip", "database.tar", "database.tar.bz2",
        "database.tar.gz", "database.tgz", "database.tmp", "database.txt",
        "database.zip", "joom.back", "joom.backup", "joom.bak", "joom.bck",
        "joom.bkp", "joom.copy", "joom.gz", "joomla.back", "Joomla.back",
        "joomla.backup", "Joomla.backup", "joomla.bak", "Joomla.bak",
        "joomla.bck", "Joomla.bck", "joomla.bkp", "Joomla.bkp",
        "joomla.copy", "Joomla.copy", "joomla.gz", "Joomla.gz",
        "joomla.old", "Joomla.old", "joomla.orig", "Joomla.orig",
        "joomla.rar", "Joomla.rar", "joomla.sav", "Joomla.sav",
        "joomla.save", "Joomla.save", "joomla.tar", "Joomla.tar",
        "joomla.tar.bz2", "Joomla.tar.bz2", "joomla.tar.gz", "Joomla.tar.gz",
        "joomla.tgz", "Joomla.tgz", "joomla.zip", "Joomla.zip",
        "joom.old", "joom.orig", "joom.rar", "joom.sav", "joom.save",
        "joom.tar", "joom.tar.bz2", "joom.tar.gz", "joom.tgz", "joom.zip",
        "site.back", "site.backup", "site.bak", "site.bck", "site.bkp",
        "site.copy", "site.gz", "site.old", "site.orig", "site.rar",
        "site.sav", "site.save", "site.tar", "site.tar.bz2", "site.tar.gz",
        "site.tgz", "site.zip", "sql.zip.back", "sql.zip.backup", "sql.zip.bak",
        "sql.zip.bck", "sql.zip.bkp", "sql.zip.copy", "sql.zip.gz",
        "sql.zip.old", "sql.zip.orig", "sql.zip.save", "sql.zip.tar",
        "sql.zip.tar.bz2", "sql.zip.tar.gz", "sql.zip.tgz", "upload.back",
        "upload.backup", "upload.bak", "upload.bck", "upload.bkp", "upload.copy",
        "upload.gz", "upload.old", "upload.orig", "upload.rar", "upload.sav",
        "upload.save", "upload.tar", "upload.tar.bz2", "upload.tar.gz",
        "upload.tgz", "upload.zip",
    ]

    for config_file in config_files:
        file_scan(config_file, url, session)

    for bkp_file in bkp_files:
        file_scan(bkp_file, url, session)

    console.print(
        "[yellow][!][/] Backup and config files scanner finished! [cyan](3/3)[/]",
        highlight=False,
    )
