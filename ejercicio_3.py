## Escribir un programa que haga transformaciones de pesos a dólares. Debe preguntarle al usuario si desea
## transformar de pesos mexicanos a dólares, de pesos chilenos a dólares, o desde pesos argentinos a dólares.
## Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares.
#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115
dolar_chile= 855
dolar_mex=20
dolar_argentino=115
print ("seleccione que moneda desea transformar a dolar")
print(" ingrese 1 si desea trasformar a peso chileno")
print(" ingrese 2 si desea trasformar a peso mexicano")
print(" ingrese 3 si desea trasformar a peso argentino")
numero=int(input("ingrese su opcion  "))
pesos=float(input("ingrese el valor de su moneda a trasformar "))
if numero == 1:
    dolares_chilenos=pesos/dolar_chile
    valor1=str(dolares_chilenos)
    print(" el numero de dolares es : " + valor1)
elif numero == 2:
    dolares_mexicanos=pesos/dolar_mex
    valor2=str(dolares_mexicanos)
    print(" el numero de dolares es  : " + valor2)
elif numero==3:
    dolares_argentinos=pesos/dolar_argentino
    valor3=str(dolares_argentinos)
    print(" el numero de dolares es : " + valor3)


     
    
     