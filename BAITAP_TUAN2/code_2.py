def box(w,h):
    print (  w * "*")  
    for i in range (h-2):
        print (("*") + (w - 2) * " " + "*")
        print (w * "*")   

print(13 * "*")
print(7 * "*")
print(35 * "*")
box(10,3)
box (5,4)