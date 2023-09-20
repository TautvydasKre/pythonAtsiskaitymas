# decimetru skaiciuokle.

dm = int(input('Iveskite decimetrus '))
km = dm // 10000
likutis = dm % 10000
m = likutis // 10
liko = likutis % 10
print(f'Verciant decimetrus gavome {km} KM {m} M ir liko {liko} DM')
