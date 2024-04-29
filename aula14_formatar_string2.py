a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'a={0}  b={1} c={2:.2f} d={0}'
#argumento
formato = string.format(a, b, c)

#paramentro nomeado
string_2 = 'a={nome1}  b={nome2} c={nome3:.2f} d={nome1} '
formato_2 = string_2.format(nome1=a, nome2=b, nome3=c)

print(formato)
print(formato_2)