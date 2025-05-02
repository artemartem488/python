string = 132*"9"
while '22222' in string or '9999' in string:
    if '22222' in string:
        string=string.replace('22222','99',1)
    else:
        string=string.replace('9999',"2",1)
print(string)       
     
