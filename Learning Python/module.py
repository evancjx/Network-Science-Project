import os
from datetime import datetime

print(dir(os))

print(os.getcwd())

os.chdir('/Dropbox/National Technological University (NTU)/Year 3 Sem 2/CZ4071 Network Science')

print(os.listdir())

os.mkdir('OS-DEMO')
os.makedirs('OS-DEMO/SUB-DIR')

print(os.listdir())

os.rmdir('OS-DEMO/SUB-DIR')
print(os.listdir())
os.makedirs('OS-DEMO/SUB-DIR')
print(os.listdir())
os.removedirs('OS-DEMO/SUB-DIR')
print(os.listdir())

os.rename('test.txt', 'demo.txt')

print(os.stat('demo.txt'))

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

print(os.environ.get('HOME'))

os.path.join(os.environ.get('HOME'), 'test.txt')