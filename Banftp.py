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


import socket #We import the socket library so that we can use the socket networking features.
socket.setdefaulttimeout(10) # We set the default timeout to one. 
s=socket.socket()
s.connect_ex(("8.8.8.8",21))  #we open a socket and connect to the server on 8.8.8.8 on port 21.
banner=s.recv(1024) # We then receive up to 1,024 bytes back and print it.
s.close()
print (banner)
