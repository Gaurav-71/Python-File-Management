import shutil
import os

os.mkdir('source')
os.mkdir('destination')

main = os.getcwd()
source = os.path.join(os.getcwd(), 'source')
destination = os.path.join(os.getcwd(), 'destination')

os.chdir(source)
file = open('a.txt', 'w+')
for line in range(10):
    file.write("Line : %d " % (line + 1))
file.close()
os.chdir(main)


def status():
    print('\t Contents in Source : ', os.listdir(source))
    print('\t Contents in Destination : ', os.listdir(destination))


print('Source : ', source)
print('Destination : ', destination)
status()
print('Copy source folder and all its contents and paste in destination folder')
shutil.copytree(source, os.path.join(destination, 'source'))
print('Copied Source to Destination Successfully!')
status()
print('Copy a.txt file from source to destination')
shutil.copy(os.path.join(source, 'a.txt'), destination)
print('Copied file a.txt from source to Destination Successfully !')
status()
print('Delete a.txt from destination')
os.remove(os.path.join(destination, 'a.txt'))
print('Deleted a.txt from Destination Successfully !')
status()
print('Move a.txt from source to destination')
shutil.move(os.path.join(source, 'a.txt'), destination)
print('Moved a.txt fromSource to Destination Successfully !')
status()

shutil.rmtree('source')
shutil.rmtree('destination')
