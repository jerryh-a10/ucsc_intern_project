import subprocess
import os
filenames = ['vagrantup.py', 'swarminit.py', 'services.py']

for fh in filenames:
    input('Press enter to run: %s'%(fh,))
    os.system('python {}'.format(fh)) 

