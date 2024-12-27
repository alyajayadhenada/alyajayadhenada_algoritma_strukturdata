# Menerima input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Menentukan kategori usia menggunakan percabangan
if usia <= 5:
    kategori = "Balita"
elif usia <= 12:
    kategori = "Anak-anak"
elif usia <= 17:
    kategori = "Remaja"
elif usia <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

# Menampilkan kategori usia
print(f"Kategori usia Anda: {kategori}")
