listKota = [
    'pangkal pinang','bogor','bekasi','bandung','solo','jogjakarta','semarang','sorong','makassar'
    ]

KotaYangDicari = input('ketik nama kota yang cari: ') 

for i, kota in enumerate(listKota):
    if kota.lower() == KotaYangDicari.lower():
        print('kota yang anda cari ada di indeks ', i)
        break
else:
    print('maaf kota yang anda cari tidak ditemukan')