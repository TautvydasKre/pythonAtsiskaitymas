# skritulio turio skaiciuokle
import math

ia = float(input('Iveskite indo auksti... '))
irk = float(input('Iveskite indo skersmeni... '))
rd1 = float(input('Iveskite pirmo rutulio skersmeni... '))
rd2 = float(input('Iveskite antro rutulio skersmeni... '))
sr1 = rd1/2
sr2 = rd2/2
isk = irk/2

rt1 = (4/3 * (math.pow(sr1, 3)) * math.pi)
rt2 = (4/3 * (math.pow(sr2, 3)) * math.pi)
ct = (math.pi * (math.pow(isk, 2)) * 10)
st = ct - rt1 - rt2
print(rt1, rt2, st)
