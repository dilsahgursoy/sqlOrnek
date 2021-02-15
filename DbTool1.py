import sqlite3 as sql

class DBTool():
    
    def __init__(self,adres,tabloadi,**kwargs):
        self.adres = adres
        self.db = sql.connect(self.adres)
        self.cur  = self.db.cursor()
        self.tabloadi = tabloadi
        self.alanlar = ""
        self.sart = ""
        for key,value in kwargs.items():
            if key == "alanlar":
                self.alanlar = ",".join(value)
            if key == "sart":
                self.sart = f" WHERE  {value}"


    def select(self,**kwargs):
        try:
            alanlar = self.alanlar if self.alanlar else "*"
            sart = self.sart if self.sart else ""
            for key,value in kwargs.items():
                if key == "alanlar":
                    alanlar = ",".join(value)
                if key == "sart":
                    sart = f" WHERE  {value}"
            sorgu = f"""
            SELECT {alanlar} FROM
            {self.tabloadi} {sart}"""
            print(sorgu)
            self.cur.execute(sorgu)
            liste = self.cur.fetchall()
        except Exception as hata:
            liste = ["Hata Mesajı",hata]
        finally:
            return liste


    def insert(self,**kwargs):
        try:
            alanlar = self.alanlar if self.alanlar else "*"
            for key,value in kwargs.items():
                if key == "alanlar":
                    alanlar = ",".join(value)
                if key == "degerler":
                    degerler = ",".join(value)
            sorgu = f"""
                INSERT INTO {self.tabloadi} 
                ({alanlar}) VALUES
                ({degerler})
            """
            print(sorgu)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc =  str(self.cur.lastrowid)
        except sql.Error as hata:
            self.db.rollback()
            sonuc = hata
        finally:
            return sonuc


    def update(self,**kwargs):
        try:
            alanlar = self.alanlar.split(",") if self.alanlar else "*"
            for key,value in kwargs.items():
                if key == "alanlar":
                    alanlar = value
                if key == "degerler":
                    degerler = value
                if key == "sart":
                    sart = f" WHERE {value}"
            fonk = lambda x: f"{x[0]}={x[1]}"
            guncelleme =  ",".join(list(map(fonk,list(zip(alanlar,degerler)))))
            sorgu = f"""
            UPDATE {self.tabloadi} SET
            {guncelleme} {sart}
            """
            print(sorgu)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = 1
        except Exception:
            self.db.rollback()
            sonuc = -1
        finally:
            return sonuc

    
    def delete(self,**kwargs):
        try:
            for key,value in kwargs.items():
                if key == "sart":
                    sart = f" WHERE {value}"
            sorgu = f"""
            DELETE FROM {self.tabloadi} {sart}
            """
            print(sorgu)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = 1
        except Exception:
            self.db.rollback()
            sonuc = -1
        finally:
            return sonuc