from visual import sphere,color

L =4
R=0.2

for x in range(-L,L+1):
    for y in range(-L,L+1):
        for z in range(-L,L+1):
               atom =sphere(pos=[x,y,z],radius=R,color=color.green)
               if ((x+y+z)%2==0):
                   atom.visible =False
