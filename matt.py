import os
import pathlib

first_dir = str(input("Enter first directory path: "))
second_dir = str(input("Enter second directory path: "))

#for x in os.scandir(first_dir):
#    if x.is_dir():
#        print(x.path)

os.chdir(first_dir)
first_list = []
for root, dirs, files in os.walk('.'):
    for name in files:
        first_list.append(os.path.join(root,name)[2:])

#first_list.sort()
#print("List of files from first directory\n-----------------")
#for fir in first_list:
#    print(fir)


os.chdir(second_dir)
second_list = []
for root, dirs, files in os.walk('.'):
    for name in files:
        second_list.append(os.path.join(root,name)[2:])

#second_list.sort()
#print("\n\nList of files from second directory\n------------")
#for sec in second_list:
#    print(sec)
ofile.write("Files in first directory not in second directory\n--------------")
fdiff = list(set(first_list).difference(set(second_list)))
for x in sorted(fdiff):
    print(x)

print("\nFiles in second directory not in first directory\n--------------")
sdiff = list(set(second_list).difference(set(first_list)))
for x in sorted(sdiff):
    print(x)
