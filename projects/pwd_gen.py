#!/usr/bin/python
# david spencer
# 05 |06 | 2022
# password generator

import random

characters= 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~{}":<>?"'

no_passwords= int(input('How many passwords do you want?\n---'))
no_digits= int(input('How long do you wish your password to be?' +'NOTICE'+' \n password should have at most 20 figures\n---'))

if no_digits <= 20:
    for i in range (0,no_passwords):
        password=''
        for i in range (0, no_digits):
            swapper= random.choice(characters)
            password= password + swapper

    print('new password generated...'+ password)

else:
    print('too many characters, retry')
    no_digits= int(input('How long do you wish your password to be?' +'NOTICE'+' \n password should have at most 20 figures\n---'))

