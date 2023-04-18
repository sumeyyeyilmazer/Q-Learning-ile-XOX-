Reinforcement Learning - Q Learning - XOX
Makine öğrenmesi tekniklerinden olan Reinforcement Learning (Pekiştirmeli Öğrenme), bir ajanın kendi eylem ve deneyimlerinden aldığı geri bildirimler ile maksimum ödüle ulaşarak öğrenme işlemini gerçekleştirmektedir. Pekiştirmeli Öğrenme modellerinden olan Q algoritması ile Python ile basit bir uygulama yazılmıştır ve Q learning algoritması kullanılarak ajanın eğitilmesi sağlanmıştır.
Anahtar Kelimeler; Pekiştirmeli Öğrenme, Q Learning
Q öğrenmesi, ortamdaki olası her durum (satır) ve eylem (sütun) için bir değer tablosudur. Belirli bir durumda belirli bir eylemi gerçekleştirmenin ne kadar iyi olduğuna dair bir değer öğreniriz. Tabloyu, tekdüze (tümü sıfır) olacak şekilde başlıyoruz ve daha sonra çeşitli eylemler için elde ettiğimiz ödülleri gözlemledikçe, tabloyu buna göre güncelliyoruz.
- Tüm sıfırları içeren tabloyu başlatırız
- Öğrenme parametrelerini ayarlarız
- Bölümlerde toplam ödüller ve adımları içerecek listeler oluşturulur
- Q-tablo öğrenme algoritması
- Q tablosundan bir eylem seçilir
- Yeni duruma geçilir ve eylem ödüllendirilir
- Q tablosu yeni bilgiler ile güncellenir
Bir XOX oyunu geliştirilerek X oyuncusunun Q öğrenme modeli ile eğitilmesi üzerine bir çalışma yapılmıştır. X oyuncusu burada ilk başta rastgele seçimler yapacak ve bu seçimleri için ödül değerleri alacaktır. Oyun sonunda toplam ödül değeri elde edecek ve Q tablosuna aksiyonları kaydolacaktır. Belirlenen epsilon değerine göre artık rastgele seçimler yerine seçimlerini kaydetmiş olduğu Q tablosuna göre belirleyecektir. XOX oyununda eğitilmiş olan X oyuncusu ile rastgele seçimler yapan O oyuncusunun kazanma skorları değerlendirilecektir.
X oyuncusunun Q learning modeli ile eğitilebilmesi icin bir Agent class ı oluşturulmuştur.
game : Ajanı eğittiğimiz XOX oyunudur.
player : Eğitilecek ajan (oyuncu) ‘X’ tir.
brain : Oyundaki farklı durumların Q değerlerini tutmaktadır.
episode : Ajanın kaç oyun ile eğitileceğini belirtir. Bu çalışmada 100000 oyunda eğitim yapılmıştır.
epsilon : Ajanın eğitim boyunca ne sıklıkla rasgele kararlar alacağını belirtir. Bu değeri zamanla düşürürüz ve ajanın kaydedilen Q tablosunu kullanmasını isteriz.
discount_factor : Ajanın yaptığı hamleler ödüllendirilir. Son hamleden ilk hamleye doğru ödül puanı düşürülür. Ödül puanını düşürmek için indirim faktörü kullanılır.
eps_reduce_factor : Her bin oyunda bir epsilon değeri düşürülür ve 90.000 oyun oynanır. Kalan son 10.000 oyunda ajan sadece Q tablosundaki verilerini kullanır.
Ajanın ilk başta yapmış olduğu rastgele hareketler ile eğitim gerçekleştirilir. Her bir oyun hareket Q tablosuna kayıt edilir. Epsilon değeri düştükçe artık ajan rastgele hareketler yerine Q tablosunu kullanmaya başlayacaktır. Tablosuna kayıt ettiği verilerden en yüksek değerli olanı seçecektir. 100.000 bin oyun için son 10.000 oyunda sadece Q tablosunu kullanacağından daha önce bahsetmiştik. Q tablosunun kullanımı için use_brain fonksiyonu oluşturulmuştur.
Ajanın eğitimi tamamlandıktan sonra X ve O oyuncusunun kaç oyun kazandıkları ve kaç oyun beraber kaldıkları ekrana basılır.
