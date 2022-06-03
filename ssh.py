import os
import subprocess 

print('Type your email your git using!')
sting_email=input()
os.chdir("/")
os.system("ssh-keygen -t ed25519 -C %s "% sting_email)
os.system("eval $(ssh-agent -s)")
#missing the touch and write in ~/.ssh/config 
#fp = open(' ~/.ssh/config', 'w')
#fp.write(' AddKeysToAgent yes')
#fp.write(' IdentityFile ~/.ssh/id_ed25519')
os.system("cat ~/.ssh/id_ed25519.pub")
print('Coppy this and past it in ssh key generator on git')


