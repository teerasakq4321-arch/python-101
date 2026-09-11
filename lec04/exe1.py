print("KPH\tMPH")
print("--------------")

for KPH in range(60,140):
    MPH =KPH * 0.6214
    print(KPH,'\t',format(MPH,'.2f'))
    