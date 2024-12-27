# Fungsi untuk penjumlahan
def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk perkalian
def kali(a, b):
    return a * b

# Fungsi untuk pembagian
def bagi(a, b):
    if b == 0:  # Menangani pembagian dengan nol
        return "Error! Pembagian dengan nol tidak diizinkan."
    else:
        return a / b

# Menampilkan menu pilihan operasi
print("Pilih operasi yang diinginkan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input pilihan operasi
pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Meminta input dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Memilih operasi yang sesuai dan menampilkan hasilnya
if pilihan == '1':
    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")
