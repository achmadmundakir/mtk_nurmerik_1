class LuasBangunDatar:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas_segitiga(self):
        return 0.5 * self.alas * self.tinggi
    def luas_jajargenjang(self):
        return self.alas * self.tinggi
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))
bangun_datar = LuasBangunDatar(alas, tinggi)
print(f"Luas Segitiga: {bangun_datar.luas_segitiga()}")
print(f"Luas Jajar Genjang: {bangun_datar.luas_jajargenjang()}")
