import typer
from rich import print
from typing_extensions import Annotated

from validators import validate_file_path, validate_new_values, validate_char
from service import replace_text, export_file

app = typer.Typer()

@app.command()
def main(
    file_path: Annotated[str, typer.Option("-f")]=None,
    character: Annotated[str, typer.Option("-c")]=None,
    new_values: Annotated[str, typer.Option("-v")]=None):

    if not file_path and  not character and not new_values:
        print(":rocket::rocket: [bold red] Welcome to eztemplate! [/bold red] :rocket::rocket:")
        file_path = typer.prompt("File path", value_proc=validate_file_path)
        character = typer.prompt("Special character (ǂ, ƺ, ȡ)", value_proc=validate_char)
        new_values = typer.prompt("New value(s) separated by comas(,) if applies", value_proc=validate_new_values)
    else:
        file_path = validate_file_path(file_path)
        character = validate_char(character)
        new_values = validate_new_values(new_values)
    new_text = replace_text(file_path, new_values, character)
    export_file(file_path, new_text)

if __name__ == "__main__":
    app()
    