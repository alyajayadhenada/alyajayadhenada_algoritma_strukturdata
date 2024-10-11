list_buah = ['Duren','Jambu','Pisang','Apel']
print('list_buah:', list_buah)
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

list_buah[0] = 'naga'
print(list_buah)
list_buah.append('Jambu Monyet')
print(list_buah)

list_buah[0] = 'mangga'
print(list_buah)


list_buah.pop()
'Jambu Monyet'
print(list_buah)

list_buah.remove('mangga')
print(list_buah)

del list_buah[0]
print(list_buah)

list_buah.sort()
print(list_buah)