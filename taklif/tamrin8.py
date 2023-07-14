a=float (input("adad1 ra vared kon :"))
b=float(input("adad2 ra vared kon:"))
c=float(input("adad3 ra vared kon:"))
if a>b and a>c :
    print("adad aval",a)
elif b>a and b>c:
    print("adad aval ",b)
elif c>a and c>b:
    print("adad aval ",c)
if a<b and a>c:
    print("adad 2 :",a)
elif a<c and a>b :
    print("adad 2 :",a)
elif b<a and b>c:
    print("adad2:",b)
elif b>a and b<c:
    print("adad2:",b)
elif c>a and c<b:
    print("adad 2:",c)
elif c>b and c<a:
    print("adad 2:",c)
if a<b and c :
    print("adad3:",a)
elif b<a and c :
    print("adad 3:",b)
elif c<a and b :
    print("adad3:",c) 