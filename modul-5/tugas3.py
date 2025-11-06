def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else: 
        tunjangan = 0

    pajak = 0.05 * gaji_pokok

    gaji_bersih = gaji_pokok + tunjangan - pajak
    print("Nama karyawan :", nama)
    print("jabatan       :", jabatan)
    print("Gaji pokok    :", gaji_pokok)
    print("Tunjangan     :", tunjangan)
    print("Pajak         :", pajak)
    print("Gaji bersih   :", gaji_bersih)
    
nama = input("Masukkan nama: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: Rp "))

hitung_gaji_bersih(nama, jabatan, gaji_pokok)