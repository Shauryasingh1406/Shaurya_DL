##Bool
print(1>4)
a= 4
b=6
print(b>a)
##I/O File handling 
f = open('file_2.txt', 'r')## This to open the existing file
##OR 
##with open('my_file.txt', 'r') as my_file :##This to open the existing file and automatically close it after the block of code is executed
##my_file_content = my_file.read()##This to read the file content and store it in a variable
##print(my_file_content)##This to print the content of the file
##print(my_file.name)##This to print the name of the file
##read_file = f.read()##This to read the file content and store it in a variable
print(f.name);##This to print the name of the file
##print(read_file)##This to print the content of the file
print(f.mode)##This to print the mode of the file
freadline = f.readline()##This to read the first
##print(freadline)##This to read the file content and store it in a list
print(f.readline())##This to read the first line of the file
for line in f:##This to read the file content line by line and print it
    print(line)
