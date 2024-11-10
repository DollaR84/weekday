# Takvim

* Yazar: Ruslan Dolovaniuk (Ukrayna)
* PayPal: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B3VG4L8B7CV3Y&source=url


Tarih ve saat ile çalışmak için ek fonksiyonlar.

## Kısayol tuşlarının listesi:
* Tüm kısayol tuşları NVDA+W ile bağlıdır. Seçilen moda göre farklı fonksiyonlar vardır;
* NVDA+ALT+W: çalışma modlarını değiştirir;
* NVDA+SHIFT+W: geri sayım ve alarm modlarında zaman ölçümleri (saat, dakika, saniye) arasında geçiş yapar;
* NVDA+SHIFT+W: geçici sinyal modunda, sinyal ayarını değiştirir: ses, konuşma, ses ve konuşma birlikte veya hiçbiri;
* NVDA+SHIFT+W: Takvim modunda, tarihi olaylar ayarını değiştirir: tarihi olay, Wikipedia'dan olay, Wikipedia'dan olay ve tarihi olay birlikte veya hiçbiri;
* NVDA+SHIFT+W: Takvim, kronometre ve zaman sinyali modlarında, tüm modların ayarlarını kaydeder;

### Takvim Modu
* NVDA+W: günün adını söyler;
* NVDA+W: Çift tıklama bu günün tatilini, varsa, ayrıca bu günle ilgili tarihi bir olayı ve/veya Wikipedia'dan bir olayı söyler;
* NVDA+SHIFT+ALT+W: hızlı başlatma için seçilen programı başlatır;
* NVDA+SHIFT+ALT+W: çift tıklama hızlı başlatma için bir program seçmenizi sağlar;

### Kronometre Modu
* NVDA+W: tek tıklama kronometreyi başlatır, eğer çalışmıyorsa;
* NVDA+W: Çift tıklama, kronometreyi başlatır, eğer çalışmıyorsa veya çalışıyorsa duraklatır. Ayrıca durdurulmuşsa çalışmasını yeniden başlatır;
* NVDA+W: Üçlü tıklama çalışan kronometreyi durdurur;

### Geri Sayım Modu
Başlangıç seçimi mod ayarını açar. Aşağıdaki kombinasyonları içerir:
* NVDA+SHIFT+W: Ayar birimlerini (saat, dakika, saniye) değiştirir;
* NVDA+W: Tek tıklama zaman seçimini kurulum için değiştirir, saat için 1 saatlik adımlarla, dakika ve saniye için 5 birimlik adımlarla;
* NVDA+W: çift tıklama seçilen aralığı ayarlar;
* NVDA+W: üçlü tıklama geri sayımı başlatır;

Çalışırken, aşağıdaki kombinasyonlar:
* NVDA+W: tek tıklama belirlenen süreye ne kadar zaman kaldığını söyler;
* NVDA+W: çift tıklama geri sayımı duraklatır, eğer çalışıyorsa veya duraklatılmışsa yeniden başlatır;
* NVDA+W: üçlü tıklama geri sayımı durdurur;

### Alarm Modu
Başlangıç seçimi mod ayarını açar. Aşağıdaki kombinasyonları içerir:
* NVDA+SHIFT+W: Ayar birimlerini (saat, dakika, saniye) değiştirir;
* NVDA+W: Tek tıklama zaman seçimini kurulum için değiştirir, saat için 1 saatlik adımlarla, dakika ve saniye için 5 birimlik adımlarla;
* NVDA+W: çift tıklama seçilen zamanı ayarlar;
* NVDA+W: üçlü tıklama alarmı başlatır;

Çalışırken, aşağıdaki kombinasyonlar:
* NVDA+W: tek tıklama belirlenen zamana ne kadar süre kaldığını söyler;
* NVDA+W: üçlü tıklama alarmı durdurur;

### Zaman Sinyali Modu
* NVDA+W: sinyal periyodunu (60, 30, 15, 0) dakika olarak değiştirir. Varsayılan 0 - sinyal devre dışı;

## Değişikliklerin listesi:
### Versiyon 1.1.0
* Türkçe yerelleştirme eklendi (Umut KORKMAZ);

### Versiyon 1.0.7
* saat sinyalinin doğruluğu düzeltildi;

### Versiyon 1.0.6
* gece yarısında zamanın telaffuzu sorunu düzeltildi;

### Versiyon 1.0.0
* hızlı başlatma programının seçimi ve başlatılması eklendi;
* Takvim için tarihi olay kaynağı seçimi eklendi;
* geçici sinyal için sinyal türü seçimi eklendi (ses, konuşma, ses ve konuşma birlikte, hiçbir şey);
* Takvim, zaman sinyali ve zamanlayıcı modlarında otomatik kaydetme eklendi;
* kaydedilen ayarların yüklenmesi sırasında bir hata düzeltildi;

### Versiyon 0.5.8
* NVDA+W'ye çift tıklayarak alarm hatırlatıcısı her 30 saniyede bir eklendi;
* geri sayım, alarm saati açıldığında/kapatıldığında ayarların otomatik olarak kaydedilmesi eklendi;
* yeniden başlatma sonrasında kaydedilen verilerden geri sayımın geri yüklenmesi eklendi;
* farklı modlarda zaman sinyali ayarlanırken oluşan hata düzeltildi;

### Versiyon 0.5.6
* mevcut günde tatilin telaffuzu eklendi, eğer varsa;
* mevcut günün tarihi olayının telaffuzu eklendi;

### Versiyon 0.5.2
* ayarların kaydedilmesi eklendi;

### Versiyon 0.5.0
* alarm modu eklendi;

### Versiyon 0.4.5
* Zaman Sinyali modu eklendi;

### Versiyon 0.4.0
* bileşen mimarisi yeniden tasarlandı;
* geri sayım zamanlayıcısı eklendi;
* kontrol sistemi değiştirildi ve modlar tanıtıldı;

### Versiyon 0.3.0
* Kronometre eklendi;
