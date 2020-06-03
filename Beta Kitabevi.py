import time
import os

os.system("color f0")

# KÜTÜPHANEDEKİ TÜM KİTAPLARIN ÖZELLİKLERİ
kitaplar = {
   "Başkaldıran İnsan": ["Albert Camus", "Felsefe", "konum1"],
   "Mülksüzler": ["Ursula Leguin", "Roman", "konum2"],
   "Ulysses": ["James Joyce", "Destan", "konum3" ],
   "Romanov Komplosu": ["Glenn Made","Roman", "konum4"],
   "Leviathan": ["Paul Auster", "Roman", "konum5"],
   "Brookly Çılgınlıkları": ["Paul Auster", "Roman", "konum6"],
   "New York Üçlemesi": ["Paul Auster", "Roman", "konum7"],
   "Ana" : ["Maksim Gorki", "Roman", "konum8"],
   "Küçük Şeylerin Tanrısı": ["Arundhati Roy", "Roman", "konum9"],
   "Milena'ya Mektuplar": ["Franz Kafka", "Roman", "konum10"],
   "Faust" : ["Goethe", "Roman", "konum11"],
   "İlahi Komedya": ["Dante", "Destan", "konum12"],
   "Korkma Ben Varım": ["Murat Menteş", "Roman", "konum13"],
   "Genç Werther'in Acıları":["Goethe", "Roman", "konum14"],
   "Zen ve Motosiklet Bakım Sanatı": ["Robert Pirsig", "Roman", "konum15"],
   "Kabil": ["Jose Saramago", "Öykü", "konum16"],
   "Notre Dame'in Kamburu": ["Victor Hugo", "Roman", "konum17"],
   "To The Lighthouse": ["Virginia Woolf", "İngilizce", "konum18"],
   "Tanrı Olmak İsteyen Otobüs Şoförü": ["Etgar Keret", "Roman", "konum19"],
   "Aşk ve Öbür Cinler": ["Gabriel Garcia Marquez", "Roman", "konum20"],
   "İnsan Ne İle Yaşar": ["Lev Tolstoy", "Öykü", "konum21"],
   "Satranç": ["Stefan Zweig", "Roman", "konum22"],
   "Olağanüstü Bir Gece": ["Stefan Zweig", "Roman", "konum23"],
   "Bir Delinin Hatıra Defteri": ["Gogol","Öykü", "konum24"],
   "Yüzbaşının Kızı":["Puşkin", "Roman", "konum25"],
   "İnci": ["John Steinbeck", "Öykü", "konum26"],
   "Fareler Ve İnsanlar": ["John Steinbeck", "Öykü", "konum27"],
   "1984":["George Orwell", "Roman", "konum28"],
   "Dövüş Kulübü": ["Chuck Palahniuk", "Roman", "konum29"],
   "Görünmez Canavarlar": ["Chuck Palahniuk", "Roman", "konum30"],
   "Gösteri Peygamberi": ["Chuck Palahniuk", "Roman", "konum31"],
   "Tıkanma": ["Chuck Palahniuk", "Roman", "konum32"],
   "Yanık Diller": ["Chuck Palahniuk", "Öykü", "konum33"],
   "Nietzsche Ağladığında": ["Irvin Yalom", "Roman", "konum34"],
   "Beyaz Zenciler": ["Ingvar Ambjörnsen", "Roman", "konum35"],
   "Mutsuzluk Zamanlarında Mutluluk": ["Wilhelm Genazino", "Roman", "konum36"],
   "Karanlıkların Efendisi": ["Ernesto Sabato", "Roman", "konum37"],
   "Yengeç Dönencesi": ["Henry Miller", "Roman", "konum38"],
   "Simyacı": ["Paulo Coelho", "Roman", "konum39"],
   "Ölü Canlar ": ["Gogol", "Roman", "konum40"],
   "Kızıl Ölümün Maskesi": ["Edgar Allan Poe", "Öykü", "konum41"],
   "Ömrüm Bir Karadutun Kar Görme Heyecanıyla Geçti": ["Mert Tutucu", "Şiir", "konum42"],
   "Ivan Ilyiç'in Ölümü": ["Lev Tolstoy", "Öykü", "konum43"],
   "Prens": ["Niccolo Machiavelli", "Tarih", "konum44"],
   "İnsancıklar": ["Dostoyevski", " Roman", "konum45"],
   "Madame Bovary": ["Gustave Flaubert", "Roman", "konum46"],
   "Gurur ve Önyargı" : ["Jane Austen", "Roman", "konum47"],
   "İnsanca Pek İnsanca": ["Friedrich Nietzsche", "Felsefe", "konum48"],
   "Sanatçının Bir Genç Adam Olarak Portresi": ["James Joyce", "Roman", "konum49"],
   "Kumarbaz": ["Dostoyevski", "Roman", "konum50"],
   "Suç ve Ceza": ["Dostoyevski", "Roman", "konum51"],
   "Hamlet": ["William Shakespeare", "Destan", "konum52"],
   "Yeraltından Notlar": ["Dostoyevski", "Roman", "konum53"],
   "Karamazov Kardeşler": ["Dostoyevski", "Roman", "konum54"],
   "Kurtlarla Koşan Kadınlar": ["Clarissa Estes", "Roman", "konum55"],
   "Yeşil Tatil": ["Naitonal Geographic", "Gezi", "konum56"],
   "Sarı Tatil": ["National Geographic", "Gezi", "konum57"],
   "Türkiye Milli Parklar Haritası": ["Atlas", "Gezi", "konum58"],
   "Nereye Ne Zaman Gidilir?": ["Atlas", "Gezi", "konum59"],
   "Paris": ["Berlitz", "Gezi", "konum60"],
   "Hastasıyım Bu Oyunun": ["Kaan Kural", "Deneme", "konum61" ],
   "Kutsal Çemberler": ["Phil Jackson", "Roman", " konum62"],
   "Varış Çizgisi": ["Paola Zannoner", "Roman", "konum63"],
   "Romantik Hareket": ["Alain De Botton", "Roman", "konum64"],
   "Seyahat Sanatı": ["Alain De Botton", "Gezi", "konum65"],
   "Dosta Doğru": ["Abdürrahim Karakoç", "Öykü", "konum66"],
   "Beşinci Mevsim": ["Abdürrahim Karakoç", "Öykü", "konum67"],
   "Kayıp Kentin Yakışıklısı": ["Yılmaz Erdoğan", "Öykü", "konum68"],
   "Yalnızlık Paylaşılmaz": ["Özdemir Asaf", "Şiir", "konum69"],
   "Benden Sonra Mutluluk": ["Özdemir Asaf", "Şiir", "konum70"],
   "Şiirler": ["Güzel Yazılar", "Şiir", "konum71"],
   "Yunus Emre": ["Memet Fuat", "Biyografi", "konum72"],
   "Hayyam" : ["A. Kadir", "Biyografi", "konum73"],
   "Böyle Buyurdu Zerdüşt": ["Friedrich Nietzsche", "Felsefe", "konum74"],
   "Son Kuşlar": ["Sait Faik Abasıyanık", "Öykü", "konum75"],
   "Puslu Kıtalar Atlası": ["Hasan Oktay Anar", "Roman", "konum76"],
   "Leyla'nın Evi": ["Zülfü Livaneli", "Roman", "konum77"],
   "Sevda Sözleri": ["Cemal Süreya", "Şiir", "konum78"],
   "Kendine Ait Bir Oda": ["Virginia Woolf", "Roman", "konum79"],
   "Kız Kulesi'ndeki Kızılderili": ["Sunay Akın", "Öykü", "konum80"],
   "İstanbul'da Bir Zürafa": ["Sunay Akın", "Öykü", "konum81"],
   "Şimdiki Çocuklar Harika": ["Aziz Nesin", "Roman", "konum82"],
   "Şamanlar Diyarı": ["Barış Müstecaplıoğlu", "Roman", "konum83"],
   "Üç Anadolu Efsanesi": ["Yaşar Kemal", "Destan", "konum84"],
   "Ayasofya'nın Gizli Tarihi": ["Pelin Çift","Tarih", "konum85"],
   "Çanakkale": ["Talha Uğurel", "Tarih", "konum86"],
   "Venedik ve Veneto": ["Gezi", "Gezi","konum87"],
   "Oz Büyücüsü": ["Frank Baum", "Roman", "konum88"],
   "Eugenie Grandet": ["Balzac", "Roman", "konum89"],
   "Aşkın Metafiziği": ["Arthut Schopenhaur", "Felsefe", "konum90"],
   "Okumak Yazmak ve Yaşamak Üzerine": ["Arthur Schopenhaur", "Felsefe", "konum91"],
   "Sevdadır": ["Arkadaş Özger", "Şiir", "konum92"],
   "Doğu Hikayeleriyle Psikoterapi": ["Nossrat Peseschkian", "Psikoloji", "konum93"],
   "Sodom": ["Sade", "Roman", "konum94"],
   "Gazap Üzümleri": ["John Steinbeck", "Roman", "konum95"],
   "Dünya Tarihi": ["Ernst Gombrich", "Tarih", "konum96"],
   "Türklerin Tarihi": ["İlber Ortaylı", "Tarih", "konum97"],
   "Osmanlıyı Yeniden Keşfetmek": ["İlber Ortaylı", "Tarih", "konum98"],
   "Osmanlı": ["Halil Inalcık", "Tarih", "konum99"],
   "Bir Nefeste Dünya Tarihi": ["Emma Marriott", "Tarih", "konum100"],
   "Tarihimizle Yüzleşmek": ["Emre Kongar", "Tarih", "konum101"],
   "Rönesanslar": ["Jack Goody", "Tarih", "konum102"],
   "Dünyanın Kanlı Tarihi": ["Jacob Field", "Tarih", "konum103"],
   "Dünya Sinemasında Akımlar": ["Esen Coçkun", "Tarih","konum104"],
   "Katip Bartleby": ["Herman Melville", "Öykü", "konum105"],
   "Denemeler": ["Montaigne", "Deneme", "konum106"],
   "Aşk Üzerine": ["Alain De Botton","Deneme", "konum107" ],
   "Silah Kaçakçılığı ve Terör": ["Uğur Mumcu", "Tarih", "konum108"],
   "Sakıcalı Piyade": ["Uğur Mumcu", "Tarih", "konum109"],
   "Kahverengi Veba": ["Daniel Guerin", "Tarih", "konum110"],
   "Geleceğin Savaşları ve Silahları": ["Özgür Mumcu", "Tarih", "konum111"],
   "Bulantı": ["Jean Paul Sartre", "Felsefe", "konum112"],
   "Dönüşüm": ["Franz Kafka", "Öykü", "konum113"],
   "Kırmızı Pazartesi": ["Gabriel Garcia Marquez", "Öykü", "konum114"],
   "Yabancı": ["Albert Camus", "Roman", "konum115"],
   "Bir Bilim Adamının Romanı: Mustafa İnan": ["Oğuz Atay", "Roman", "konum116"],
   "Claude'un İtirafları": ["Emile Zola", "Roman", "konum117"],
   "Albertine Kayıp": ["Marcel Proust", "Roman", "konum118"],
   "Aylak Adam": ["Yusuf Atılgan", "Roman", "konum119"],
   "Çavdar Tarlasında Çocuklar": ["Salinger", "Roman", "konum120"],
   "Kürk Mantolu Madonna": ["Sabahattin Ali", "Öykü", "konum121"],
   "Ölümcül Kemikler": ["Amin Maalouf", "Roman", "konum122"],
   "Sineklerin Tanrısı": ["William Golding", "Roman", "konum123"],
   "Demir Ökçe": ["Jack London", "Roman", "konum124"],
   "Şeker Portakalı": ["Jose Mauro De Vasconcelos", "Roman", "konum125"],
   "Köşeye Kıstırmak": ["Paul Auster", "Roman", "konum126"],
   "Kış Günlüğü": ["Paul Auster", "Roman", "konum127"],
   "Ruhi Mücerret": ["Murat Menteş", "Roman", "konum128"],
   "Dublörün Dilemması": ["Murat Menteş", "Roman", "konum129"],
   "Otomatik Portakal": ["Anthony Burgess", "Roman", "konum130"],
   "Marti Jonathan Livingston": ["Richard Bach", "Öykü", "konum131"],
   "Frankenstein Ya Da Modern Prometheus": ["Mary Shelley", "Roman", "konum132"],
   "Karanlık Güzergahlar": ["John Ralston Saul", "Roman", "konum133"],
   "Yolda": ["Jack Kerouac", "Roman", "konum134"],
   "Ruh Yoluyla Tedavi": ["Stefan Zweig", "Psikoloji", "konum135"],
   "Psikolojiye Giriş": ["Kemal Sayar", "Psikoloji", "konum136"],
   "Sesim Seninle Her Yerde": ["Sidney Rosen", "Roman", "konum137"],
   "Küçük Kaptan'ın Dönüşü": ["Paul Biegel", "Roman", "konum138"],
   "Tom Sawyer'ın Maceraları": ["Mark Twain", "Öykü", "konum139"],
   "Don Kişot": ["Cervantes", "Öykü", "konum140"],
   "Cinayetler Oteli": ["Agatha Christie", "Öykü", "konum141"],
   "Siyah Lale": ["Alexandre Dumas", "Öykü", "konum142"],
   "Monte Kristo Kontu": ["Alexandre Dumaas", "Öykü", "konum143"],
   "Da Vinci ve Saklı Not Defteri": ["Leonardo Da Vinci", "Roman", "konum144"],
   "İki Yıl Okul Tatili": ["Jules Verne", "Roman", "konum145"],
   "Pıtırcık Bilinmeyen Öyküleri 1": ["Goscinny / Sempe", "Öykü", "konum146"],
   "Pıtırcık Bilinmeyen Öyküleri 2": ["Goscinny / Sempe", "Öykü", "konum147"],
   "Seçme Konuşmalar": ["Konfüçyüs", "Felsefe", "konum148"],
   "Evliya Çelebi'nin Seyahatnamesi'nden Seçmeler": ["Evliya Çelebi", "Gezi", "konum149"],
   "Mercan Adası": ["Ballantyne", "Roman", "konum150"],
   "Hitler Oyuncağımı Çaldı": ["Judith Kerr", "Roman", "konum151"],
   "Çocuk Kalbi": ["Edmondo De Amicis","Roman", "konum152"],
   "Psikanalize Yeni Giriş Dersleri": ["Sigmund Freud", "Psikoloji", "konum153"],
   
   
   
   
   
}
yapılabilecekişlemler = ["a-) Aradığım kitap nerede? Yazarı kim? Gibi sorularınıza cevap bulabilir" , "b-) Aradığınız yazarın hangi kitaplarına sahip olduğunuzu öğrenebilir ", "c-) Kitaplığınıza baktığınızda bir kitabın eksik olduğunu düşünüyorsanız; kayıp kitabın rafta bulunduğu konumun numarasını yazarak o kitabın adını öğrenebilir .", "d-) Kitap türü aratarak o türdeki kitaplarınızı görebilir.", "e-) Kitaplığınızdaki toplam kitap sayısını öğrenebilir.", "f-) Kitaplığınızdaki tüm kitapları sıralayabilir ve ayrıntılı bilgilere ulaşabilir." ]
# YAPILABİLECEK İŞLEMLER LİSTESİ
print ("Kitaplığına hosgeldin sevgili okur. Bu program sayesinde kitaplığın hakkında ulaşmak istediğin bilgilere en kısa sürede ulaşabilirsin. :")


