import typer
from rich import print
from typing_extensions import Annotated

from validators import validate_file_path, validate_new_values, validate_char
from service import replace_text, export_file, replace_text_from_csv

app = typer.Typer()


@app.command()
def text(
    file_path: Annotated[str, typer.Option("-f")] = None,
    character: Annotated[str, typer.Option("-c")] = None,
    new_values: Annotated[str, typer.Option("-v")] = None,
):
    if not file_path and not character and not new_values:
        print(
            ":rocket::rocket: [bold red] Welcome to eztemplate! [/bold red] :rocket::rocket:"
        )
        file_path = typer.prompt("Template path", value_proc=validate_file_path)
        character = typer.prompt(
            "Special character (ǂ, ƺ, ȡ)", value_proc=validate_char
        )
        new_values = typer.prompt(
            "New value(s) separated by comas(,) if applies",
            value_proc=validate_new_values,
        )
    else:
        file_path = validate_file_path(file_path)
        character = validate_char(character)
        new_values = validate_new_values(new_values)
    new_text = replace_text(file_path, new_values, character)
    export_file(file_path, new_text)


@app.command()
def csv(
    template_path: Annotated[str, typer.Option("-f")] = None,
    character: Annotated[str, typer.Option("-c")] = None,
    csv_path: Annotated[str, typer.Option("-csv")] = None,
    index: Annotated[int, typer.Option("-i")] = 0,
):
    if not template_path and not character and not csv_path:
        print(
            ":rocket::rocket: [bold red] Welcome to eztemplate! [/bold red] :rocket::rocket:"
        )
        template_path = typer.prompt("Template path", value_proc=validate_file_path)
        character = typer.prompt(
            "Special character (ǂ, ƺ, ȡ)", value_proc=validate_char
        )
        csv_path = typer.prompt("CSV file path", value_proc=validate_file_path)
        index = typer.prompt(
            "Index of column to generate the new files", default=0, type=int
        )
    else:
        template_path = validate_file_path(template_path)
        character = validate_char(character)
        csv_path = validate_file_path(csv_path)
    replace_text_from_csv(csv_path, template_path, character, index)


if __name__ == "__main__":
    app()
