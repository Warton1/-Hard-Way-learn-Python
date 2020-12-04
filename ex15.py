from sys import argv
(script, filename) = argv 
txt = open(filename)

print ("ex15_sample.txt %r:" % filename)
print(txt.read())

print ("Type the filename again: ex15_example.txt")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())