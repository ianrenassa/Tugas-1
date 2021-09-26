teori = float(input("Nilai Ujian Teori = "))
praktik = float(input("Nilai Ujian Praktik = "))

if teori >= 70 and praktik >= 70:
    print("Selamat, anda lulus!")
elif teori >= 70 and praktik < 70:
    print("Anda harus mengulang ujian praktik.")
elif teori < 70 and praktik >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktik.")