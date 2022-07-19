#Simula un cajero automático con pedido de clave y bloqueo


clave= "hola"
dineroEnCuenta= 6000

print ("Bienvenido")
contraseña=input ("Ingrese su contraseña ")

#Si la contraseña no es correcta

if (contraseña!=clave):
    suma=0
    print ("\nContraseña incorrecta")
    while(suma<3):                                               #Si se ingresa 3 veces mal la contaseña se bloquea la cuenta
        contraseña=input ("Ingrese nuevamente su contraseña ")
        suma=suma+1
        print ("\nContraseña incorrecta")
    print ("\nCuenta bloqueada","\nGracias por usas nuestros servicios")

else:

    dinero=int(input("Ingresar la cantidad de dinero que desea retirar "))

    if (dineroEnCuenta<dinero):                     #Si el dinero que se desea retirar es mayor al que hay en la cuenta
         print ("Saldo insuficiente","\nGracias por usas nuestros servicios")
    else:                                           #Si el saldo que se desea retirar es inferior al que hay en la cuenta
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
    print ("\nGracias por usas nuestros servicios")


