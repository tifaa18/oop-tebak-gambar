class TebakGambar:
    def __init__(self, gambar, kunci_jawaban, poin):
        self.gambar = gambar
        self.kunci_jawaban = kunci_jawaban.lower()
        self.poin = poin
        self.kesempatan = 3

    def tampilkan_soal(self):
        print("=== TEBAK GAMBAR ===")
        print(f"Petunjuk Gambar : {self.gambar}")
        print(f"Poin Soal      : {self.poin}")
        print(f"Kesempatan      : {self.kesempatan} kali")

    def tebak(self, jawaban_user):
        jawaban_user = jawaban_user.lower()
        if jawaban_user == self.kunci_jawaban:
            print(f"BENAR! Kamu mendapatkan {self.poin} poin!\n")
            return True
        else:
            self.kesempatan -= 1
            print(f"SALAH! Sisa kesempatan: {self.kesempatan}\n")
            return False

# --- PENGUJIAN OBJEK ---
# Membuat objek soal pertama
soal1 = TebakGambar("Kucing + Makan + Bebek", "kucing makan bebek", 100)

# Menjalankan simulasi game
soal1.tampilkan_soal()

# Simulasi tebakan salah
soal1.tebak("kucing tidur")

# Simulasi tebakan benar
soal1.tebak("kucing makan bebek")