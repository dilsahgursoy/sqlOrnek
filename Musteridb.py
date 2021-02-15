from DbTool1 import DBTool

class Musteri():
    def __init__(self):
        self.db = DBTool(adres="SQL\chinook.db",tabloadi="customers",alanlar=["Firstname","LastName","email"])
    
    def musteriListele(self):
        return self.db.select(sart="Firstname='Ahmet'")

    def musteriEkle(self):
        return self.db.insert(degerler=["'Zeynep'","'Aslan'","'zeynep@gmail.com'"])
        #return self.db.insert()

    def musteriGuncelle(self,cid):
        return self.db.update(degerler=["'Hüseyin'","'Kaplan'","'huseyin@gmail.com'"],sart=f" CustomerId = {cid}")

    def musteriSil(self,sart=""):
        return self.db.delete(sart=sart)


if __name__ == "__main__":
    musteri1 = Musteri()
    liste = musteri1.musteriListele()
    print(liste)
    sonuc = musteri1.musteriEkle()
    print(sonuc)
