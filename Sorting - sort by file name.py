import os
import shutil


def customSplit(str):
    result = str.split('(')
    return result[0].strip()


def sort(source):
    for file in os.listdir(source):
        name, extension = os.path.splitext(os.path.join(source, file))
        try:
            os.mkdir(customSplit(name))
        except:
            pass
        try:
            shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), customSplit(name)))
        except:
            pass


sort(os.getcwd())
