öğrenciListesi = []
dersListesi = []
öğrenciDersNotuListesi = []

# öğrencileri yapalım
def Öğrenciekle(adısoyadı, öğrencino, şifre,  bölüm, devamsızlık, girişyılı, dönem, öğrenciNotları):
    if len([eleman for eleman in öğrenciListesi if eleman["ÖğrenciNo"] == öğrencino]) == 0:
        öğrenciListesi.append({"AdıSoyadı": adısoyadı, "ÖğrenciNo": öğrencino,
                               "Şifre": şifre,"Bölüm": bölüm,
                               "Devamsızlık": devamsızlık, "GirişYılı": girişyılı, "Dönem": dönem,
                               "ÖğrenciNotları": öğrenciNotları})

def DersEkle(id, isim, dersid, mid1etki, mid2etki, finaletki, dönem):
    if len([ders for ders in dersListesi if ders["Dersİd"] == dersid]) == 0:
        id = len(dersListesi) + 1
        dersListesi.append({"İd": id, "İsim": isim, "Mid1etki": mid1etki,
                            "Mid2etki": mid2etki, "Finaletki": finaletki,
                            "Dersİd": dersid, "Dönem": dönem})

def DersEkleDüzenle(öğrencino, dersid, vize1=None, vize2=None, final=None):
    öğrenciNotuDict = {"Öğrencino": öğrencino, "Dersİd": dersid}
    
    if vize1 is not None:
        öğrenciNotuDict["vize1"] = vize1
    if vize2 is not None:
        öğrenciNotuDict["vize2"] = vize2
    if final is not None:
        öğrenciNotuDict["final"] = final

    öğrenciNotuDict["Ortalama"] = OrtalamayıHesapla(öğrenciNotuDict)
    öğrenciDersNotuListesi.append(öğrenciNotuDict)

def OrtalamayıHesapla(öğrenciNotuDictParametre):
    ortalama = 0
    ders = [ders for ders in dersListesi if ders["Dersİd"] == öğrenciNotuDictParametre["Dersİd"]][0]
    if ders is not None:
        if "vize1" in öğrenciNotuDictParametre:
            ortalama += ders["Mid1etki"] * öğrenciNotuDictParametre["vize1"] / 100
        if "vize2" in öğrenciNotuDictParametre:
            ortalama += ders["Mid2etki"] * öğrenciNotuDictParametre["vize2"] / 100
        if "final" in öğrenciNotuDictParametre:
            ortalama += ders["Finaletki"] * öğrenciNotuDictParametre["final"] / 100
    return ortalama

# Öğrenci, ders ve not ekleme işlemleri
Öğrenciekle("MERT AZKO", "123456", "mert123", "Bilgisayar Mühendisliği", 5, 2020, 1, [])
Öğrenciekle("Ayşe Demir", "789012", "ayse456", "Elektrik Mühendisliği", 2, 2021, 2, [])
Öğrenciekle("Mehmet Yılmaz", "135792", "mehmet789", "Endüstri Mühendisliği", 3, 2022, 1, [])
Öğrenciekle("Zeynep Kaya", "246813", "zeynep246", "Kimya Mühendisliği", 0, 2022, 2, [])

DersEkle(1, "Matematik", "MAT101", 30, 30, 40, 1)
DersEkle(2, "Programlama", "PRG202", 20, 30, 50, 2)

DersEkleDüzenle("123456", "MAT101", vize1=80, vize2=85, final=90)
DersEkleDüzenle("123456", "PRG202", vize1=75, vize2=90, final=85)
DersEkleDüzenle("789012", "MAT101", vize1=70, vize2=75, final=80)
DersEkleDüzenle("789012", "PRG202", vize1=85, vize2=80, final=90)
DersEkleDüzenle("135792", "MAT101", vize1=90, vize2=95, final=85)
DersEkleDüzenle("135792", "PRG202", vize1=80, vize2=75, final=70)
DersEkleDüzenle("246813", "MAT101", vize1=60, vize2=70, final=75)
DersEkleDüzenle("246813", "PRG202", vize1=70, vize2=80, final=85)




#şimdi kullancıı için giriş sistemi
def KullanıcıSelamlama(adısoyadı):
    print(f'Hoşgeldin{adısoyadı}')

def NotlarıGörüntüle(öğrenciNo):
    öğrenciNotları = [notlar for notlar in öğrenciDersNotuListesi if notlar["Öğrencino"] == öğrenciNo]
    
    if not öğrenciNotları:
        print("Henüz notunuz bulunmuyor.")
    else:
        for notlar in öğrenciNotları:
            ders = [ders for ders in dersListesi if ders["Dersİd"] == notlar["Dersİd"]][0]
            ders_adi = ders["İsim"]
            vize1 = notlar.get("vize1", 0)
            vize2 = notlar.get("vize2", 0)
            final = notlar.get("final", 0)
            ortalama = notlar["Ortalama"]
            
            print(f"Ders Adı: {ders_adi}")
            print(f"Vize 1: {vize1}")
            print(f"Vize 2: {vize2}")
            print(f"Final: {final}")
            print(f"Ortalama: {ortalama}")
            print("\n")   

def öğrenciDersGörüntüle(öğrenciNo):
    dersİsimleri = []
    dersKodları = [öğrenciDersNotu["Dersİd"] for öğrenciDersNotu in öğrenciDersNotuListesi if öğrenciDersNotu["Öğrencino"] == öğrenciNo]
    for dersKodu in dersKodları:
        dersİsmi = [ders for ders in dersListesi if ders["Dersİd"] == dersKodu][0]["İsim"]
        dersİsimleri.append(dersİsmi + " (" + dersKodu + ")")
    return dersİsimleri
def Kullanıcıİşlemleri():
    seçim=input("Yapmak istediğiniz işlemi seçiniz \n * Dersleri görmek için 1\n * Notları görmek için 2\n")
    if seçim=="1":
        print(öğrenciDersGörüntüle(öğrenciNo))
    elif seçim=="2":
        NotlarıGörüntüle(öğrenciNo)

hak=3
öğrenciNo=None
şifre=None
girişyapanöğrenci=None
#Giriş yapan öğrenci
while hak>0:
    öğrenciNo=input("Ögrenci No: ")
    şifre=input("Şifre Giriniz: ")
    girişyapanöğrenciSorgu=[öğrenci for öğrenci in öğrenciListesi if öğrenci["ÖğrenciNo"]==öğrenciNo and öğrenci["Şifre"]==şifre]
    if len(girişyapanöğrenciSorgu)>0:#0 dan büyük demek girilren veri var anlamına gelir sorgulama yöntemidir 0
        girişyapanöğrenci=girişyapanöğrenciSorgu[0]#giriş yapan bu sorgunun ilk elmanına eşit olur demek zaten sorgu doğru olduğu için


    if girişyapanöğrenci is None:
        hak-=1 
        print(f"Yanlış girdiniz kalan hakkınız={hak}")
        
    else:
        KullanıcıSelamlama(girişyapanöğrenci["AdıSoyadı"])
         #indexli bi f printi yapcaksan tek tırnak başla index içi çift tırnak yoksa hata veriyor aq
        Kullanıcıİşlemleri()

        break         
    if hak<=0:
        print("Çok fazla yanlış denedin gevşek sistem kapandı bb")
        exit()
#şifreyi filan string girmeyince sorun yarattı kabul etemdi ilginç




