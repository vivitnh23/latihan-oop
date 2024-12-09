from Data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilkanMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Ubah Data")
        print("4. Cari Data")
        print("5. Tampilkan Semua Data")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ")

        if pilihan == "1":
            nim, nama, jurusan, tahun_masuk = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan, tahun_masuk)
            data_mahasiswa.tambah_data(mahasiswa)

        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_data(nim)

        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama = input("Masukkan Nama baru: ")
            jurusan = input("Masukkan Jurusan baru: ")
            data_mahasiswa.ubah_data(nim, nama, jurusan)

        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            TampilkanMahasiswa.tampilkan_detail(mahasiswa)

        elif pilihan == "5":
            TampilkanMahasiswa.tampilkan_list(data_mahasiswa.data)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()