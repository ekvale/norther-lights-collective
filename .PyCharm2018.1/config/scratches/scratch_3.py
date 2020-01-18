
files = ["myfile.txt", "your.txt", "welcome.txt"]

for i, j in enumerate(files):
    print(i, (j.split(".")[0]))




f = open("myfile.txt", 'w')

f.write("First line. \n Second line. \n")
f.close()

import Turtle

