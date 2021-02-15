liste = ["ADI","SOYADI"]
liste2 = ["'dilsah'","'gursoy'"]
sonuc = []
for sutun,deger in zip(liste,liste2):
    sonuc.append(f"{sutun}={deger}")
print(",".join(sonuc))


fonk = lambda x: f"{x[0]}={x[1]}"
",".join(list(map(fonk,list(zip(liste,liste2)))))