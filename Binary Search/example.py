def binary_search(dizi, hedef):
    # Arama yapılacak aralığın sınırlarını belirliyoruz
    sol = 0
    sağ = len(dizi) - 1

    # sol sağdan küçük veya eşit olduğu sürece aramaya devam
    while sol <= sağ:
        orta = (sol + sağ) // 2   # ortadaki indeksi bul
        print(orta,"indexi üzerinden geçildi.")
        if dizi[orta] == hedef:   # ortadaki eleman aradığımız değerse bulduk
            return True
        elif dizi[orta] > hedef:  # ortadaki değer hedeften büyükse sol tarafa bak
            sağ = orta - 1
        else:                     # ortadaki değer hedeften küçükse sağ tarafa bak
            sol = orta + 1

    return False   # döngü biterse eleman yok

# 1'den 10'a kadar bir liste oluştur
sayilar = list(range(1, 11))

print(sayilar)  # [1,2,3,4,5,6,7,8,9,10]
print(binary_search(sayilar, 7))  # True
print(binary_search(sayilar, 12)) # False
