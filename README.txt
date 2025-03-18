# Kitap Öneri Sistemi - Sıfırdan Kurulum Kılavuzu

## Başlamadan Önce Gerekenler
- İnternet bağlantısı
- En az 5GB boş disk alanı
- Windows 10/11 işletim sistemi

## ADIM 1: Anaconda Kurulumu
1. Web tarayıcınızı açın
2. https://www.anaconda.com/download adresine gidin
3. "Download" butonuna tıklayın (Windows için)
4. İndirilen "Anaconda3-xxxx.xx-Windows-x86_64.exe" dosyasını çalıştırın
5. Kurulum adımları:
   - "Next" butonuna tıklayın
   - "I Agree" seçeneğini seçin
   - "Just Me (recommended)" seçeneğini seçin
   - Kurulum konumu için varsayılanı kabul edin
   - ÖNEMLİ: "Add Anaconda3 to my PATH environment variable" kutucuğunu İŞARETLEYİN
   - "Install" butonuna tıklayın
   - Kurulum bitene kadar bekleyin (5-10 dakika sürebilir)
   - "Finish" butonuna tıklayın

## ADIM 2: Proje Dosyalarını Hazırlama
1. Size verilen "KitapOneri.zip" dosyasını masaüstüne kopyalayın
2. Zip dosyasına sağ tıklayın
3. "Tümünü Çıkar" > "Çıkar" seçeneğini seçin
4. Masaüstünde "KitapOneri" klasörü oluşturulacak

## ADIM 3: Anaconda Ortamı Oluşturma
1. Windows başlat menüsünü açın
2. "Anaconda Prompt" yazın
3. "Anaconda Prompt (Anaconda3)" programını YÖNETİCİ OLARAK çalıştırın
4. Aşağıdaki komutları sırayla yazın:
   ```
   conda create --name kitaponeri python=3.8
   ```
   - "Proceed ([y]/n)?" sorusuna "y" yazıp Enter'a basın
   ```
   conda activate kitaponeri
   ```
   ```
   cd C:\Users\%USERNAME%\Desktop\KitapOneri
   ```

## ADIM 4: Gerekli Kütüphaneleri Yükleme (Alternatif Yöntem)
1. Anaconda Prompt'ta şu komutları sırayla yazın:
   ```
   conda update -n base -c defaults conda
   conda install -c conda-forge transformers
   conda install -c pytorch pytorch
   conda install -c conda-forge scikit-learn
   conda install numpy
   conda install -c conda-forge pyqt
   ```
   - Her komut için "Proceed ([y]/n)?" sorusuna "y" yazıp Enter'a basın
   - Bu işlem 15-20 dakika sürebilir

## ADIM 5: Veritabanını Oluşturma
1. Anaconda Prompt'ta yazın:
   ```
   python scrape_books.py
   ```

## ADIM 6: Programı Çalıştırma
1. Anaconda Prompt'ta yazın:
   ```
   python gui.py
   ```

## Olası Hatalar ve Çözümleri

### "conda is not recognized" Hatası
1. Anaconda'yı kaldırın
2. Yeniden kurun ve PATH'e ekleme seçeneğini işaretlediğinizden emin olun
3. Bilgisayarı yeniden başlatın

### "pip is not recognized" Hatası
```
conda install pip
```

### Kütüphane Yükleme Hataları
```
conda install -c conda-forge transformers
conda install -c pytorch pytorch
conda install -c conda-forge scikit-learn
conda install numpy
conda install -c conda-forge pyqt
```

### Program Açılmazsa
1. Tüm Anaconda Prompt'ları kapatın
2. Yeni Anaconda Prompt'u yönetici olarak açın
3. Şu komutları sırayla yazın:
   ```
   conda activate kitaponeri
   cd C:\Users\%USERNAME%\Desktop\KitapOneri
   python gui.py
   ```

## Önemli Notlar
- İlk çalıştırmada yapay zeka modelleri indirilecektir (10-15 dakika sürebilir)
- Windows Defender uyarı verebilir, "İzin Ver" seçeneğini seçin
- Program ilk açılışta yavaş olabilir, sonraki açılışlar daha hızlı olacaktır
- Tüm kurulum yaklaşık 30-45 dakika sürebilir
- Sorun yaşarsanız tüm adımları en baştan tekrarlayın

## Sistem Gereksinimleri
- Windows 10 veya 11
- En az 4GB RAM
- En az 5GB boş disk alanı
- İnternet bağlantısı 