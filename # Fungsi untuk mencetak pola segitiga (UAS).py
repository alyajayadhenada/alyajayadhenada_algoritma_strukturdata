# Fungsi untuk menghitung gaji per bulan
def hitung_gaji(tarif_per_jam_kerja_per_hari, hari_kerja):
    total_gaji = 0  # Variabel untuk menyimpan total gaji per bulan
    
    # Perulangan untuk menghitung gaji setiap hari kerja
    for i in range(hari_kerja):
        jam_kerja = int(input(f"Masukkan jumlah jam kerja untuk hari ke-{i+1}: "))
        
        # Jika jam kerja lebih dari 8 jam, hitung lembur
        if jam_kerja > 8:
            jam_lembur = jam_kerja - 8
            gaji_hari = (8 * tarif_per_jam_kerja_per_hari) + (jam_lembur * tarif_per_jam_kerja_per_hari * 1.5)
        else:
            # Jika jam kerja tidak lebih dari 8 jam
            gaji_hari = jam_kerja * tarif_per_jam_kerja_per_hari
        
        total_gaji += gaji_hari  # Tambahkan gaji hari ini ke total gaji
    
    return total_gaji

# Input dari pengguna
tarif_per_jam_kerja_per_hari = float(input("Masukkan tarif gaji per jam: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

# Menghitung total gaji per bulan
gaji_perbulan = hitung_gaji(tarif_per_jam_kerja_per_hari, hari_kerja)

# Menampilkan hasil
print(f"Total gaji per bulan adalah: Rp{gaji_perbulan:,.2f}")
