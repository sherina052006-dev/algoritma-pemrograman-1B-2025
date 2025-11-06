def cek_anagram(kata1, kata2):

    if kata1 == kata2:
        return False
    
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kedua kata tersebut merupakan anagram.")
else:
    print("Kedua kata tersebut bukan merupakan anagram.")