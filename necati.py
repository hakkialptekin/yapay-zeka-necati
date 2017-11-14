##yapay gerizeka Mk.2 NECATİ
##karşılama
ad=input("Oooooo kimleri görüyoruz?   ")
if (ad=="azem" or ad=="ela" or ad=="mina" or ad=="begüm" or ad=="ayça" or ad=="zerrin" or ad=="zeynep sude"
    or ad=="duygu" or ad=="doğa" or ad=="aslı" or ad=="asya" or
    ad=="dila" or ad=="irem" or ad=="zeynep" or ad=="betül" or ad=="lara"):
    print("Hoşgeldin abla")
if (ad=="asil" or ad=="onur" or ad=="bahadır" or ad=="semih" or ad=="osman" or
    ad=="ayberk" or ad=="ahmet" or ad=="kerem" or ad=="yiğit" or ad=="alp"):
    print("Hoşgeldin birader")
if (ad=="deniz" or ad=="kerem zaman"):
    print("Hoşgeldin büyük üstat")
if (ad=="miray"):
    print("Merhaba bayan")
if (ad=="kurtuluş" or ad=="hürol"):
    print("Merhaba hocam")
if not(ad=="azem" or ad=="ela" or ad=="mina" or ad=="begüm" or ad=="ayça" or ad=="zerrin" or ad=="zeynep sude"
    or ad=="duygu" or ad=="doğa" or ad=="aslı" or ad=="asya" or
    ad=="dila" or ad=="irem" or ad=="zeynep" or ad=="betül" or ad=="lara"
    or ad=="asil" or ad=="onur" or ad=="bahadır" or ad=="semih" or ad=="osman" or
    ad=="ayberk" or ad=="ahmet" or ad=="kerem" or ad=="yiğit" or ad=="alp"
       or ad=="deniz" or ad=="kerem zaman"
       or ad=="miray" or  ad=="kurtuluş" or ad=="hürol"):
        print("Sen kimsin lo?")
##sorular
x=input()
if(x=="nasılsın" or x=="nörüyon" or x=="nası gidiyo"):
    import random  
    cevap=["iyilik işte","kötüyüm","eh işte","nörek","yuvarlanıp gidiyoz işte"]
    ran = random.randint(0,4)
    print(cevap[ran])
    
    
e1="sınaav kolaya benziyodu ama aslında fantaydı"
e2="geçen gün taksi çevirdim hala dönüyo"
e3="geçen gün ödeme noktasına gittim ö dedim geldim"
e4="Adamın biri güneşte yanmış, ayda düz."
e5="kelebekler,köstebekler ama ben beklemem."
espriler=[e1,e2,e3,e4,e5]
import random
if(x=="espri yap"):
    ran2 = random.randint(0,4)
    print(espriler[ran2])

##görüşürüz
if(x=="görüşürüz" and ad=="azem" or ad=="ela" or ad=="mina" or ad=="begüm" or ad=="ayça" or ad=="zerrin" or ad=="zeynep sude"
    or ad=="duygu" or ad=="doğa" or ad=="aslı" or ad=="asya" or
    ad=="dila" or ad=="irem" or ad=="zeynep" or ad=="betül" or ad=="lara"):
    print("görüşürüz abla")
if(x=="görüşürüz" and ad=="asil" or ad=="onur" or ad=="bahadır" or ad=="semih" or ad=="osman" or
    ad=="ayberk" or ad=="ahmet" or ad=="kerem" or ad=="yiğit" or ad=="alp"):
    print("görüşürüz birader")
if(x=="görüşürüz" and ad=="deniz" or ad=="kerem zaman"):
    print("görüşürüz üstat")
if (ad=="miray"):
    print("görüşürüz bayan")
if (ad=="kurtuluş" or ad=="hürol"):
    print("görüşürüz hocam")



