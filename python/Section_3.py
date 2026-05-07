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
##freadline = f.readline()##This to read the first
##print(freadline)##This to read the file content and store it in a list
##print(f.readline())##This to read the first line of the file
for line in f:##This to read the file content line by line and print it
    print(line, end='')##This to print the line without adding a new line character
f_contents = f.read()##This to read the file content and store it in a variable
print(f_contents)##This to print the content of the file
f_content1= f.read(10)##This to read the first 10 characters of the file and store it in a variable
print(f_content1)##This to print the first 10 characters of the file
f.seek(0)##This to move the file pointer to the beginning of the file

f.read()
f.seek(0)##This to move the file pointer to the beginning of the file
f_content2 = f.readlines()##This to read the first 10 characters of the file and store it in a variable
print(f_content2)##This to print the first
###################Writing to a file    
f1 = open('file_3.txt', 'w')##This to create a new file and open it in write mode
f1.write('This is a new file created using Python.\n')##This to write a string to the file
f1.write('This file is created for demonstration purposes.\n')##This to write a string to the file
f1.close()##This to close the file
##OR
with open('file_4.txt', 'w') as f2:##This to create a new file and open it in write mode and automatically close it after the block of code is executed
    f2.write('This is another new file created using Python.\n')##This to write a string to the file
    f2.write('This file is also created for demonstration purposes.\n')##This to write a string to the file     

    #####################Appending to a file
with open('file_3.txt', 'a') as f3:##This to open the existing file in append mode and automatically close it after the block of code is executed
    f3.write('\nThis line is appended to the file .\n')##This to write a string to the file
    f3.write('\nThis line is also appended to the file.\n')##This to write a string to the file
 
with open('file_3.txt', 'a') as f3:##This to open the existing file in append mode and automatically close it after the block of code is executed
    f3.write('\nThis line is appended to the file again  .\n')##This to write a string to the file
    f3.write('\nThis line is also appended to the file again .\n')##This to write a string to the file


    
 
