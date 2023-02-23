def same_by(characteristic, objects):
characteristic_list = [characteristic(x) for x in objects]
for i in range(len(characteristic_list)-1):
    if characteristic_list[i] != characteristic_list[i+1]:
       return False
return True

values = [-7,-5,2,1]
if same_by(lambda x: x > 0, values):
print('same')
else:
print('different')

