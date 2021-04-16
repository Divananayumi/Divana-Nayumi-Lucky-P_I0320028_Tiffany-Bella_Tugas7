str = "Program Menghitung Jumlah Pesanan Makanan"
s = str.center(61,'*')
print(s)

nama_pemesan = input("Nama pemesan :")
print("Selamat datang", nama_pemesan)

print("\nMenu makanan : BAKSO, MIE AYAM, SOTO")
str = input("Masukkan menu makanan yang dipesan dengan menuliskan nama menu sebanyak jumlah yang dipesan :")
pesanan =str.upper()
print("Pesanan: ", pesanan)

str = pesanan
x = str.count('BAKSO')
y = str.count('MIE AYAM')
z = str.count('SOTO')
print("JUMLAH BAKSO: ", x)
print("JUMLAH MIE AYAM: ", y)
print("JUMLAH SOTO: ", z)