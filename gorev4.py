# Kullanıcıdan bir metin al
metin = input("Bir metin girin: ")

# Metni ters çevirme (döngü ile)
ters_metin = ""
for karakter in metin:
    ters_metin = karakter + ters_metin  # Yeni karakteri başa ekleyerek ters çevirme

# Sonucu ekrana yazdır
print(f"Ters çevrilmiş metin: {ters_metin}")
