
size = 10 

def bar():
    print ("#" + 4 * size * "=" + "#")

def top():
    for line in range(1, size + 1):
        print ("|" + (-2 * line + 2 * size) * " " + \
               "<>" + (4 * line - 4 )* "." + "<>" + \
               (-2 * line + 2 * size) * " " + "|")

def bottom():
    for line in range(size , 0, -1):
        print ("|" + (-2 * line + 2 * size) * " " + \
               "<>" + (4 * line - 4 ) * "." + "<>" + \
               (-2 * line + 2 * size) * " " + "|")
