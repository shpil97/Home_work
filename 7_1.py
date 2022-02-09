import os
name_project = 'my_project'
path_list = ['settings', 'mainapp', 'adminapp', 'authapp']


def dir_add(my_list):
    for i in path_list:
        os.makedirs(os.path.join(name_project, i), exist_ok=False)


if __name__ == '__main__':
    dir_add(path_list)
