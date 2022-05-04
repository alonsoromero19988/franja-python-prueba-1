##una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
##Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu
##programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
##coste final total.
valor_pan=3.49
pan_del_dia=str(valor_pan)
Pan_no_del_dia= valor_pan*0.6
pan_añejo=str(Pan_no_del_dia)
print("el precio del pan del dia es:  "+ pan_del_dia)
print(" el precio del pan que no es del dia es de " + pan_añejo)

numero_panes= int(input("ingrese el numero de panes  "))
valor_pan_añejo= numero_panes*Pan_no_del_dia
valor_añejo=str(valor_pan_añejo)
print(" el precio final del pan que no es del dia es :" + valor_añejo)

valor_del_dia = valor_pan*numero_panes
valor_dia= str(valor_del_dia)
print("el precio del pan del dia es : "+ valor_dia)

descuento= valor_del_dia - valor_pan_añejo
descuento1=str(descuento)
print("El descuento es de : " + descuento1)

