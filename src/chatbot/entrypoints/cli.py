import click
import click_spinner
import os

from chatbot.services import services, unit_of_work

LINKS_TEMP_FILE = "links.txt"


@click.group()
def cli():
    pass


@click.command()
@click.argument("url")
@click.option("--limit", default=1000, help="Limit the number of pages scraped")
def scrap(url: str, limit: int):
    uow = unit_of_work.LocalChromaUnitOfWork()

    """Crawl and scrap web pages starting from the given URL"""
    if not os.path.exists(LINKS_TEMP_FILE):
        # Save it to temp file
        with open(LINKS_TEMP_FILE, "w") as file:
            click.echo(f"Crawling from {url}...")
            with click_spinner.spinner() as spinner:
                for url in services.crawl(url, uow, limit=limit):
                    services.crawl(url, uow, limit=limit)
                    file.write(url)
                    file.write("\n")
                    file.flush()

    with open(LINKS_TEMP_FILE, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        with click.progressbar(lines, label=f"Scrapping from {click.format_filename(b'links.txt')}") as bar:
            for url in bar:
                services.scrap(url, uow)

    click.echo(f"🎉 Scrapped {len(lines)} web pages!")


cli.add_command(scrap)

if __name__ == "__main__":
    cli()
