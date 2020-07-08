import os
from datetime import datetime

print("All functions and attributes in OS module : ", dir(os))
print("Current Working Directory : ", os.getcwd())
print("Changing CWD to Desktop ... ")
os.chdir(r'C:\Users\gaura\Desktop')
print("Updated CWD : ", os.getcwd())
print("All files & folders in CWD : ", os.listdir())
os.chdir(r'C:\Users\gaura\Desktop\Python\File Management')
print("Updated CWD to : ", os.getcwd())
print("Create New Folder named junk\nCreating ...")
try:
    os.mkdir("junk")
    print("junk file created")
except:
    pass
print("All files & folders in CWD : ", os.listdir())
print("Create New Folder named junk with 3 subfolders\nCreating ...")
try:
    os.makedirs('main-dir\sub-dir-1\sub-dir-2\sub-dir-3')
    print("main-dir created with sub directories")
except:
    pass
print("All files & folders in CWD : ", os.listdir())
print("Delete junk folder")
try:
    os.rmdir("junk")
    print("Deleted Junk folder")
except:
    pass
print("Rename main-dir to parent")
try:
    os.rename("main-dir", "parent")
    print("Renamed !")
except:
    pass
print("All files & folders in CWD : ", os.listdir())
print("All details about parent dir", os.stat("parent"))
createdTime = os.stat("parent").st_ctime
print("File created time : ", datetime.fromtimestamp(createdTime))
print(
    "Travel through all directories and files in a given path (top down order) using os.walk, returns a tuple ("
    "dirpath,dirnames,filenames)")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path : ", dirpath)
    print("Directories : ", dirnames)
    print("Files : ", filenames)
    print()
print("Concatenation of paths, concat cwd and parent dir")
newpath = os.path.join(os.getcwd(), 'parent')
os.chdir(newpath)
print("Path concatenated and changed, current path : ", os.getcwd())
print("Check if newpath exists, Checking ....  Result : ",os.path.exists(newpath))
print("Check if sub-dir-1 is directory, Checking ... Result : ",os.path.isdir(os.path.join(os.getcwd(),'sub-dir-1')))
print("Check if example.txt is a file, Checking ... Result : ",os.path.isfile('parent/sub-dir-1/sub-dir-2'))
print("Directory name : ",os.path.dirname(os.path.join(newpath,'example.txt')))
print("File name : ",os.path.basename('parent/example.txt'))
fname,ext = os.path.splitext('example.txt')
print("File name/path : ",fname,"extension : ",ext)

