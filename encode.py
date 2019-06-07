string1='core'
string2='kata'
string3=''
for i in range(0,len(string1)):
    number1=(ord(string1[i]))-96
    number2=(ord(string2[i]))-96
    if((number1+number2)<=26):
        string3=string3+(chr(96+number1+number2))
    else:
        string3=string3+(chr(96+(number1+number2-26)))
print(string3)        
