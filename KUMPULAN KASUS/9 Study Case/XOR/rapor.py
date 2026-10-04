cetak = False
pdf = False

rapor = cetak ^ pdf

if rapor:
    print("Rapor diproses")
else:
    print("Pilih satu format")