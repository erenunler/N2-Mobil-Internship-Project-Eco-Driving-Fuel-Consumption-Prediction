# 1. HAFTA EDA RAPORU

## DATASET VE VERİ KALİTESİ
Proje kapsamında verilen telemetri veri setini inceledim. Toplamda 30.000 satır ve 6 kolondan oluşan temiz bir yapı buldum. Hedef değişkenimi fuel_consumption olarak belirledim. Kalan değişkenleri ise modele ipucu vermesi için girdi sütunları olarak atadım. Yaptığım kontrollerde eksik veri veya tekrar eden satır bulmadım.

## DEĞİŞKEN İLİŞKİLERİ VE GRAFİKLER
Verileri daha iyi anlamak için grafikler çizdirdim. Isı haritası ve saçılım grafikleri ile hedef değişkenimi etkileyen kalıpları belirledim.
* Sert fren sayısı, rölanti süresi ve devir dalgalanması arttıkça yakıt tüketimi artıyor.
* Sürüş pürüzsüzlüğü arttıkça yakıt tüketimi hafif bir düşüş eğilimine giriyor.
Ayrıca yakıt tüketiminin genel dağılımının 7 ile 9 litre arasında yoğunlaştığını gördüm.

## AYKIRI DEĞERLER
Aykırı değerleri bulmak için istatistiksel sınırların dışında kalan kayıtları filtreledim. Özellikle sert fren sayısında ve yakıt tüketiminde gerçek sürüş profiline uymayan anormal kayıtlar tespit ettim. Modeli daha sağlıklı eğitebilmek için bu değerleri veri setinden tamamen temizledim.

## VERİ SIZINTISI VE ECO SCORE
Veri setindeki en büyük risk eco_score sütunuydu. Yaptığım analizlerde bu puanın yakıt tüketimi üzerinden hesaplandığını anladım. Eğitimde kullanmam durumunda model kopya çekecekti ve veri sızıntısı yaşanacaktı. Bu hataya düşmemek için eco_score sütununu veri setinden çıkardım ve model eğitimine hazır hale getirdim.