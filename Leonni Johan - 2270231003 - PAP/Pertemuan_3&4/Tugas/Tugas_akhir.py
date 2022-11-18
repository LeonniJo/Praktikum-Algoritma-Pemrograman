import time
from datetime import datetime
sekarang = datetime.now()
str(sekarang)
print("""
========================================================================
                    Kokoro Kuroe Bookstore
               Jln. Kologad Jatirahayu No.10
                Pondok Melati - Kota Bekasi
                   Telp : 0821-2345-6789 
=========================================================================""")
print("""Daftar Buku yang Tersedia
+==================================+===================+
|No| JUDUL BUKU                    | HARGA             |
+==================================+===================+
| 1.| Be Happy                     | Rp 30.000         |
| 2.| Madilog                      | Rp 120.000        |
| 3.| Origin                       | Rp 150.000        |
| 4.| Laut Bercerita               | Rp 120.000        |
| 5.| Dunia Sophie                 | Rp 120.000        |
| 6.| Yes To Live                  | Rp 80.000         |
| 5.| Sherlock Holmes Series       | Rp 60.000         |
| 6.| Pulang                       | Rp 150.000        |
| 7.| Filosofi Teras               | Rp 80.000         |
| 8.| Innovators                   | Rp 200.000        |
| 9.| Mindset                      | Rp 80.000         |
|10.| Filosofi Kopi                | Rp 80.000         |
+==================================+===================+""")
print("Masukan identitas pembeli")
nama=input ("Nama Pembeli                       : ")
alamat=input("Alamat                             : ")
notelp=input("Masukan No. Telp                   : ")

gudang={"Be Happy": 30000,"Madilog": 120000,"Origin": 150000,"Laut Bercerita": 120000,"Dunia Sophie": 120000,"Yes To Live": 80000,"Sherlock Holmes Series": 480000,"Pulang": 150000,"Filosofi Teras": 80000,"Innovators": 200000,"Mindset": 80000, "Filosofi Kopi": 80000 }

keranjang = []
total = []

def kasir():
    jawaban_pembeli = input("Silahkan masukan judul buku yang ingin dibeli? ")
    while jawaban_pembeli != "tidak":
        if jawaban_pembeli in gudang:
            keranjang.append(jawaban_pembeli)
            jawaban_pembeli = input("Berhasil ditambahkan! Ada tambahan lagi?" 
            "(Ketik 'tidak' untuk membayar)")
        else:
            jawaban_pembeli = input("Maaf, judul buku yang kamu ketik tidak tersedia. Mohon masukan judul buku yang tersedia." 
            "(Ketik 'tidak' untuk membayar)")
kasir()

print("Ini adalah daftar buku yang dipesan : ",keranjang)

jawaban = input("Apakah kamu ingin menambahkan pesanan buku lagi? (Ketik ya/tidak)")

if jawaban == "ya":
    kasir()
    print("Ini adalah daftar buku yang dipesan : ", keranjang)
    for buku in keranjang:
        total.append(gudang[buku])
    harga_yang_dibayar = sum(total)
else:
    for buku in keranjang:
        total.append(gudang[buku])
    harga_yang_dibayar = sum(total)


ppn = int(harga_yang_dibayar * 0.05)
total_belanja = int(ppn + harga_yang_dibayar)
print            ("Total belanja            :",total_belanja)

bayar = int(input("Uang yang dibayar        : "))

kembalian = int(bayar-total_belanja)
kurang = int(total_belanja-bayar)
if bayar > total_belanja:
    print ("Kembalian                :",kembalian)
elif bayar == total_belanja:
    print("Uang anda pas, Terimakasih telah berbelanja di toko buku kami.")
else:
    print("Maaf uang anda kurang ",kurang)

print("Memproses struk belanja...")
time.sleep(3)
print("\n")
print("=" * 80)
print("                                 STRUK PEMBELIAN BUKU")
print("""                                Kokoro Kuroe Bookstore
                            Jln. Kologad Jatirahayu No.10
                             Pondok Melati - Kota Bekasi""")
print("="*80)
print("No. Struk                : KK22702310003")
print("Tanggal                  :",sekarang.today())
print("Nama Pembeli             :",nama)
print("Alamat                   :",alamat)
print("No.Telp                  :",notelp)
print("Judul Buku yang Dibeli   :",keranjang)
print("-------------------------------------------------------------------------------")
print("         Total Harga Buku    : Rp {}".format(harga_yang_dibayar))
print("         PPN                 : Rp {}".format(ppn))
print("         Total               : Rp {}".format(total_belanja))
print("         Uang yang dibayar   : Rp {}".format(bayar))
print("         Kembalian           : Rp {}".format(kembalian))
print("-------------------------------------------------------------------------------")
print("""===============TERIMA KASIH SUDAH MEMBELI BUKU DI TOKO KAMI==================
Untuk Informasi Lebih Lanjut Silahkan Hubungi :
Telp/WA.0821-2345-6789
Email : kokuroebookstore@gmail.com
Instagram : kokubookstore.id
""")