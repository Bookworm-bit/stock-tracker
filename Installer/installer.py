import sys
import subprocess

requirements = open("requirements.txt", "r")
req = requirements.readlines()

for item in req:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', item])