cod, numpecas, vunitario = input().split(" ")
cod2, numpecas2, vunitario2 = input().split(" ")

numpecas = int(numpecas)
vunitario = float(vunitario)

numpecas2 = int(numpecas2) 
vunitario2 = float(vunitario2) 

valorpagar = (numpecas * vunitario) + (numpecas2 * vunitario2)

print(f'VALOR A PAGAR: R$ {valorpagar:.2f}')