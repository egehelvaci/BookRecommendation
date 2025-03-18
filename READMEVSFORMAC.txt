# Kitap Öneri Sistemi - MacOS Visual Studio Code Kurulum Kılavuzu

## Gereksinimler
- MacOS işletim sistemi
- İnternet bağlantısı
- En az 5GB boş disk alanı
- Yönetici (admin) şifresi

## ADIM 1: Visual Studio Code Kurulumu
1. VSCode'u indirin:
   - https://code.visualstudio.com/ adresine gidin
   - "Download Mac Universal" butonuna tıklayın
   - İndirilen .dmg dosyasını açın
   - VSCode uygulamasını Applications klasörüne sürükleyin

2. Gerekli Eklentileri Yükleyin:
   - VSCode'u açın
   - Sol taraftaki Extensions sekmesine tıklayın (⌘ + Shift + X)
   - Şu eklentileri arayıp yükleyin:
     * Python (Microsoft)
     * Jupyter
     * Python Extension Pack
     * Python Indent

## ADIM 2: Python Kurulumu
1. Python'u indirin:
   - https://www.python.org/downloads/ adresine gidin
   - Sayfanın altındaki "Looking for a specific release?" linkine tıklayın
   - Python 3.8.10 sürümünü bulun ve macOS 64-bit installer'ı indirin
   - İndirilen .pkg dosyasını çalıştırın
   - Kurulum sihirbazını takip edin
   - "Install certificates.command" dosyasını çalıştırın

2. Terminal'i açın (⌘ + Space, "Terminal" yazın)
3. Python kurulumunu kontrol edin:
   ```
   python3.8 --version
   ```

## ADIM 3: Proje Dosyalarını Hazırlama
1. Masaüstünde proje klasörü oluşturun:
   ```
   cd ~/Desktop
   mkdir KitapOneri
   ```

2. ZIP dosyasını çıkartın:
   - KitapOneri.zip dosyasını Masaüstüne kopyalayın
   ```
   cd ~/Desktop
   unzip KitapOneri.zip -d KitapOneri
   ```

3. VSCode ile projeyi açın:
   - VSCode'u açın
   - File > Open Folder
   - Desktop > KitapOneri klasörünü seçin

## ADIM 4: Sanal Ortam Oluşturma
1. VSCode'da terminal açın (⌘ + `)
2. Sanal ortam oluşturun:
   ```
   python3.8 -m venv venv
   source venv/bin/activate
   ```

## ADIM 5: Kütüphaneleri Yükleme
1. pip'i güncelleyin:
   ```
   pip install --upgrade pip
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```
   # Python 3.8 uyumlu kararlı sürümler
   pip install numpy==1.23.5
   pip install transformers==4.21.0
   pip install torch==1.13.1
   pip install scikit-learn==1.4.0
   pip install PyQt5==5.15.10
   ```

### Python 3.8 Uyumluluk Notları
1. Bazı kütüphaneler Python 3.8 ile tam uyumlu olmayabilir
2. Eğer hala hata alırsanız:
   ```
   # Sanal ortamı deaktive edip silin
   deactivate
   rm -rf venv
   
   # Yeni sanal ortam oluşturun
   python3.8 -m venv venv
   source venv/bin/activate
   
   # Kütüphaneleri sırayla yükleyin
   pip install numpy==1.23.5
   pip install transformers==4.21.0
   pip install torch==1.13.1
   pip install scikit-learn==1.4.0
   pip install PyQt5==5.15.10
   ```

3. Alternatif çözüm:
   ```
   # Tüm kütüphaneleri tek komutla yükleyin
   pip install numpy==1.23.5 transformers==4.21.0 torch==1.13.1 scikit-learn==1.4.0 PyQt5==5.15.10
   ```

4. Eğer yukarıdaki sürümlerle hata alırsanız:
   ```
   pip install --upgrade numpy
   pip install --upgrade transformers torch scikit-learn PyQt5
   ```

## ADIM 6: Python Yorumlayıcısını Seçme
1. Command Palette'i açın (⌘ + Shift + P)
2. "Python: Select Interpreter" yazın
3. "./venv/bin/python" seçeneğini seçin

## ADIM 7: Projeyi Çalıştırma
1. gui.py dosyasını açın
2. Sağ üstteki ▶️ butonuna tıklayın
   veya terminal'de:
   ```
   python gui.py
   ```

## Olası Hatalar ve Çözümleri

### GUI Hatası
1. XQuartz'ı yükleyin:
   ```
   brew install --cask xquartz
   ```
2. Bilgisayarı yeniden başlatın

### Kütüphane Hataları
1. Sanal ortamı kontrol edin:
   ```
   source venv/bin/activate
   ```
2. Kütüphaneleri yeniden yükleyin:
   ```
   pip install -r requirements.txt
   ```

### VSCode Python Seçimi Sorunu
1. VSCode'u kapatıp açın
2. Command Palette > Python: Select Interpreter
3. Yenileme yapın ve venv'i seçin

## Faydalı VSCode Kısayolları
- ⌘ + ` : Terminal
- ⌘ + Shift + P : Komut Paleti
- ⌘ + S : Kaydet
- ⌘ + B : Kenar çubuğu
- F5 : Debug başlat

## Önemli Notlar
0. Python 3.8.10 Kullanımı:
   - Bu sürüm yapay zeka modelleriyle daha uyumlu
   - Kütüphanelerin test edilmiş kararlı sürümlerini kullanıyoruz
   - Daha güvenilir ve kararlı çalışma sağlar

1. İlk çalıştırmada:
   - Yapay zeka modelleri indirilecek (10-15 dk)
   - MacOS güvenlik uyarıları verebilir
   - "İzin Ver" seçeneğini seçin

2. Performans İyileştirmeleri:
   - Diğer uygulamaları kapatın
   - En az 4GB boş RAM olsun
   - VSCode'u yeniden başlatın

3. Hata Ayıklama:
   - Terminal çıktılarını kontrol edin
   - Debug modunda çalıştırın (F5)
   - Hata mesajlarını not alın

4. Güvenlik Uyarıları:
   - MacOS, ilk kez çalıştırıldığında güvenlik uyarısı verebilir
   - System Preferences > Security & Privacy'den izin verin 