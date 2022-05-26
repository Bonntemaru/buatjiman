import os
def awal():
    os.system("CLS")
    print("PENCUCIAN RIZQY CLEAN")
    print("Selamat Datang\n")
    print("="*30)
    nama = input("Masukan nama anda:")
    print("Masukan jenis kendaraan anda")
    print("A.Motor = 15.000 B.Mobil = 20.000 C.Pickup = 30.000")
    pilih = input("Masukan pilihan (A/B/C) :")
    biaya(pilih)
#biaya cuci motor
def biaya(pilih):
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
#membuat class queue
class queue():
#menginisialisasi dirinya sebuah list kosong
    def _init_(self):
        self.items=[]
        self.size = 0
        self.current_size = 0
#membuat fungsi cek apakah kosong
    def IsEmpty(self):
        if self.current_size == 0:
            return True
        else:
            return False
#membuat fungsi cek apakah penuh
    def IsFull(self):
        if self.current_size == self.size:
            return true
        else:
            return fals
#membuat fungsi menambah item
    def enqueue(self,item):
        os.system("cls")
        print(30*"=")
        print("<== Tambah Antrian ==>")
        print(30*"=")
        if self.size == 0:
            print("antrian belum ada")
            cek =input("lanjut buat antrian?(Y/N)")
            cek = cek.upper()
            if cek == "Y":
                n = int(input("Masukan panjang antrian:"))
                self.size = n
                print("antrian telah dibuat!!")
                print("tekan [Enter] untuk kembali ke menu utama")
                input()
                awal()
            else:
                print("tekan [Enter] untuk kembali ke menu utama")
                input()
                awal()
        elif self.IsFull():
            print("antrian telah penuh")
        else:
            databaru = input("nama pelanggan:")
            databaru = databaru.upper()
            self.data.append(databaru)
            self.current_size = len(self.data)
        for i in range(self.size):
            print (" [%2d] "%(self.size - i), end="")
        print()
        for i in range(self.size):
            print(25*"=" ,end="")
        print()
        sisakosong = self.size - self.current_size
        for i in range(self.size):
            if sisakosong > i:
                print(" %10s"%(""),end="")
            else:
                print(" %10s "%(self.data(self.size - 1 - i)), end="")
        print("<<==COSTUMER SERVICE==>>")
        for i in range(self.size):
                print(30*"=" /n)
        print(databaru,"mulai mengantri")
        print("pada urutan",self.current_size)
        waktutunggu = self.current_size * 15
        print("estimasi : ",waktutunggu, "menit")
    print("Tekan [Enter] untuk kembali ke menu utama")
    input()
    awal()

#membuat fungsi mengurangi item
    def dequeue(self):
        os.system("cls")
        if self.IsEmpty():
            print("tidak ada yang mengantri")
            print("Tekan [Enter] untuk kembali ke menu utama")
            input()
            awal()
        else:
            datakeluar = self.data.pop(0)
            self.current_size = len(self.data)
            print("<== Terima Kasih ==> ")
            print(datakeluar,"sudah mencuci di tempat kami")
            for i in range(self.size):
                print(" [%2d] " (self.size -1), end="")
            print(25*"=")
            sisakosong = self.size - self.current_size
            for i in range(self.size):
                if sisakosong > i:
                    print(" %10s" % (""), end="")
                else:
                    print(" %10s " % (self.data(self.size - 1 - i)), end="")
            print("<<==COSTUMER SERVICE==>>")
            for i in range(self.size):
                print(30 * "=" / n)
            print(databaru, "mulai mengantri")
            print("pada urutan", self.current_size)
            waktutunggu = self.current_size * 15
            print("estimasi : ", waktutunggu, "menit")
        print("Tekan [Enter] untuk kembali ke menu utama")
        input()
        awal()

#membuat fungsi isi queue
    def size(self):
        os.system("cls")
        print(30*"=")
        n = int(input("masukan batas antrian:"))
        if n < self.current_size:
            print("KAPASITAS TIDAK BOLEH MINES!!")
        else:
            self.size = n
            print("batas diperbaharui!!")
#membuat fungsi lihat data di queue
    def getlist(self):
        return self.items

#pelanggan
# class pelanggan():
#     def __init__(self,nama,pilih):
#         self.nama = nama
#         self.pilih = pilih

    def show(self):
        os.system("cls")
        print("<== status antrian ==>")
        cari = input("masukan nama:")
        item = cari.upper()
        for i in self.data:
            if item in i:
                index = self.data.index(item)
                break
            else:
                continue

        for i in range(self.size):
            print(" [%2d] "%(self.size - i),end="")

        for i in range(self.size):
            print(" [%2d] "(self.size - 1), end="")
        print(25 * "=")
        sisakosong = self.size - self.current_size
        for i in range(self.size):
            if sisakosong > i:
                print(" %10s" % (""), end="")
            else:
                print(" %10s " % (self.data(self.size - 1 - i)), end="")
        print("<<==COSTUMER SERVICE==>>")
        for i in range(self.size):
            print(30 * "=" / n)
        print(databaru, "mulai mengantri")
        print("pada urutan", self.current_size)
        waktutunggu = self.current_size * 15
        print("estimasi : ", waktutunggu, "menit")

    print("Tekan [Enter] untuk kembali ke menu utama")
    input()
    awal()

def hapusAntrian():
    q.dequeue()
def tambahAntrian():
    q.enqueue()
def keluar():
    os.system("cls")
    print("<== terimakasih ==>")
def lihatAntrian():
    q.show()
def tambahKapasitas():
    q.size()

#buat gui
#selesaikan looping queue
#memisahkan tamppilan

