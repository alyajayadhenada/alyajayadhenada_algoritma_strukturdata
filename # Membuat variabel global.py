# Membuat variabel global
nama = "Belajar kode"
Versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.1"
    # mengakses variabel lokal
    print ("Nama: %s" % nama)
    print ("Versi: %s" % Versi)

 # mengakses variabel global
print ("Nama: %s" % nama)
print ("Versi: %s" % Versi)

# memanggil fungsi help()
help()


 
           