import os
print("PENCUCIAN RIZQY CLEAN")
print("Selamat Datang\n")
print("========================")
nama = input("Masukan nama anda:")
print("Masukan jenis kendaraan anda")
print("A.Motor = 15.000 B.Mobil = 20.000 C.Pickup = 30.000")
pilih = input("Masukan pilihan (A/B/C) :")
#biaya cuci motor
HgMotor = 15000
HgMobil = 20000
HgPickup = 30000
#pilihan user
while(True):
    if pilih == "A":
        Hg = HgMotor
        break
    elif pilih == "B":
        Hg = HgMobil
        break
    elif pilih == "C":
        Hg = HgPickup
        break
    else:
        pilih = input("Masukan dengan huruf kapital:")


HgKendaraan = [HgMotor,HgMobil,HgPickup]
print("Layanan : 1. Biasa(+0) 2. Poles(+7000).")
layanan = input("Masukan jenis layanan :")
#biaya tarif
biasa = 0
poles = 7000

while (True):
    if layanan == "1":
        LA = biasa
        break
    elif layanan == "2":
        LA = poles
        break
    else:
        layanan = input("Masukan hanya angka (1/2):")

tot = int(Hg + LA)
print("Total bayar =",tot)
tarif = [biasa, poles]

#pelanggan
class pelanggan():
    def __init__(self,nama,pilih):
        self.nama = nama
        self.pilih = pilih

    def show(self):
        print("=====================")
        print("Hallo",self.nama,"anda harus bayar ",self.pilih)
 
pel1 = pelanggan(nama,tot)
pel1.show()
print("Terima kasih ",nama,"telah mencuci di pencucian kami")

#membuat class queue
# class queue():
# #menginisialisasi dirinya sebuah list kosong
#     def _init_(self):
#         self.items=[]
# #membuat fungsi cek apakah kosong
#     def IsEmpty(self):
#         return self.items==[]
# #membuat fungsi menambah item
#     def enqueue(self,item):
#         self.items.insert(0,item)
# #membuat fungsi mengurangi item
#     def dequeue(self):
#         return self.item.pop()
# #membuat fungsi isi queue
#     def size(self):
#         return len(self.item)
# #membuat fungsi lihat data di queue
#     def getlist(self):
#         return self.items
# 
# antri = queue
# pel1 = antri
# pel1.getlist(pel1)

#buat gui
#selesaikan looping queue
#memisahkan tamppilan

