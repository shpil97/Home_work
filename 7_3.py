import os
import shutil

name = 'my_project'

try:
    for root, dirs, files in os.walk(name):
        if 'templates' in dirs and root != name:
            for entry in os.listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', entry), os.path.join(name, 'templates', entry))
except FileExistsError:
    print('Работа уже была проведена')
