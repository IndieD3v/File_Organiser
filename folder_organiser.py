import shutil, os

current = os.getcwd()

content = os.listdir(current)

for c in content:

    file_name, file_type = os.path.splitext(c)

    if file_type in ('.png','.jpg'):
        shutil.move(
            os.path.join(current, f"{file_name}{file_type}"),
            os.path.join(current, 'images',
                         f"{file_name}{file_type}"))

    elif file_type in ('.exe'):
        shutil.move(
            os.path.join(current, f"{file_name}{file_type}"),
            os.path.join(current, 'apps',
                         f"{file_name}{file_type}"))

    elif file_type in ('.zip'):
        shutil.move(
            os.path.join(current, f"{file_name}{file_type}"),
            os.path.join(current, 'zip-file',
                         f"{file_name}{file_type}"))