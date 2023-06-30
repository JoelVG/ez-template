import typer
from validators import validate_file_path, validate_new_values
from service import replace_text, export_file

app = typer.Typer()

@app.command()
def ask():
    print("**************Welcome to eztemplate**************")
    file_path = typer.prompt("File path", value_proc=validate_file_path)
    character = typer.prompt("Special character", type=str)
    new_values = typer.prompt("New values separated by comas(,)", value_proc=validate_new_values)
    # print(f"file {file_path} char {character} new values {new_values}")
    new_text = replace_text(file_path, new_values, character)
    export_file(file_path, new_text)

if __name__ == "__main__":
    app()
    