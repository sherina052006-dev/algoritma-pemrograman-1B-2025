kupon = {
    "DISKON10": 10,
    "HEMAT20": 20,
    "SUPER50": 50,
}

def tampilkan_semua_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.")
    else:
        print("\n=== DAFTAR KUPON TERSEDIA ===")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}  -  Diskon: {diskon}%")

def proses_transaksi():
    try:
        total_belanja = float(input("Masukkan total belanja: "))
    except ValueError:
        print("\nTotal belanja harus berupa angka!")
        return

    kode_kupon = input("Masukkan kode kupon (jika ada): ").upper()

    if kode_kupon == "":
        print(f"\nTidak memakai kupon.\nTotal bayar: Rp {total_belanja:.2f}")
        return

    if kode_kupon in kupon:
        persen = kupon[kode_kupon]
        potongan = total_belanja * (persen / 100)
        total_bayar = total_belanja - potongan
        print("\n=== TRANSAKSI BERHASIL ===")
        print(f"Total Belanja : Rp {total_belanja:.2f}")
        print(f"Diskon        : {persen}%")
        print(f"Potongan      : Rp {potongan:.2f}")
        print(f"Total Bayar   : Rp {total_bayar:.2f}")

        del kupon[kode_kupon]
        print(f"\nKupon '{kode_kupon}' telah digunakan dan dihapus dari sistem.")
    else:
        print("\nKupon tidak valid atau sudah pernah digunakan!")

while True:
    print("\n=== MENU SISTEM KUPON DISKON ===")
    print("1. Proses Transaksi")
    print("2. Tampilkan Semua Kupon Tersedia")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        proses_transaksi()
    elif pilihan == "2":
        tampilkan_semua_kupon()
    elif pilihan == "3":
        print("\nProgram selesai. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid. Masukkan angka 1-3.")