clave= "hola"
dineroEnCuenta= 6000

print ("Bienvenido")
contraseña=input ("Ingrese su contraseña ")

if (contraseña!=clave):
    suma=0
    print ("\nContraseña incorrecta")
    while(suma<3):
        contraseña=input ("Ingrese nuevamente su contraseña ")
        suma=suma+1
        print ("\nContraseña incorrecta")
    print ("\nCuenta bloqueada")

else:

    dinero=int(input("Ingresar la cantidad de dinero que desea retirar "))
    if (dineroEnCuenta<dinero):
         print ("Saldo insuficiente")
    else:
        mil=dinero//1000
        resto_mil=dinero%1000
        quin=resto_mil//500
        resto_quin=resto_mil%500
        dosc=resto_quin//200
        resto_dosc=resto_quin%200
        cien=resto_dosc//100
        resto_cien=resto_dosc%100
        cincu=resto_cien//50
        resto_cincu=resto_cien%50
        print ("Usted debe recibir")
        if (mil!=0):
         print (mil,"billetes de $1000")
        if(quin!=0):
         print (quin,"billetes de $500")
        if (dosc!=0):
         print(dosc,"billetes de $200")
        if (cien!=0):
         print (cien,"billetes de $100")
        if (cincu!=0):
         print (cincu,"Billetes de $50")
        if (resto_cincu!=0):
         print ("$",resto_cincu,"quedan en la cuenta")



