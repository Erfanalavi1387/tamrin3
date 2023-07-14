a=int(input("sal ra vared kon:"))
b=int(input("mah ra vared kon:"))
c=int(input("roz ra vared kon:"))
d=int(input("sal tavalod ra vared kon:"))
e=int(input("mah tavalod ra vared kon:"))
f=int(input("roz tavalod ra vared kon:"))
if c<f:
    c+=30
    b-=1

i=c-f
if b<e:
    b+=12
    a-=1
h=b-e

g=a-d 

print("sen shoma=>",g,h,i)

x=i*24*3600
y=(24*h)*3600
z=g*12*30*24*3600
print("sanie omr shoma=>",x+y+z)