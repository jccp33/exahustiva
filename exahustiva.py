import os
import sys

# ---------- obtener nombre sistema ---------- #
def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]
# ---------- obtener nombre sistema ---------- #

# ----------- funciones de ejemplo ----------- #
# funcion silla
# (x-5)*(x-5)*(x-5) + 1

# funcion con minimo
# (x-2)*(x-5)*(x-5)+1

# funcion con dos minimos
# (x-2)*(x-2)*(x-5)*(x-5)+1
# ----------- funciones de ejemplo ----------- #

# ------------ funcion a minimizar ----------- #
func_str = "(x-5)*(x-5) + 1"
def funcion(x):
    return (x-5)*(x-5) + 1
# ------------ funcion a minimizar ----------- #

# ------------- limpiar pantalla ------------- #
if get_platform() == "Windows":
    os.system("cls")
if get_platform() == "Linux":
    os.system("clear")
# ------------- limpiar pantalla ------------- #




# ----------- ejecucion principal ------------ #
a = float(input("a: "))
b = float(input("b: "))
e = float(input("e: "))

n  = 2 * (b - a) / e
dx = (b - a) / n
x1 = a
x2 = x1 + dx
x3 = x2 + dx

file = open("graf.dat","w")
file.write("set xrange [" + str(a) + ":" + str(b) + "]\n");
file.write("set yrange [0:10]\n");

i = a
while dx <= b:
    if funcion(x1)>=funcion(x2) and funcion(x2)<=funcion(x3):
        print("Minimo entre " + str(x1) + " y " + str(x3))
        break
    else:
        file.write("set arrow 1 from "+str(x1)+",0 to "+str(x1)+","+str(funcion(x1))+"\n")
        file.write("set arrow 2 from "+str(x2)+",0 to "+str(x2)+","+str(funcion(x2))+"\n")
        file.write("set arrow 3 from "+str(x3)+",0 to "+str(x3)+","+str(funcion(x3))+"\n")
        file.write("plot " + func_str + "\n");
        file.write("pause 0.1\n")
        file.write("refresh\n\n")
        # actualizar variables
        i = i + 1
        x1 = x2
        x2 = x3
        x3 = x2 + dx
    # finalizacion while
    if x3 > b:
        print("No existe minimo entre " + str(a) + " y " + str(b))
        break
    i = i + 1

file.write("\npause -1\n")
file.close()

os.system("gnuplot \"graf.dat\"")
# ----------- ejecucion principal ------------ #

