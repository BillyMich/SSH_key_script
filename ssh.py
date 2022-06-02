import os
import subprocess 

print('Type your email your git using!')
sting_email=input()
os.chdir("/home/")
os.system("ssh-keygen -t ed25519 -C %s "% sting_email)
