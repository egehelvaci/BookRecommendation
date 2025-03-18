# Kitap Öneri Sistemi - Visual Studio Code MacOS Kurulum Kılavuzu

## Başlamadan Önce Gerekenler
- İnternet bağlantısı
- En az 5GB boş disk alanı
- MacOS Catalina veya üzeri
- Terminal kullanımı için temel bilgi

## ADIM 1: Homebrew Kurulumu
1. Terminal'i açın:
   - Spotlight Search'i açın (⌘ + Space)
   - "Terminal" yazın ve Enter'a basın

2. Homebrew'i kurun:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   - Kurulum sırasında Mac şifrenizi girmeniz istenecektir
   - Şifre girerken karakterler görünmez, bu normaldir

## ADIM 2: Visual Studio Code Kurulumu
1. Homebrew ile VSCode'u yükleyin:
   ```
   brew install --cask visual-studio-code
   ```

2. Python Eklentilerini Yükleyin:
   - VSCode'u açın (⌘ + Space, "Visual Studio Code" yazın)
   - Command Palette'i açın (⌘ + Shift + P)
   - "Extensions: Install Extensions" yazın
   - Arama kutusuna "Python" yazın
   - Microsoft'un Python eklentisini yükleyin
   - "Jupyter" eklentisini de yükleyin

## ADIM 3: Anaconda Kurulumu
1. Homebrew ile Anaconda'yı yükleyin:
   ```
   brew install --cask anaconda
   ```

2. Anaconda'yı PATH'e ekleyin:
   ```
   echo 'export PATH="/opt/homebrew/anaconda3/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

## ADIM 4: Proje Dosyalarını Hazırlama
1. Masaüstünde KitapOneri klasörü oluşturun:
   ```
   cd ~/Desktop
   mkdir KitapOneri
   ```

2. ZIP dosyasını çıkartın:
   ```
   cd ~/Desktop
   unzip KitapOneri.zip -d KitapOneri
   ```

3. VSCode ile klasörü açın:
   ```
   code ~/Desktop/KitapOneri
   ```

## ADIM 5: Conda Ortamını Ayarlama
1. VSCode'da yeni terminal açın (⌘ + `)
2. Conda ortamı oluşturun:
   ```
   conda create --name kitaponeri python=3.8
   conda activate kitaponeri
   ```

3. VSCode'da Python yorumlayıcısını seçin:
   - ⌘ + Shift + P tuşlarına basın
   - "Python: Select Interpreter" yazın
   - Listeden "kitaponeri" ortamını seçin

## ADIM 6: Kütüphaneleri Yükleme
1. Terminal'de şu komutları çalıştırın:
   ```
   conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
   ```
   - Her komut için "Proceed ([y]/n)?" sorusuna "y" yazıp Enter'a basın

## ADIM 7: Projeyi Çalıştırma
1. Sol taraftaki Explorer'dan gui.py dosyasını açın
2. Sağ üst köşedeki Play (▶️) butonuna tıklayın
   veya
   Terminal'de şu komutu yazın:
   ```
   python gui.py
   ```

## Sorun Giderme

### "conda: command not found" Hatası
1. PATH'i kontrol edin:
   ```
   echo $PATH
   ```
2. Anaconda'yı PATH'e ekleyin:
   ```
   echo 'export PATH="/opt/homebrew/anaconda3/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### VSCode Python Yorumlayıcısı Görünmüyor
1. VSCode'u kapatıp açın
2. ⌘ + Shift + P > "Python: Select Interpreter"
3. "Refresh" seçeneğine tıklayın
4. Conda ortamları listede görünecektir

### "PyQt Hatası" veya "GUI Açılmıyor"
1. XQuartz'ı yükleyin:
   ```
   brew install --cask xquartz
   ```
2. Bilgisayarı yeniden başlatın
3. Programı tekrar çalıştırın

## Önemli VSCode Mac Kısayolları
- ⌘ + ` : Terminal'i aç/kapat
- ⌘ + Shift + P : Komut paletini aç
- F5 : Debug modunda çalıştır
- ⌘ + S : Kaydet
- ⌘ + Space : Kod önerilerini göster
- ⌘ + B : Sol kenar çubuğunu aç/kapat
- ⌘ + J : Alt paneli aç/kapat

## Önerilen VSCode Ayarları
1. settings.json dosyasına eklenebilecek ayarlar:
   ```json
   {
     "python.defaultInterpreterPath": "/opt/homebrew/anaconda3/envs/kitaponeri/bin/python",
     "python.formatting.provider": "black",
     "editor.formatOnSave": true,
     "python.linting.enabled": true
   }
   ```

## Not
- MacOS güvenlik uyarıları verebilir, "İzin Ver" seçeneğini seçin
- İlk çalıştırmada yapay zeka modelleri indirilecektir (10-15 dakika sürebilir)
- Debug modunda çalıştırırken daha detaylı hata mesajları alabilirsiniz
- Terminal'de conda komutları çalışmazsa yeni terminal açın
- M1/M2 Mac kullanıcıları için tüm kütüphaneler otomatik olarak ARM mimarisi için derlenecektir 