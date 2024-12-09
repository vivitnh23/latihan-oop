class Mahasiswa:
    def _init_(self, nim, nama, jurusan, tahun_masuk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk
    
    def _str_(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}, Tahun Masuk: {self.tahun_masuk}"

class DataMahasiswa:
    def _init_(self):
        self.mahasiswa_list = []

    def tambah_data(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        tahun_masuk = input("Masukkan Tahun Masuk: ")
        
        mahasiswa = Mahasiswa(nim, nama, jurusan, tahun_masuk)
        self.mahasiswa_list.append(mahasiswa)
        print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")
    
    def hapus_data(self):
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                self.mahasiswa_list.remove(mahasiswa)
                print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.\n")
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.\n")
    
    def cari_data(self):
        nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                print(mahasiswa)
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.\n")
    
    def ubah_data(self):
        nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                print("Data mahasiswa ditemukan.")
                nama = input(f"Masukkan Nama baru (kosongkan jika tidak ingin mengubah): ")
                if nama:
                    mahasiswa.nama = nama
                
                jurusan = input(f"Masukkan Jurusan baru (kosongkan jika tidak ingin mengubah): ")
                if jurusan:
                    mahasiswa.jurusan = jurusan
                
                tahun_masuk = input(f"Masukkan Tahun Masuk baru (kosongkan jika tidak ingin mengubah): ")
                if tahun_masuk:
                    mahasiswa.tahun_masuk = tahun_masuk
                
                print(f"Data mahasiswa dengan NIM {nim} berhasil diubah.\n")
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.\n")

# Fungsi untuk menampilkan menu pilihan
def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")

# Program utama
data_mahasiswa = DataMahasiswa()

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data_mahasiswa.tambah_data()
    elif pilihan == "2":
        data_mahasiswa.cari_data()
    elif pilihan == "3":
        data_mahasiswa.ubah_data()
    elif pilihan == "4":
        data_mahasiswa.hapus_data()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")