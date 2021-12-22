#Writing to a Text File#

file=open("Python Test.text", "a+")
file.write("Python is a great language. \n")
file.close()
print("Name of the file: ",file.name)
