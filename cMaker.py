import sys
from subprocess import call

nome = sys.argv[1]
name = nome[0:-4]
#Abre novo arquivo
f = open("CMakeLists.txt","w")
#Faz o arquivo
f.write("cmake_minimum_required(VERSION 2.8)\n")
f.write("project( " + name + " )\n")
f.write("find_package( OpenCV REQUIRED )\n")
f.write("add_executable(" + name + " " + nome + " )\n")
f.write("target_link_libraries(" + name +  " ${OpenCV_LIBS} )\n")
f.close()
#Chama cmake e make para fazer o executavel
call(["cmake","."])
call("make")
