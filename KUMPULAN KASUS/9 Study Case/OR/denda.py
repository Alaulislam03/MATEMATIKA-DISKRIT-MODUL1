telat = True
rusak = False

denda = telat or rusak

if denda:
    print("Bayar denda")
else:
    print("Bebas denda")