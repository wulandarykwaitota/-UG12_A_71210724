awal = int(input("Masukan Nilai Awal : "))
akhir = int(input("Masukan Nilai Akhir : "))

for x in range (awal,akhir):
    if x % 2 == 1:
            print(x, end=' ')
