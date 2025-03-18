# Kitap Öneri Sistemi - MacOS Visual Studio Code Kurulum Kılavuzu (Sıfırdan)

## Başlamadan Önce
- MacOS yüklü bir bilgisayar
- İnternet bağlantısı
- En az 5GB boş alan
- Yönetici (admin) şifresi

## ADIM 1: Temel Kurulumlar
1. Terminal'i açın:
   - ⌘ + Space tuşlarına basın
   - "Terminal" yazın ve Enter'a basın

2. Homebrew'i kurun:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   - Mac şifrenizi girmeniz istenecek (yazarken görünmez)
   - Kurulum bitene kadar bekleyin

3. Visual Studio Code'u kurun:
   ```
   brew install --cask visual-studio-code
   ```

4. Anaconda'yı kurun:
   - https://www.anaconda.com/download adresine gidin
   - "Download for macOS" butonuna tıklayın (Intel x86_64)
   - İndirilen .pkg dosyasını çift tıklayın
   - Kurulum sihirbazını takip edin:
     * "Continue" > "Continue" > "Agree"
     * Install for "Just Me" seçin
     * Varsayılan kurulum konumunu değiştirmeyin
     * Mac şifrenizi girin

5. Anaconda'yı aktifleştirin:
   ```
   # Intel Mac için doğru yol
   /usr/local/anaconda3/bin/conda init zsh
   source ~/.zshrc
   ```

6. Kurulumu test edin:
   ```
   conda --version
   ```

## ADIM 2: Visual Studio Code Ayarları
1. VSCode'u açın:
   - ⌘ + Space tuşlarına basın
   - "Visual Studio Code" yazın ve Enter'a basın

2. Python eklentilerini yükleyin:
   - ⌘ + Shift + X tuşlarına basın
   - Arama kutusuna "Python" yazın
   - "Python" (Microsoft) eklentisini yükleyin
   - "Jupyter" eklentisini yükleyin

## ADIM 3: Proje Kurulumu
1. Proje klasörünü hazırlayın:
   ```
   cd ~/Desktop
   mkdir KitapOneri
   cd KitapOneri
   ```

2. Size verilen ZIP dosyasını Masaüstüne kopyalayın ve çıkartın:
   ```
   cd ~/Desktop
   unzip KitapOneri.zip -d KitapOneri
   ```

3. VSCode'da projeyi açın:
   ```
   code ~/Desktop/KitapOneri
   ```

## ADIM 4: Python Ortamı Kurulumu
1. VSCode'da terminal açın:
   - ⌘ + ` tuşlarına basın

2. Conda ortamını oluşturun:
   ```
   conda create --name kitaponeri python=3.8
   ```
   - "Proceed ([y]/n)?" sorusuna "y" yazın

3. Ortamı aktifleştirin:
   ```
   conda activate kitaponeri
   ```

4. Kütüphaneleri yükleyin:
   ```
   conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
   ```
   - Yükleme sırasında "y" yazıp onaylayın
   - Bu işlem 10-15 dakika sürebilir

## ADIM 5: VSCode Python Yorumlayıcı Seçimi
1. Command Palette'i açın:
   - ⌘ + Shift + P tuşlarına basın
2. "Python: Select Interpreter" yazın
3. Listeden "kitaponeri" ortamını seçin

## ADIM 6: Projeyi Çalıştırma
1. gui.py dosyasını açın:
   - Sol taraftan gui.py'a çift tıklayın
2. Sağ üstteki ▶️ (Play) butonuna tıklayın

## Olası Hatalar ve Çözümleri

### 1. "conda: command not found"
Şu komutu çalıştırın:
```
source ~/.zshrc
```

### 2. GUI Açılmıyor
XQuartz'ı yükleyin:
```
brew install --cask xquartz
```
Bilgisayarı yeniden başlatın

### 3. Kütüphane Hataları
Şu komutları sırayla çalıştırın:
```
conda deactivate
conda remove --name kitaponeri --all
conda create --name kitaponeri python=3.8
conda activate kitaponeri
conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
```

## Faydalı VSCode Kısayolları (Mac)
- ⌘ + ` : Terminal
- ⌘ + Shift + P : Komut Paleti
- ⌘ + S : Kaydet
- ⌘ + B : Kenar çubuğu
- F5 : Debug başlat

## Önemli Notlar
1. İlk çalıştırmada:
   - Yapay zeka modelleri indirilecek (10-15 dk)
   - MacOS güvenlik uyarıları verebilir
   - "İzin Ver" seçeneğini seçin

2. Intel Mac (i7) kullanıcıları için:
   - Kütüphaneler x86_64 mimarisi için derlenecek
   - Rosetta 2 gerektirmez
   - Daha hızlı kurulum ve çalışma sağlar

3. Performans için:
   - VSCode'u yeniden başlatın
   - Diğer uygulamaları kapatın
   - En az 4GB boş RAM olsun

4. Hata ayıklama için:
   - Terminal çıktılarını kontrol edin
   - Debug modunda çalıştırın (F5)
   - Hata mesajlarını not alın 