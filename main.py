import typer
from rich import print

from validators import validate_file_path, validate_new_values, validate_char
from service import replace_text, export_file

app = typer.Typer()

@app.command()
def ask():
    print(":rocket::rocket: [bold red] Welcome to eztemplate! [/bold red] :rocket::rocket:")
    file_path = typer.prompt("File path", value_proc=validate_file_path)
    character = typer.prompt("Special character (ǂ, ƺ, ȡ)", value_proc=validate_char)
    new_values = typer.prompt("New value(s) separated by comas(,) if applies", value_proc=validate_new_values)
    new_text = replace_text(file_path, new_values, character)
    export_file(file_path, new_text)

if __name__ == "__main__":
    app()
    