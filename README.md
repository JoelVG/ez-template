# eztemplate
Tool to replace text in defined templates.  
Special characters to define your variables in your template: ǂ, ƺ, ȡ  
> We are only using this special characters to avoid problems with another common one that may cause problems processing the text.

## Example
We have a template that has the following words to replace: candidate, place, time, company.   
We notice that each word starts with this special character (ǂ)

> We can use the compiled app in the same way: [Windows](/JoelVG/ez-template/raw/v0-csf-files-and-cli/dist/eztemplate.exe)

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
`python main.py -f email-template.txt -c ǂ -v "Sebastian André,P sherman calle wallaby 42 sydney,10:30,ACME"`

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

## Flags  
- `-f` path to the template file.
- `-c` denote the special character for the variables in the template.
- `-v` list of new values.

## More examples
[v0 Examples](docs/v0.md)

## Requirements
Python 3.7+

