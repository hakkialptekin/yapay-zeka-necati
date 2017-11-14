# yapay-zeka-necati
##yapay gerizeka mk.1 NECATİ
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

##nasılsın
a=input()
import random  
cevap=["iyilik işte","kötüyüm","eh işte","nörek","yuvarlanıp gidiyoz işte"]
if(a=="nasılsın" or a=="nasıl gidiyor" or a=="nörüyon"):
    ran = random.randint(0,4)
    print(cevap[ran])
    
##espri
e1="sınaav kolaya benziyodu ama aslında fantaydı"
e2="geçen gün taksi çevirdim hala dönüyo"
e3="geçen gün ödeme noktasına gittim ö dedim geldim"
e4="Adamın biri güneşte yanmış, ayda düz."
e5="kelebekler,köstebekler ama ben beklemem."
espriler=[e1,e2,e3,e4,e5]
e=input()
import random
if(e=="espri yap"):
    ran2 = random.randint(0,4)
    print(espriler[ran2])

