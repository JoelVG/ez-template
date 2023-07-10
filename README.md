# eztemplate
CLI Tool to replace text in defined templates.
Special characters to define your variables in your template: ǂ, ƺ, ȡ
> We are only using this special characters to avoid problems with another common one that may cause problems processing the text.

## `text` command
We have a template that has the following words to replace: candidate, place, time, company.
We notice that each word starts with this special character (ǂ)

> We can use the compiled app in the same way: [Windows](/dist/eztemplate.exe) - [UnixOs](/dist/eztemplate)

[email-template.txt](email-template.txt)
```
Hello ǂcandidate how are you?

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nulla sed nulla sollicitudin, a condimentum erat molestie.
Praesent ac vehicula quam. Maecenas efficitur lorem vitae tortor vulputate porta.
Cras consequat condimentum urna ac scelerisque. Mauris gravida in urna eu venenatis. Ut pretium convallis metus vitae dignissim.
Nullam congue ex non enim efficitur lobortis. Nam tortor lectus, tincidunt vel porttitor a, tempor ut sapien.
Vestibulum auctor hendrerit ex et cursus. Maecenas eget libero in dolor mattis rhoncus at ac sapien.

See you in ǂplace at ǂtime.

Best regards.
ǂcompany
```
So we can use this tool like:
```
$ python main.py text -f email-template.txt -c ǂ -v "Sebastian André,P sherman calle wallaby 42 sydney,10:30,ACME"
```

This will generate a new file with the suffix *_replaced* in the same folder.
```
Hello Sebastian André how are you?

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nulla sed nulla sollicitudin, a condimentum erat molestie.
Praesent ac vehicula quam. Maecenas efficitur lorem vitae tortor vulputate porta.
Cras consequat condimentum urna ac scelerisque. Mauris gravida in urna eu venenatis. Ut pretium convallis metus vitae dignissim.
Nullam congue ex non enim efficitur lobortis. Nam tortor lectus, tincidunt vel porttitor a, tempor ut sapien.
Vestibulum auctor hendrerit ex et cursus. Maecenas eget libero in dolor mattis rhoncus at ac sapien.

See you in P sherman calle wallaby 42 sydney at 10:30.


Best regards.
ACME.
```

### Flags
- `-f` path to the template file.
- `-c` denote the special character for the variables in the template.
- `-v` list of new values.

## `csv` command
As before, we need a [template](template.txt) with defined targets. For this example we will use the template provided in the docs, also we need a [.csv file](new-values.csv) that will contain the values that we want to replace in the template.

This command will take this new values from the csv, replace in the template and generate a .txt file with the prefix of `message_`  and the suffix of the value that is in the first column in the same path that we have the template.

|col1|col2|
|-----|-----|
|Joe|Sam|
|Felix|Carol|
|Abe|Roxane|

E.g.
```
$ python main.py csv -f template.txt -c ǂ -csv new-values.csv
🚀🚀 Your file has been exported! 🚀🚀
🚀🚀 Your file has been exported! 🚀🚀
🚀🚀 Your file has been exported! 🚀🚀
```
Or if we want to interact with the console:
```
$ python main.py csv
🚀🚀  Welcome to eztemplate!  🚀🚀
Template path: template.txt
Special character (ǂ, ƺ, ȡ): ǂ
CSV file path: new-values.csv
Index of column to generate the new files [0]:
🚀🚀 Your file has been exported! 🚀🚀
🚀🚀 Your file has been exported! 🚀🚀
🚀🚀 Your file has been exported! 🚀🚀
```
Will generate: message_Joe.txt, message_Felix.txt, message_Abe.txt.
If we want to set the value from another column as suffix we can pass the index flag like:
```
$ python main.py csv -f template.txt -c ǂ -csv new-values.csv -i 2
```
so this will take the values from the column 2 and use it as suffix.
## More examples
[v0 Examples](docs/v0.md)

## Requirements
Python 3.8+
```
$ pip install -r requirements.txt
```
