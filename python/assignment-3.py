f = open("file.txt","w+")
f.write("This is first line\n")
f.write("This is second line")
f.seek(0)
print(f.read())
        