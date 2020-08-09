import os
import subprocess


# tested ; it works

#subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-ppassword' , 'test.zip', 'test'], shell=False)

# apparently folder must contain a file to have encryption
#subprocess.run([r'7z\7-Zip\7z.exe', 'a', '-ppassword' , 'test.7z', 'test'], shell=False)

# try:
#     subprocess.run([r'7z\7-Zip\7z.exe', 'e', 'test.7z', 'test'], shell=False)
# except:
#     print('file is password protected')


if r'_' in r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\_test.7z':
    subprocess.run([r'7z\7-Zip\7z.exe', 'e', '-ppassword', '_test.7z', '-o_test'], shell=False)
else:
    print('file is regular 7z')
    subprocess.run([r'7z\7-Zip\7z.exe', 'e', 'test.7z', '-otest'], shell=False)