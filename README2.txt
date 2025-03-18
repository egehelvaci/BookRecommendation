# Kitap Öneri Sistemi - MacOS Kurulum Kılavuzu

## Başlamadan Önce Gerekenler
- İnternet bağlantısı
- En az 5GB boş disk alanı
- MacOS işletim sistemi
- Terminal kullanımı için temel bilgi
+ NOT: Bu kurulum kılavuzu Python 3.12 kullanan sistemlerde de çalışacak şekilde hazırlanmıştır.
+ Conda ortamı sayesinde sisteminizdeki Python sürümünden bağımsız olarak çalışacaktır.

## ADIM 1: Homebrew Kurulumu
1. Terminal'i açın:
   - Spotlight Search'i açın (⌘ + Space)
   - "Terminal" yazın ve Enter'a basın

2. Homebrew'i kurun:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   - Kurulum sırasında Mac'inizin yönetici şifresi istenecektir
   - Bu şifre, Mac'inize giriş yaparken kullandığınız şifredir
   - Şifreyi yazıp Enter'a basın
   - Kurulum tamamlanana kadar bekleyin

## ADIM 2: Python 3.8 ve Anaconda Kurulumu
1. Önce Python 3.8'i Homebrew ile yükleyin:
   ```
   brew install python@3.8
   ```

2. Python 3.8'i PATH'e ekleyin:
   ```
   echo 'export PATH="/opt/homebrew/opt/python@3.8/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. Python sürümünü kontrol edin:
   ```
   python3.8 --version
   ```

4. Anaconda'yı yükleyin:
   ```
   brew install --cask anaconda
   ```

5. Anaconda'yı PATH'e ekleyin:
   ```
   echo 'export PATH="/opt/homebrew/anaconda3/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

## ADIM 3: Proje Dosyalarını Hazırlama
1. Masaüstünde KitapOneri klasörü oluşturun:
   ```
   cd ~/Desktop
   mkdir KitapOneri
   ```

2. Size verilen "KitapOneri.zip" dosyasını Masaüstüne kopyalayın
3. ZIP dosyasını çıkartın:
   ```
   cd ~/Desktop
   unzip KitapOneri.zip -d KitapOneri
   cd KitapOneri
   ```

## ADIM 4: Conda Ortamı Oluşturma
1. Terminal'de şu komutları sırayla yazın:
   ```
   conda create --name kitaponeri python=3.8
   ```
   Not: Burada özellikle Python 3.8 sürümünü belirtiyoruz
   - "Proceed ([y]/n)?" sorusuna "y" yazıp Enter'a basın

2. Ortamı aktifleştirin:
   ```
   conda activate kitaponeri
   ```
   Not: Terminal'de (kitaponeri) yazısını görmelisiniz

## ADIM 5: Gerekli Kütüphaneleri Yükleme
1. Conda'yı güncelleyin:
   ```
   conda update -n base -c defaults conda
   ```

2. Conda-forge kanalını ekleyin:
   ```
   conda config --add channels conda-forge
   ```

3. Kütüphaneleri tek komutla yükleyin:
   ```
   conda install transformers pytorch scikit-learn numpy pyqt
   ```
   - Her komut için "Proceed ([y]/n)?" sorusuna "y" yazıp Enter'a basın
   - Bu işlem 15-20 dakika sürebilir

## ADIM 6: Veritabanını Oluşturma
1. Terminal'de şu komutu yazın:
   ```
   python scrape_books.py
   ```

## ADIM 7: Programı Çalıştırma
1. Terminal'de şu komutu yazın:
   ```
   python gui.py
   ```

## Sorun Giderme

### Python Sürüm Hatası (3.12 Kullananlara Özel)
1. Önce mevcut ortamı kaldırın:
   ```
   conda deactivate
   conda remove --name kitaponeri --all
   ```
2. Yeni ortamı Python 3.8 ile oluşturun:
   ```
   conda create --name kitaponeri python=3.8
   conda activate kitaponeri
   ```
3. Kütüphaneleri conda ile yükleyin:
   ```
   conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
   ```

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

### Kütüphane Yükleme Hataları
1. Conda ortamında olduğunuzdan emin olun:
   ```
   conda activate kitaponeri
   ```
2. Conda-forge kanalını ekleyin:
   ```
   conda config --add channels conda-forge
   ```
3. Kütüphaneleri tekrar yüklemeyi deneyin:
   ```
   conda install transformers pytorch scikit-learn numpy pyqt
   ```

### "PyQt Hatası" veya "GUI Açılmıyor"
1. XQuartz'ı yükleyin:
   ```
   brew install --cask xquartz
   ```
2. Bilgisayarı yeniden başlatın
3. Programı tekrar çalıştırın

### Diğer Hatalar İçin
1. Python sürümünü kontrol edin:
   ```
   python --version
   ```
   Python 3.8.x çıktısı almalısınız

2. Tüm dosyaların klasörde olduğunu kontrol edin:
   ```
   ls
   ```
   Şu dosyaları görmelisiniz:
   - book_recommender.py
   - gui.py
   - scrape_books.py
   - books_database.json
   - requirements.txt

## Önemli Notlar
- Kurulum sırasında istenen şifre, Mac'inizin yönetici şifresidir
- Şifre girerken ekranda yıldız (*) görünmez, bu normal bir güvenlik önlemidir
- İlk çalıştırmada yapay zeka modelleri indirilecektir (10-15 dakika sürebilir)
- İnternet bağlantınızın olması gerekir
- İlk açılış yavaş olabilir, sonraki açılışlar daha hızlı olacaktır
- MacOS güvenlik uyarısı verebilir, "İzin Ver" seçeneğini seçin
- Tüm kurulum yaklaşık 30-45 dakika sürebilir

## Sistem Gereksinimleri
- MacOS Catalina (10.15) veya üzeri
- En az 4GB RAM
- En az 5GB boş disk alanı
- İnternet bağlantısı 