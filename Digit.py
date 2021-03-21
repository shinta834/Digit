def digitAwal (x,y):
    # formula untuk menghitung x pangkat y
    hasilPemangkatan = x**y
    # rubah hasil pangkat dari tipe int menjadi str
    a = str (hasilPemangkatan)
    # untuk mengambil nilai dari index awal
    output1 = a[0]
    return output1

def digitAkhir (x,y):
    # formula untuk menghitung x pangkat y
    hasilPemangkatan = x**y
    # rubah hasil pangkat dari tipe int menjadi str
    a = str (hasilPemangkatan)
    # untuk mengambil nilai dari index akhir
    output2 = a[-1]
    return output2

print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))

print('')

print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))