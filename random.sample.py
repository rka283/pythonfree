Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> import string
>>> print("hello,enter the password")
hello,enter the password
>>> length=int(input("enter the length of the word")
	   15
	   
SyntaxError: invalid syntax
>>> lower=string.ascii_lowercase
>>> upper=string.ascii_uppercase
>>> number=string.digits
>>> symbols=string.punctuation
>>> all=lower+upper+number+symbol
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    all=lower+upper+number+symbol
NameError: name 'symbol' is not defined
>>> temp=random.sample(all,length)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    temp=random.sample(all,length)
NameError: name 'length' is not defined
>>> password="".join(temp)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    password="".join(temp)
NameError: name 'temp' is not defined
>>> print(password)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(password)
NameError: name 'password' is not defined
>>> 