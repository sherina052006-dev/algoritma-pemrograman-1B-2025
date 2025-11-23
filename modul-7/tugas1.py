contact_book = {}

def tampilkan_semua_kontak():
    if not contact_book:
        print("\nTidak ada kontak yang tersimpan.")
    else:
        print("\n=== Daftar Semua Kontak ===")
        for nama, info in contact_book.items():
            print(f"  Nama : {nama}")
            print(f"  Nomor: {info[0]}")
            print(f"  Email: {info[1]}")

def cari_kontak():
    nama = input("Masukkan nama yang dicari: ")
    if nama in contact_book:
        print("\nKontak ditemukan:")
        print(f"Nama: {nama}")
        print(f"Nomor: {contact_book[nama][0]}")
        print(f"Email: {contact_book[nama][1]}")
    else:
        print("\nKontak tidak ditemukan.")

def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ")
    if nama in contact_book:
        print("Kontak sudah ada!")
    else:
        nomor = input("Masukkan nomor telepon: ")
        email = input("Masukkan email: ")
        contact_book[nama] = [nomor, email]
        print("\nKontak berhasil ditambahkan.")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diupdate emailnya: ")
    if nama in contact_book:
        email_baru = input("Masukkan email baru: ")
        contact_book[nama][1] = email_baru
        print("\nEmail berhasil diperbarui.")
    else:
        print("\nKontak tidak ditemukan.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in contact_book:
        del contact_book[nama]
        print("\nKontak berhasil dihapus.")
    else:
        print("\nKontak tidak ditemukan.")
        
while True:
    print("\n=== MENU CONTACT BOOK ===")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Tampilkan Semua Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        tambah_kontak()
    elif pilih == "2":
        cari_kontak()
    elif pilih == "3":
        tampilkan_semua_kontak()
    elif pilih == "4":
        update_email()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("\nPilihan tidak valid. Silakan pilih 1-6.")