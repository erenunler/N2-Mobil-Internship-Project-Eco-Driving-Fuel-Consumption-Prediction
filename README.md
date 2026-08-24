# N2 Mobil: Eco-Driving & Fuel Consumption Prediction

Bu proje, N2 Mobil Araç Takip Sistemleri 4 Haftalık Makine Öğrenmesi Staj Programı kapsamında geliştirilmiş bir yakıt tüketimi tahmin modelidir. Araçlardaki telemetri cihazlarından alınan sürüş profili verilerini kullanarak, filo yöneticilerine araçların anlık yakıt harcamasını optimize etme ve sürücü alışkanlıklarını analiz etme imkanı sunmayı hedefler.

## Projenin Amacı
Sürüş davranışlarından yakıt tüketimini tahmin eden bir regresyon modeli geliştirmek ve sürecin sonunda bu modeli bir API servisi olarak ürünleştirmektir.

## Geliştirici
Ahmet Eren Ünler - Bilişim Sistemleri Mühendislik Stajyeri

## Kullanılan Teknolojiler
* Python, Pandas, NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

## Kurulum
Projeyi lokalinizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu klonlayın:
`git clone https://github.com/erenunler/N2-Mobil-Internship-Project-Eco-Driving-Fuel-Consumption-Prediction.git`

2. Gerekli kütüphaneleri kurun:
`pip install -r requirements.txt`

## Proje Yapısı
* `data/`: Telemetri sensörlerinden elde edilen ham veri setlerinin bulunduğu klasör.
* `notebooks/`: EDA ve model geliştirme aşamalarının yer aldığı Jupyter notebook dosyaları.
