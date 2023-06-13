name = 'Fred'

# Using the old .format() method:
print("His name is {var}.".format(var=name))

# Using f-strings, embed expressions inside a string
print(f"His name is {name}.")

# Pass `!r` to get the <strong>string representation</strong>:
# print(f'His name is {name!r}')

# work with a dict
d = {'a':123,'b':456}
print(f"Address: {d['a']} Main Street")

# work with a list 
library = [('Author', 'Topic', 'Pages'), \
           ('Tom', 'Adventure', 601), \
           ('Lori', 'Physics', 95), \
           ('Hamilton', 'Mythology', 144)]

for book in library:
    print(f'{book[0]} {book[1]} {book[2]}')

# work with txt file, reading
my_file = open('example.txt','r')

# We can now read the file
text = my_file.read()
print(text)

# But what happens if we try to read it again?
text = my_file.read()
print(text)

# Seek to the start of file (index 0)
my_file.seek(0)

# Now read again
text = my_file.read()
print(text)

# Readlines returns a list of the lines in the file
my_file.seek(0)
lines = my_file.readlines()
print(lines)

# When you have finished using a file, it is always good practice to close it.
my_file.close()


# Writing to a File
my_file = open('test.txt','w')

# Write to the file
my_file.write('This is a new first line.\n')

# always do this when you're done with a file
my_file.close()  

# Appending to a File
my_file = open('test.txt','a+')
my_file.write('This line is being appended to test.txt. \n')
my_file.write('And another line here.\n')
my_file.close()  
