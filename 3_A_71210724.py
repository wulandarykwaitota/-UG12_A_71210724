a = int(input('Masukkan Pembatas : '))
b = int(input('Masukkan Angka yang dilarang : '))
for i in range(a):
    if i != b:
        print(i,end =' ')
    else:
        continue