def gabung_tuple(t1, t2):
    gabung = t1 + t2
    
    unik = []
    for angka in gabung:
        if angka not in unik:
            unik.append(angka)
    
    for i in range(len(unik)):
        for j in range(i + 1, len(unik)):
            if unik[i] < unik[j]:
                unik[i], unik[j] = unik[j], unik[i]
    
    return tuple(unik)

t1 = (3, 1, 4)
t2 = (1, 5, 9)
hasil = gabung_tuple(t1, t2)

print("Hasil akhir_tuple:", hasil)