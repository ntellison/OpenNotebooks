import os
import subprocess


# tested ; it works

subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-ppassword' , 'test.zip', 'test'], shell=False)