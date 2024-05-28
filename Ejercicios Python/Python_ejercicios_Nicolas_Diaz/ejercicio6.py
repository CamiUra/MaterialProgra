n1=int(input("Ingrese el primero numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))
if n1>n2 and n1>n3:
    print(n1, " es el mayor")
else:
    if n2>n1 and n2>n3:
        print(n2, " es el mayor")
    else:
        if n3>n1 and n3>n2:
            print(n3, " es el mayor")
if n1<n2 and n1<n3:
    print(n1, " es el menor")
else:
    if n2<n1 and n2<n3:
        print(n2, " es el menor")
    else:
        if n3<n1 and n3<n2:
            print(n3, " es el menor")