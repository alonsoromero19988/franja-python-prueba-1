##Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número
##de años, y muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.
dinero_invertido = float(input( " ingrese el dinero que desea invertir  "))
interes=float(input("ingrese el interes porcentual anual en porcentaje:  "))
años = int(input("ingrese la cantidad de años  "))
capital_final =(dinero_invertido*(interes/100+1)**años)
capital_final=round(capital_final , 2)
capital=str(capital_final)

print("el capital final es de : " + capital)
