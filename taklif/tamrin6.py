a=float(input("vazn khod ra vared kon(kg):"))
b=float(input("ghad khod ra vared kon(cm):"))
c=a/(b**2)*10000
print (c)
if c<18.5 :
    print("kambod vazn")
elif c>=18.5 and c<24.9:
    print("Normal")
elif c>=25 and c<29.9:
    print("ezafe vazn")
elif c>=30 and c<34.9:
    print("chagh")
else :
    print("khaili chagh")
