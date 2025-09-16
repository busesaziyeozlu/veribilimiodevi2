# =============================================================================
# Soru 1 – Sayı Analizi
# Kullanıcıdan bir sayı isteyin.
# • Sayı pozitif, negatif ya da sıfır mı kontrol edin.
# • Aynı zamanda tek/çift olup olmadığını da belirtin.
# • Çıktı örneği: "Pozitif Çift" veya "Negatif Tek" gibi.
# =============================================================================

number=int(input("Sayı giriniz:"))
if number>0:
    situation="Pozitif"
elif number<0:
    situation="Negatif"
else:
    situation="Sıfır"
    
if number %2==0:
    situation +=" Çift"
else:
    situation +=" Tek"
print(situation)   

# =============================================================================
# Soru 2 – Harf Frekansı (String)
# Kullanıcıdan bir kelime alın.
# • Hangi harften kaç tane geçtiğini bulun.
# • Sonucu dictionary olarak gösterin.
# Örnek: "data" → {'d': 1, 'a': 2, 't': 1}
# =============================================================================

kelime = input("Bir kelime giriniz: ")

frekans = {}

for harf in kelime:
    if harf in frekans:
        frekans[harf] += 1
    else:
        frekans[harf] = 1

print(frekans)
   
from collections import Counter

kelime = input("Bir kelime giriniz: ")
frekans = Counter(kelime)

print(dict(frekans))

# =============================================================================
# Soru 3 – Şifre Kontrolü (String Metotları)
# Kullanıcıdan şifre girmesini isteyin. Şifre:
# • En az 8 karakter olmalı
# • En az 1 büyük harf içermeli
# • En az 1 rakam içermeli
# Koşulları sağlayıp sağlamadığına göre kullanıcıyı bilgilendirin
# =============================================================================
password = input("Şifrenizi giriniz: ")
uzunluk = len(password) >= 8
buyuk_harf = any(ch.isupper() for ch in password)
rakam = any(ch.isdigit() for ch in password)

if uzunluk and buyuk_harf and rakam:
    print("Şifre geçerli ")
else:
    print("Şifre geçersiz ")
    if not uzunluk:
        print("- Şifre en az 8 karakter olmalı.")
    if not buyuk_harf:
        print("- Şifre en az 1 büyük harf içermeli.")
    if not rakam:
        print("- Şifre en az 1 rakam içermeli.")


# =============================================================================
# Soru 4 – Liste İşlemleri
# [12, 4, 9, 25, 30, 7, 18] listesini kullanın.
# • Listenin ortalamasını bulun.
# • Ortalamadan büyük sayıları ayrı bir listeye atın.
# • Sonucu ekrana yazdırın.
# 
# ============================================================================
sayilar = [12, 4, 9, 25, 30, 7, 18]
ortalama = sum(sayilar) / len(sayilar)
print("Listenin ortalaması:", ortalama)
buyukler = [sayi for sayi in sayilar if sayi > ortalama]
print("Ortalamadan büyük sayılar:", buyukler)

#Soru 5 – Nested Loop (Desen)

for i in range(1, 6):      
    for j in range(i):      
        print("*", end="")  
    print()                 

# =============================================================================
# Soru 6 – While Döngüsü
# Kullanıcıdan sürekli sayı isteyin.
# • Kullanıcı 0 girdiğinde program dursun.
# • Girilen tüm sayıların toplamını ve ortalamasını yazdırın.
# =============================================================================

toplam = 0
adet = 0

while True:
    sayi = int(input("Bir sayı giriniz (çıkmak için 0): "))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1

if adet > 0:
    ortalama = toplam / adet
    print("Girilen sayıların toplamı:", toplam)
    print("Girilen sayıların ortalaması:", ortalama)
else:
    print("Hiç sayı girilmedi.")

# =============================================================================
# Soru 7 – Palindrom Kontrolü
# Kullanıcıdan bir kelime isteyin.
# • Kelimenin palindrom olup olmadığını kontrol edin.
# • Örnek: "kayak" → Palindrom , "python" → Değil
# =============================================================================
kelime = input("Bir kelime giriniz: ")

tersi = kelime[::-1]

if kelime == tersi:
    print(f'"{kelime}" → Palindrom ')
else:
    print(f'"{kelime}" → Palindrom değil ')
# =============================================================================
# Soru 8 – List Comprehension
# 1’den 100’e kadar olan sayılardan:
# • Hem 3’e hem 5’e bölünebilenlerin karelerini içeren bir liste oluşturun.
# • Sonucu ekrana yazdırın
# =============================================================================

liste2= [sayi**2 for sayi in range(1, 101) if sayi % 3 == 0 and sayi % 5 == 0]

print("3 ve 5'e bölünebilen sayıların kareleri:", liste2)

# =============================================================================
# Soru 9 – String İşlemleri
# Bir cümle alın.
# • Cümledeki kelimeleri split() ile ayırın.
# • Her kelimenin ilk harfini büyük yaparak yeni bir string oluşturun.
# • Örnek: "python veri bilimi" → "Python Veri Bilimi"
# =============================================================================

cumle = input("Bir cümle giriniz: ")
yeni_cumle = " ".join([kelime.capitalize() for kelime in cumle.split()])
print("Yeni cümle:", yeni_cumle)

#Mini Proje – Film Yorumu Analizi
# Film Yorumları Analizi

# Kullanıcıdan yorumları al (örnek olarak 5 yorum)
yorumlar = []
adet = int(input("Kaç yorum gireceksiniz? "))

for i in range(adet):
    yorum = input(f"{i+1}. yorumu giriniz: ")
    yorumlar.append(yorum)

# Her yorumun uzunluğu
uzunluklar = [len(y) for y in yorumlar]

# "iyi" geçen yorum sayısı (küçük/büyük harf farkını önlemek için lower() kullandık)
iyi_sayisi = sum("iyi" in y.lower() for y in yorumlar)

# En uzun ve en kısa yorum
en_uzun = max(yorumlar, key=len)
en_kisa = min(yorumlar, key=len)

# Ortalama uzunluk
ortalama = sum(uzunluklar) / len(uzunluklar)

# Sonuçları ekrana yazdır
print("Toplam yorum sayısı:", len(yorumlar))
print('"iyi" geçen yorum sayısı:', iyi_sayisi)
print("En uzun yorum:", en_uzun)
print("En kısa yorum:", en_kisa)
print("Ortalama uzunluk:", round(ortalama, 1), "karakter")






































