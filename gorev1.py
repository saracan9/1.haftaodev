# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri gerçekleştir
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"  # Sıfıra bölme kontrolü
mod = sayi1 % sayi2 if sayi2 != 0 else "Tanımsız"
us = sayi1 ** sayi2

# Sonuçları ekrana yazdır
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
print(f"Mod: {mod}")
print(f"Üs alma: {us}")
