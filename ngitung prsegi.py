def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# Contoh pengguna
sisi = 5
print("print persegi:", luas_persegi(sisi))
print("volume kubus:", volume_persegi(sisi))