inventaris = {}

def tampilkan_semua_barang():
    if not inventaris:
        print("\nTidak ada data barang.")
    else:
        print("\n=== DAFTAR SEMUA BARANG ===")
        print(f"{'ID':5} {'Nama Barang':25} {'Harga':10} {'Stok':5}")
        for id_barang, info in inventaris.items():
            print(f"{id_barang:5} {info[0]:20} {info[1]:10} {info[2]:7}")

def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ")
    if id_barang in inventaris:
        info = inventaris[id_barang]
        print("\nBarang ditemukan:")
        print(f"ID    : {id_barang}")
        print(f"Nama  : {info[0]}")
        print(f"Harga : {info[1]}")
        print(f"Stok  : {info[2]}")
    else:
        print("\nBarang tidak ditemukan.")

def tambah_barang():
    id_barang = input("Masukkan ID barang baru: ")
    if id_barang in inventaris:
        print("ID sudah ada! Gunakan ID lain.")
    else:
        nama = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
        inventaris[id_barang] = [nama, harga, stok]
        print("\nBarang berhasil ditambahkan.")

def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")

    if id_barang in inventaris:
        try:
            tambahan_stok = int(input("Masukkan perubahan stok : "))
            stok_baru = inventaris[id_barang][2] + tambahan_stok
            if stok_baru < 0:
                print("\nGagal! Stok tidak boleh negatif.")
            else:
                inventaris[id_barang][2] = stok_baru
                print("\nStok berhasil diperbarui.")
        except ValueError:
            print("\nInput stok harus berupa angka!")
    else:
        print("\nBarang tidak ditemukan.")

def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("\nBarang berhasil dihapus.")
    else:
        print("\nBarang tidak ditemukan.")

while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tambah Barang Baru")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tampilkan Semua Barang")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
       tampilkan_semua_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("\nProgram selesai. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid. Silakan masukkan angka 1-6.")