class TampilkanMahasiswa:
    @staticmethod
    def tampilkan_list(data):
        print("\nDaftar Mahasiswa:")
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            for mahasiswa in data:
                print(mahasiswa)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\nDetail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")