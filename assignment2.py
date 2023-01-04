#r+
#In Python, the 'r+' mode is used to open a file for both reading and writing. It allows you to read from and write to the same file.
#Here is an example of how to use 'r+' mode to open a file in Python:
# Open the file in 'r+' mode
f = open('file.txt', 'r+')
# Read the contents of the file
contents = f.read()
print(contents)
# Write to the file
f.write('This is a new line\n')
# Close the file
f.close()
#This will open the file 'file.txt' in 'r+' mode, allowing you to read from and write to the file.

#w+
#In Python, the 'w+' mode is used to open a file for both reading and writing. It allows you to read from and write to the same file.
#Unlike the 'r+' mode, the 'w+' mode will overwrite the contents of the file if it already exists. If the file does not exist, it will create a new file and open it for reading and writing.
#Here is an example of how to use 'w+' mode to open a file in Python:
# Open the file in 'w+' mode
f = open('file.txt', 'w+')
# Write to the file
f.write('This is the first line\n')
f.write('This is the second line\n')
# Move the file pointer to the start of the file
f.seek(0)
# Read the contents of the file
contents = f.read()
print(contents)
# Close the file
f.close()
#This will open the file 'file.txt' in 'w+' mode, allowing you to read from and write to the file. If the file already exists, its contents will be overwritten. If the file does not exist, a new file will be created and opened in 'w+' mode.

#a+
#In Python, the 'a+' mode is used to open a file for both reading and writing. It allows you to read from and write to the same file.
#Unlike the 'w+' mode, the 'a+' mode will not overwrite the contents of the file if it already exists. Instead, it will append new data to the end of the file. If the file does not exist, it will create a new file and open it for reading and writing.
#Here is an example of how to use 'a+' mode to open a file in Python:
# Open the file in 'a+' mode
f = open('file.txt', 'a+')
# Write to the file
f.write('This is a new line\n')
# Move the file pointer to the start of the file
f.seek(0)
# Read the contents of the file
contents = f.read()
print(contents)
# Close the file
f.close()
#This will open the file 'file.txt' in 'a+' mode, allowing you to read from and write to the file. If the file already exists, the new data will be appended to the end of the file. If the file does not exist, a new file will be created and opened in 'a+' mode.
