import os
import shutil


def sort(source):
    for file in os.listdir(source):
        name, extension = os.path.splitext(os.path.join(source, file))
        try:
            os.mkdir(extension)
        except:
            pass
        try:
            shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), extension))
        except:
            pass


sort(os.getcwd())
