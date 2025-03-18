# Kitap Öneri Sistemi - Visual Studio Code Kurulum Kılavuzu

## Başlamadan Önce Gerekenler
- İnternet bağlantısı
- En az 5GB boş disk alanı
- Visual Studio Code yüklü olmalı
- Anaconda yüklü olmalı

## ADIM 1: Visual Studio Code Kurulumu
1. VSCode'u indirin:
   - https://code.visualstudio.com/ adresine gidin
   - "Download for Windows/Mac" butonuna tıklayın
   - İndirilen kurulum dosyasını çalıştırın

2. Python Eklentilerini Yükleyin:
   - VSCode'u açın
   - Sol taraftaki Extensions (Ctrl+Shift+X) sekmesine tıklayın
   - Arama kutusuna "Python" yazın
   - Microsoft'un Python eklentisini yükleyin
   - "Jupyter" eklentisini de yükleyin

## ADIM 2: Anaconda Kurulumu (Yüklü değilse)
1. Anaconda'yı indirin:
   - https://www.anaconda.com/download adresine gidin
   - İşletim sisteminize uygun sürümü indirin
   - Kurulum sırasında "Add Anaconda3 to PATH" seçeneğini işaretleyin

## ADIM 3: Proje Dosyalarını Hazırlama
1. Masaüstünde "KitapOneri" klasörü oluşturun
2. ZIP dosyasını bu klasöre çıkartın
3. VSCode'u açın
4. File > Open Folder ile KitapOneri klasörünü açın

## ADIM 4: Conda Ortamını Ayarlama
1. VSCode'da yeni terminal açın (Terminal > New Terminal)
2. Conda ortamı oluşturun:
   ```
   conda create --name kitaponeri python=3.8
   conda activate kitaponeri
   ```

3. VSCode'da Python yorumlayıcısını seçin:
   - Ctrl+Shift+P tuşlarına basın
   - "Python: Select Interpreter" yazın
   - Listeden "kitaponeri" ortamını seçin

## ADIM 5: Kütüphaneleri Yükleme
1. Terminal'de şu komutları çalıştırın:
   ```
   conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
   ```

## ADIM 6: Projeyi Çalıştırma
1. Sol taraftaki Explorer'dan gui.py dosyasını açın
2. Sağ üst köşedeki Play (▶️) butonuna tıklayın
   veya
   Terminal'de şu komutu yazın:
   ```
   python gui.py
   ```

## Sorun Giderme

### VSCode Python Yorumlayıcısı Görünmüyor
1. VSCode'u kapatıp açın
2. Ctrl+Shift+P > "Python: Select Interpreter"
3. "Refresh" seçeneğine tıklayın
4. Conda ortamları listede görünecektir

### Terminal'de Conda Komutu Tanınmıyor
1. VSCode'u kapatın
2. Anaconda'yı kaldırıp yeniden yükleyin
3. Kurulum sırasında "Add to PATH" seçeneğini işaretleyin
4. VSCode'u yeniden açın

### Modül Bulunamadı Hatası
1. Terminal'de ortamın aktif olduğundan emin olun:
   ```
   conda activate kitaponeri
   ```
2. Kütüphaneleri tekrar yükleyin:
   ```
   conda install -c conda-forge transformers pytorch scikit-learn numpy pyqt
   ```

### Debugging İpuçları
- F5 tuşu ile debug modunda çalıştırabilirsiniz
- Breakpoint koymak için satır numarasının yanına tıklayın
- Variables panelinden değişkenleri izleyebilirsiniz
- Debug Console'dan kod çalıştırabilirsiniz

## Önemli VSCode Kısayolları
- Ctrl+` : Terminal'i aç/kapat
- Ctrl+Shift+P : Komut paletini aç
- F5 : Debug modunda çalıştır
- Ctrl+F5 : Normal modda çalıştır
- Ctrl+S : Kaydet
- Ctrl+Space : Kod önerilerini göster

## Önerilen VSCode Ayarları
1. settings.json dosyasına eklenebilecek ayarlar:
   ```json
   {
     "python.defaultInterpreterPath": "conda env path",
     "python.formatting.provider": "black",
     "editor.formatOnSave": true,
     "python.linting.enabled": true
   }
   ```

## Not
- VSCode'un terminal'inde conda komutları çalışmazsa, Anaconda Prompt'u kullanabilirsiniz
- Debug modunda çalıştırırken daha detaylı hata mesajları alabilirsiniz
- Problem panelinden hataları takip edebilirsiniz
- Git entegrasyonu için Source Control panelini kullanabilirsiniz 