# Kullanıcıdan bir sayı al
n = int(input("Bir sayı girin: "))

# Toplamı hesapla
toplam = 0
for i in range(1, n + 1):
    toplam += i

# Sonucu ekrana yazdır
print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")
