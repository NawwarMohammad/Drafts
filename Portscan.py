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

import socket
import sys
try:
  for i in range (1,25):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if s.connect_ex((sys.argv[1],i))==0:
     print (sys.argv[1]+":"+str(i)+" open")
    s.close()
except Exception(e):
 pass
