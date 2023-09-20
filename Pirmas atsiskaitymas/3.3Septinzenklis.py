# Septinzenklio skaiciaus 1,3,5,7 sandauga ir likusiu sumos skaiciuokle.

sk = int(input('Iveskite septinzenkli skaiciu... '))
x1 = sk // 1000000
x2 = sk // 100000 % 10
x3 = sk // 10000 % 10
x4 = sk // 1000 % 10
x5 = sk // 100 % 10
x6 = sk // 10 % 10
x7 = sk % 10
suma = x1*x3*x5*x7+x2+x4+x6
print(f'skaiciaus {sk} 1,3,5,7 sandauga ir likusiu suma {suma} ')
