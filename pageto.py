# -*- coding: cp1251 -*-
print ('')
print ('  Password Generation Tool 1.0g, GPL v.3')
print ('  E-mail: Andrew Golubev <ganrage@fastmail.fm>')
print ('')


import random

a=''

PassAmount=20
PassLenght=20

L='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.:;"*-_=+%$#^&()@!?[]{}|/`~,<>'

i=0
while i < PassAmount:
	PasswordIs=''
	q=0
	while q < PassLenght:
		PasswordIs=PasswordIs+random.choice(L)
		q+=1
	print ('    Password: ', PasswordIs)
	i+=1
print ('')
print (' Hit ''Enter'' ')

a=input()