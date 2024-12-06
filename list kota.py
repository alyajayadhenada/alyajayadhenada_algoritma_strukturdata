listkota = [
    'jakarta', 'surabaya', 'depok', 'bekasi', 'solo', 'jogjakarta', 'semarang', 'pangkalpinang', 
]

kotaYangDicari = input('masukkan nama kota yang dicari: ')
 
i = 0
while i < len(listkota):
    if listkota [i].lower() == kotaYangDicari.lower():
        print('Ketemu di index', i)
        break
    print('Bukan ', listkota[i])
    i += 1
else:
    print('Maaf, kota yang anda cari tidak ditemukan. ')