total_gaji = 0
total_lembur = 0
total_bonus = 0
total_gajilembur = 0

for hari in range(1, 8):
    print(f"\n Hari ke-{hari}")

    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
            else:
                break
        except ValueError:
             print("Input tidak valid! Masukkan angka jam lembur dengan benar.")

    while True:
        shift = input("Apakah shift malam? (y/n): ")
        if shift in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    gaji_pokok = 100_000
    lembur = 0

    if jam_lembur == 0:
        lembur = 0
    elif 1 <= jam_lembur <= 3:
        lembur = 25_000 * jam_lembur
    elif jam_lembur == 4:
        lembur = 100_000
    elif jam_lembur == 6:
        lembur = 200_000
    elif jam_lembur == 8:
        lembur = 300_000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    bonus = 50_000 if shift == 'y' else 0

    total_lembur += jam_lembur
    total_bonus += bonus
    total_gaji += gaji_pokok + lembur + bonus
    total_gajilembur += lembur
    
print("\nRekapitulasi Gaji Mingguan Pak Wowo")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")
print(f"Total gaji lembur: Rp{total_gajilembur}")