while True:
   for each in yapılabilecekişlemler:
      print (each)
       


   işlem = input("Şimdi gerçekleştirmek istediğiniz işlemin başındaki harfi yazıp 'Enter' tuşuna basınız :")
   # PROGRAMIN MEKANİZMASI AŞAĞIDA
   if işlem == 'a':
       x = input("Kitabın adını yazarken lütfen her kelimenin başını büyük harfle ve kurallara uygun yazdığınızdan emin olunuz: ")
       for n in kitaplar:       
          if n == x:
             print ("-".join(kitaplar[n]))

         
   elif işlem == 'b':
      x = input("Kitaplarını bulmak istediğiniz yazarın adını yazarken lütfen her kelimenin baş harfini büyük yazınız: : ")
      for each in kitaplar:
         özelliklerlistesi = kitaplar[each]
         kitabınyazarı = özelliklerlistesi[0]
         if x == kitabınyazarı:
            print (each)
                        
   elif işlem == "c" :
      x = input("Hangi konumda hangi kitap olduğunu öğrenmek için konumu yazınız:  ")
      for each in kitaplar:
         
          özelliklerlistesi = kitaplar[each]
          kitabınkonumu = özelliklerlistesi[2]
          if x == kitabınkonumu:
             print (each)
        
   elif işlem == "d" :
      türlistesi = ["Felsefe", "Roman", "Destan", "Gezi", "Öykü", "Tarih", "Deneme", "Psikoloji", ]
      print ("Aratabileceğiniz türler arasında şunlar vardır: " +  ('-'.join(türlistesi)))
      x = input("Şimdi yazmak istediğiniz türü baş harfi büyük olacak şekilde yazınız: ")
      for each in kitaplar:
          özelliklerlistesi = kitaplar[each]
          kitabıntürü = özelliklerlistesi[1]
          if x == kitabıntürü:
             print (each)
         
            
   elif işlem == "e" :
      def toplam(kitaplar):
         toplamsayı= 0
         for each in kitaplar:
            toplamsayı = toplamsayı + 1
         return toplamsayı
      print ("Kitaplığınızda toplam  " + str(toplam(kitaplar))+ "  kitap vardır.")
      
   elif işlem == "f":
      print ()
      print ()
      for each in kitaplar:
         print ( "Kitabın Adı: "+str(each)+ "   --  Yazarı, Türü ve Konumu:   "+ str("  -  ".join(kitaplar[each])))
         print()

      
       
   print ("####################################################################################")   
         
time.sleep(9999)
   

