import os

import click
import click_spinner

from chatbot.services import services, unit_of_work

LINKS_TEMP_FILE = "links.txt"


@click.group()
def cli():
    pass


@click.command()
@click.argument("url")
@click.option("--limit", default=1000, help="Limit the number of pages scraped")
def scrap(url: str, limit: int):
    """Crawl and scrap web pages starting from the given URL"""
    uow = unit_of_work.LocalChromaUnitOfWork()
    if not os.path.exists(LINKS_TEMP_FILE):
        # Save it to temp file
        with open(LINKS_TEMP_FILE, "w", encoding="utf8") as file:
            click.echo(f"Crawling from {url}...")
            with click_spinner.spinner():
                for line in services.crawl(url, uow, limit=limit):
                    services.crawl(line, uow, limit=limit)
                    file.write(line)
                    file.write("\n")
                    file.flush()

    with open(LINKS_TEMP_FILE, "r", encoding="utf8") as file:
        lines = [line.strip() for line in file.readlines()]
        with click.progressbar(
            lines, label=f"Scrapping from {click.format_filename(b'links.txt')}"
        ) as progress_bar:
            for line in progress_bar:
                services.scrap(line, uow)

    click.echo(f"🎉 Scrapped {len(lines)} web pages!")


cli.add_command(scrap)

if __name__ == "__main__":
    cli()
