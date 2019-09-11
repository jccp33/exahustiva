import os

# funcion silla
# (x-5)*(x-5)*(x-5) + 1

# funcion con minimo
# (x-2)*(x-5)*(x-5)+1

# funcion con dos minimos
# (x-2)*(x-2)*(x-5)*(x-5)+1

func_str = "(x-5)*(x-5) + 1"
def funcion(x):
    return (x-5)*(x-5) + 1

os.system("clear")
a = input("a: ")
b = input("b: ")
e = input("e: ")

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
