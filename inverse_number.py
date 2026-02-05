# Programa para invertir un numero de 4 digitos

print("---------------------------------------")
print("inversión y descomposición de un Número de 4 Digitos")
print("---------------------------------------")

#--------------------------------------------------
# input
#--------------------------------------------------

n = int(input("Digite un número de 4 digitos: "))

#--------------------------------------------------
# processing
#--------------------------------------------------

r4 = n%10
r3 = (n//10)%10
r2 = (n//100)%10
r1 = (n//1000)%10

ni = r4*1000 + r3*100 + r2*10 + r1


#--------------------------------------------------
# output 
#--------------------------------------------------

print("-----------------------")
print("------RESUTADO---------")
print("-----------------------")

print("Numero original: " + str(n))
print("Ultimo digito: " + str(r4))
print("Tercer digito: " + str(r3))
print("Segundo digito: " + str(r2))
print("Primer digito: " + str(r1))
print("El numero invertido es: " + str(ni))