
name = "fred"
# print(f"His Name is {var}".format(var=name))

print(f"His name is {name}")

libary = [('Autor', 'Topic', 'Pages'),
          ('Tom', 'Adventure', 601),
          ('124', 12312, 'yoadfa')]

for book in libary:
    print(book[0], book[1], book[2])
    
path = 'text.txt'
file = open(path, 'r')#read
text = file.read()
file.close()
file = open(path, 'w')#write
file.write('Hi')
file.close()
file = open(path, 'a+')#append
file.write('asdf')
file.write('adfkhg;igohusnidblskjnsali;efaohreguslfj')
file.close()

#file.seek(0)
#set the point to 0
