import os



if not os.path.exists(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\lool'):
    
    savefile_s = os.path.split(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\lool')
    savefile_fn = r'_{}'.format(savefile_s[1])
    os.makedirs(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\{}'.format(savefile_fn))

print(savefile_fn)

l = 'fuck this'
widgetname = 'okay'

with open(r'C:\Users\User\source\repos\TestNoteApplication\TestNoteApplication\NoteFinal\{}\{}.html'.format(savefile_fn, widgetname), 'w') as file:
    file.write(l)
file.close()