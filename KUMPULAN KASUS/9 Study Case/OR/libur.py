minggu = False
nasional = True

libur = minggu or nasional

if libur:
    print("Sekolah tutup")
else:
    print("Sekolah buka")