from __future__ import division
def potencia10(n):
    while n%10 ==0:
        n=n/10
    return False if n == 1  else True

def operadoresValidos(operador):
    ops = {'+':True,'-':True,'*':True,'/':True,'%':True} 
    return ops.has_key(operador) == False

primer = 5
while potencia10(primer):
    primer = input("Teclea un primer numero potencia de 10, maximo 1000000\n")

operador = '?'

while operadoresValidos(operador):
    operador = raw_input("Teclea el operador \n")

segundo = 5

while potencia10(segundo):
    segundo = input("Teclea un segundo numero potencia de 10, maximo 1000000\n")

respuesta =0

if operador == "+":
    respuesta = primer + segundo
elif operador == '-':
    respuesta = primer - segundo
elif operador == '*':
    respuesta = primer / segundo
elif operador == '/':
    respuesta = primer / segundo
elif operador == '%':
    respuesta = primer % segundo
if operador == '/':
    print("%d %s %d = %f"%(primer,operador,segundo,respuesta)) 
else:
    print("%d %s %d = %d"%(primer,operador,segundo,respuesta))
