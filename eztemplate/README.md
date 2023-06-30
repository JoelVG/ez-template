# eztemplate
Tool to replace text in defined templates.  

## Recomended special characters: ǂ, ƺ, ȡ
Source: https://en.wikipedia.org/wiki/List_of_Unicode_characters

## Example
We have a template that has the following words to replace: candidate, place, time, company. We can notice that each word starts with this special character (ǂ)

email-template.txt
```
Hello ǂcandidate how are you?
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque placerat nulla sed nulla sollicitudin, a condimentum erat molestie. Praesent ac vehicula quam. Maecenas efficitur lorem vitae tortor vulputate porta. Cras consequat condimentum urna ac scelerisque. Mauris gravida in urna eu venenatis. Ut pretium convallis metus vitae dignissim. Nullam congue ex non enim efficitur lobortis. Nam tortor lectus, tincidunt vel porttitor a, tempor ut sapien. Vestibulum auctor hendrerit ex et cursus. Maecenas eget libero in dolor mattis rhoncus at ac sapien.

See you in ǂplace at ǂtime.

Best regards.
ǂcompany
```
So we can use this tool like:  
`python eztemplate.py -c ǂ -f email-template.txt -a Michael Jackson,India,20:30,ACME`

## Flags  
- `-c` denote the special character for the variables in the template.  
- `-f` path to the template file.  
- `-a` list of new values.  


## Requirements
Python 3.7+

