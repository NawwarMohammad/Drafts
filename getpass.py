#!/usr/bin/env python3
# Basic user interface header
print(r"""
_______    ____         ___         ___         ___  ___         ___         ___
|      \   |  |         \  \       /   \       /  /  \  \       /   \       /  /            ____ __ 
|  |\   \  |  |  _____   \  \     /  /\ \     /  /    \  \     /  /\ \     /  /      ____   |  /  /
|  |  \  \ |  |  / _` \   \  \   /  /  \ \   /  /      \  \   /  /  \ \   /  /      / _` \  |  __/
|  |   \  \|  | | (_| |    \  \_/  /    \ \_/  /        \  \_/  /    \ \_/  /      | (_| |  |  |
|__|    \_____|  \__,_|     \_____/      \____/          \_____/      \____/        \__,_|  |__|""")
print("\n**********************************SYRIA**************************************************")
print("\n*            Copyright of Nawwar Mohammad, 2024                                         *")
print("\n*            https://www.linkedin.com/in/nawwarmohammad/                                *")
print("\n*            https://github.com/NawwarMohammad                                          *")
print("\n**********************************SYRIA**************************************************")

import sys
import crypt

passfile=open('dict.txt','r')
for word in  passfile.readlines():
  if (crypt.crypt(word.strip(),"MS")==sys.argv[1]):  
    print ("password is "+word)
    # Password + salt = Password hash
#We can use this function in a small password cracker program to recover a password by checking it against the dictionary of expected passwords.
