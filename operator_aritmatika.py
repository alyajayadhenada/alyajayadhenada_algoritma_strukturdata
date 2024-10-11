# operator aritmatika
a, b = 10, 3

print(a, '+', b,'=', a + b)
print(a, '-', b,'=', a - b)
print(a, '*', b,'=', a * b)
print(a, '/', b,'=', a / b)
print(a, '%', b,'=', a % b)
print(a, '**', b,'=', a ** b)
print(a, '//', b,'=', a //b)

#operator komparasi atau perbandingan

a, b = 5, 10

print(a, '>', b, '=' , a > b)
print(a, '<', b, '=' , a < b)
print(a, '==', b, '=', a == b)
print(a, '!=',b, '=', a !=  b)
print(a, '>=', b, '=', a >= b)
print(a, '<=', b,'=', a <= b)

#operator penugasan

#penugasan pertama
a - 10
print('a = 10 -> ', a)

a += 5
print('a += 5 -> ', a)

a -= 3
print('a -= 3 -> ', a)

a *= 6
print('a *= 6 -> ', a)

a /= 8
print('a /= 8 -> ', a)

# karena a jadi float,kita ubah lagi menjadi integer
a=int(a)

a%= 9
print('a %= -> ',9)

a //= 6
print('a //= 6 -> ', a)

a **= 1
print('a **= 1 ->',  a)

#operator logika
print(True and True)

print(1 + 2 == 3 and True)
print('----')
print(False or 1 > 5)
print(False or 5 > 2)
print('----')
print(not(1 > 5))
print(not(1 < 5))

#operator keanggotan
 
perusahaan = 'microsoft'
list_pulau = ['jawa', 'sumatra', 'sulawesi']

# ini adalah dictinory,insyaallah akan kita pelajari
# di pertemuan-pertemuan yang akan datang
mahasiswa = {
    'nama' : 'Lendis Fabri',
     'asal' : 'Lamongan'
}
     


print(
    "Apakah 'c' ada di variabel perusahaan?",
    'c' in perusahaan
    )

print(
    "Apakah 'c' ada di variabel perusahaan?",
    'c' in perusahaan

)
print(
    "Apakah 'z' tidak ada di variabel perusahaan ?",
    'c' not in perusahaan

)
print(
    "Apakah 'Madura' tidak ada di variabel list_pulau?",
    'Madura' not in perusahaan

)
print(
    "Apakah atribut 'nama' ada di variabel mahasiswa?", 
    'nama' in mahasiswa
)



